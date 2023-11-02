# Базовый шаблон проекта для FastAPI

## Общее описание
Пример приведенный ниже, подсказывают как можно организовать структуру проекта FastAPI.

Так же предложен вариант использования паттерна Dependency Injection.
И как один из способов реализации слоистой архитектуры.

Принцип заключается в том, чтобы разделить логику и код на слои. 

Что позволит иметь:
- более поддерживаемую и понятную структуру проекта.
- масштабирование и переиспользование кода.
- возможность тестирования отдельных частей проекта.

#### Будет полезным для ознакомления (видео)
[Слоистая архитектура](https://youtu.be/aF5_niKPL6c?si=sEqSQYFqU9kPsVDp)

[Слоистая Архитектура на FastAPI](https://youtu.be/8Im74b55vFc?si=0-ZwffTNCdT6VZAx)

## Инструменты
- FastAPI
- SqlAlchemy
- Postgres
- Alembic
- Docker


## Архитектура и структура

### Контексты
Отчасти подобие элемента DDD (Domain-driven design) - ограниченный контекст (bounded context). 

Не требуется глубоко разбираться в [DDD](https://habr.com/ru/companies/oleg-bunin/articles/551428/), 
но без понимания контекста никуда.

### Контроллеры 
Контроллеры везде называют по разному: `routers`, `endpoints`, `controllers`, мы используем
`controllers`.

Контроллеры отвечают за запрос\ответ.
Можно сказать что они должны быть "тупые", не иметь бизнес-логики, вообще не иметь бизнес-логики.

Они вызывают нужные зависимости: авторизация, проверка прав и т.д. 
Передают данные в сервис. Обрабатывают `HttpExceptions`.

### Сервисы
Сервис - это "бизнес контроллеры", отвечает за бизнес логику, взаимодействуют с 
репозиторием и другими сервисами.

Если в пределах одной сессии (в нашем случае SqlAlchemy) нужно взаимодействовать с 
несколькими репозиториями, то следует использовать QueryRepository.

### Репозитории
Репозиторий — это коллекция, которая содержит сущности, может фильтровать и возвращать
результат обратно, в зависимости от требований нашего приложения. Где и как он хранит 
эти объекты, является ДЕТАЛЬЮ РЕАЛИЗАЦИИ.

В нашем случае репозиторий может взаимодействовать с базой данных, например Postgres, Redis, 
MongoDB.

Каждый отдельный репозиторий взаимодействует только с одной моделью (таблицей).

Паттерн репозиторий служит цели отделить логику работы с БД от бизнес-логики приложения.
Лично для себя выделяю основной плюс в переиспользовании методов выборки. 

Примерами методов репозитория могут быть такие названия методов как:
- get_single()
- get_by_id()
- get_user_list()
- get_multi()
- и т.д.

Также репозиторий может использоваться для create/update/delete операций.

## Структура
Контексты - отдельная часть логики проекта. 
Содержит свои контроллеры, сервисы, репозитории, зависимости, модели, exceptions и т.д.


### Способ организации кода
- Файлы находятся в папке разбитые по контекстам. 
Каждый контекст относится к определенной сущности либо бизнес-процессу.
- Для выборок данных используем паттерн репозиторий.
- Бизнес-логика и операции создания/изменения моделей выносим в сервис-классы. 
Сервис классы не хранят свое состояние, что позволяет их переиспользовать без повторной 
инициализации.
- Для того чтобы не зависеть от Request в сервисы передаем либо одиночные параметры, 
либо DTO (Pydantic Model). 
Это позволяет переиспользовать код вне контроллеров (например, команда создания нового 
пользователя и т.д.).
- Стараемся, чтобы модели оставались максимально тонкими. В основном содержат в себе связи 
(relations).

### Пример проекта
Структура проекта, где файлы разбиты по контекстам проекта. 

Проект заглушка, пример организации кода.
- [Пример](./examples/app_support)

### Структуры проекта
```
├── migrations/
├── src
│   ├── config/
│   │   ├── database
│   │   │   ├── db_config.py
│   │   │   └── db_helper.py
│   │   └── project_config.py
│   ├── support/ # контекст
│   │   ├── controllers/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── models/
│   │   └── routes.py
│   ├── user/ # контекст
│   │   ├── user_service.py
│   │   ├── user_repository.py
│   │   ├── user_model.py
│   │   ├── user_contoller.py
│   │   ├── user_schema.py
│   │   └── routes.py
│   ├── auth/ # контекст
│   │   └── auth_service.py
│   ├── lib/ # библиотека
│   │   ├── interfaces/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   └── services/
│   ├── routes.py
│   └── main.py
├── tests/
├── pyproject.toml
├── .env
├── .gitignore
└── alembic.ini
```

### Директории и файлы
#### Основное
- migrations - директория alembic для миграций
- migrations/versions - файлы миграций
- migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
- migrations/env.py - скрипт alembic для работы миграций
-
- src - верхний уровень, содержит общие routes, main.py и все контексты
- src/config - директория для общих настроек
- src/config/database/db_config.py - настройки базы данных
- src/config/database/db_helper.py - получение сессии базы данных
- src/config/project_config.py - настройки для проекта
- src/main.py - корень проекта, который запускает приложение FastAPI
- src/routes.py - общие routers для всех приложений проекта
-
- tests - тесты проекта
- .env.example - пример (шаблон) для файла .env, переменные окружения
- pyproject.toml - файл зависимостей для [poetry](https://python-poetry.org/docs/)
- poetry.lock - обеспечить согласованность между текущими установленными зависимостями и 
теми, которые вы указали в файле pyproject.toml

#### Контексты
- src/support - контекст поддержки
- src/auth - контекст авторизации
- src/user - контекст пользователей

#### Библиотека (переиспользуемый код)
- src/lib - библиотека общих классов. Переиспользуемый код.
- src/lib/interfaces - директория для классов интерфейсов
- src/lib/models/base_model - базовый класс SqlAlchemy
- src/lib/schemas/base_schema - класс базовой модели Pydantic, с настройкой для интеграция с ORM (Ранее известный 
как "ORM Mode"/from_orm)
- src/lib/repositories/base_repository - класс базового repository
- src/lib/repositories/sqlalchemy_repository - класс базового repository для
сессии SqlAlchemy
- src/lib/services/base_service - базовый класс сервиса (CRUD) для взаимодействия с repository

### Файлы контекста
- prefix_controller.py - контроллеры контекста
- prefix_repository.py - работа с БД (Postgres, Redis, MongoDB и т.д.)
- prefix_service.py - специфичная для модуля бизнес-логика
- prefix_schema.py - pydantic модели
- routes.py - общие routes для всех контроллеров контекста
- prefix_model.py - модели ORM

### Дополнительные файлы контекста
- dependencies.py - зависимости для контекста
- exceptions.py - специфические для контекста исключения
- constants.py - константы контекста

## Соглашения

- Логическая часть проекта находиться внутри контекста 
- Контекст называем в единственном числе (например session, user, support)
- Избегаем длинных названий файлов и используем `_` (например user_service.py)
- Сущности более одной собираются в папки (например services, schemas)
- Поддерживаем цепочку Controller -> Service -> Repository
- Запросы контекста пишем в локальном репозитории (например support_repository.py)

## Импорты
Вначале, описываем библиотеки, группируем логически.

```
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from fastapi import Depends, HTTPException, APIRouter


```

Перечисляем используемые контексты.
```
from ...auth.user_schema import UserSchema
from ...auth.auth_service import is_admin
```

В конце, локальные зависимости контекста.

```
from ..schemas.support_schema import (
    CreateSupportSchema,
    UpdateSupportSchema,
    SupportResponseSchema
)
from ..services.support_service import SupportService
```

## Что дополнительно можно почитать
[DTO в Python. Способы реализации](https://habr.com/ru/articles/752936/)
[Python и чистая архитектура](https://habr.com/ru/companies/piter/articles/588669/)
[Архитектура ПО](https://backendinterview.ru/architecture/index.html)
[Bounded contexts будь проще](https://youtu.be/r_HYgERfMos?si=ZbcPAzIaFzGpkB_D)

## Старт с Docker
```
docker-compose up --build
```

### Alembic migrate
Не выключая контейнеры выполнить команду
```
docker exec -it app-net-back alembic upgrade head
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\docs
```

### Alembic создание migrations
Не выключая контейнеры выполнить команду
```
docker exec -it app-net-back alembic revision --autogenerate -m 'название модели или миграции'
```
