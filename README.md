# Базовый шаблон проекта для FastAPI

## Общее описание

<img src="/examples/uow.jpg"/>

Примеры приведенные ниже, подсказывают как можно организовать структуру проекта FastAPI.

Так же предложен вариант использования паттернов Dependency Injection и Unit of Work.
Принцип заключается в том, чтобы разделить логику и код на слои. 

Что позволит иметь:
- более поддерживаемую и понятную структуру проекта
- масштабирование и переиспользование кода
- возможность тестирования отдельных частей проекта

## О слоях

### Контроллеры 
Контроллеры мы можем называть по разному: `routers`, `endpoints`, `controllers`.

Контроллеры отвечают за запрос\ответ. Можно сказать что они должны быть "тупые", не иметь бизнес-логики.
Они вызывают нужные зависимости: авторизация, проверка прав и т.д. Передают данные в сервис. Обрабатывают 
`HttpExceptions`.

Нужно использовать зависимости (`Depends`) так как они кешируются.
Зависимости можно использовать повторно несколько раз — FastAPI по 
умолчанию кэширует результат зависимости в пределах области запроса, т.е. если у нас есть зависимость, 
которая вызывает сервис, мы не будем посещать БД каждый раз, когда вызываем эту 
зависимость — только первый вызов функции.

Зная это, мы можем легко разделить зависимости на несколько более мелких функций, которые работают в 
меньшем домене и легче повторно использовать в других маршрутах.

### Сервисы
Сервис отвечает за бизнес логику и взаимодействуют с репозиторием.

Если в пределах одной сессии (в нашем случае SqlAlchemy) нужно взаимодействовать с несколькими репозиториями, то
следует использовать Unit of Work.

### Репозитории
Репозиторий — это коллекция, которая содержит сущности, может фильтровать и возвращать
результат обратно, в зависимости от требований нашего приложения. Где и как он хранит эти объекты, 
является ДЕТАЛЬЮ РЕАЛИЗАЦИИ.

В нашем случае репозиторий может взаимодействовать с базой данных, например Postgres, Redis, MongoDB.

### Unit of Work
Если сказать просто, UoW это класс, который объединяет репозитории.

Паттерн Unit of Work помогает упростить работу с различными репозиториями и дает уверенность, что все 
репозитории будут использовать один и тот же DbContext.

Так же использование паттерна Репозиторий и UoW позволяет создать правильную структуру для развертывания 
приложения и внедрения DI, которые как минимум помогают в тестировании проекта.

### Пример проекта
Структура проекта, где файлы разбиты по приложениям проекта. 
- [Пример #2](./examples/app_support_2)

### Пример структуры проекта
```
├── migrations/ или alembic/
├── core/
│   ├── databases
│   │   ├── db_config.py
│   │   └── db_helper.py
│   └── config.py
├── share/ 
├── src
│   ├── support
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── repositories.py
│   │   ├── service.py
│   │   └── utils.py
│   └── users
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── dependencies.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── repositories.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── routes.py
│   └── main.py
├── tests/
│   ├── users
│   └── support
├── pyproject.toml или requirements.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
```

### Директории и файлы

- core - директория для общих настроек
- core/database/db_config.py - настройки базы данных
- core/database/db_helper.py - получение сессии базы данных
- core/config.py - настройки для проекта
- migrations (alembic) - директория alembic для миграций
- migrations/versions - файлы миграций
- migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
- migrations/env.py - скрипт alembic для работы миграций
- src - верхний уровень приложения, содержит общие маршруты, main.py, все сервисы (приложения)
- src/main.py - корень проекта, который запускает приложение FastAPI
- src/routes.py - общие routers для всех приложений проекта
- tests - тесты проекта
- .env - переменные окружения
- .env.example - пример (шаблон) для файла .env
- pyproject.toml - файл зависимостей для [poetry](https://python-poetry.org/docs/)
- poetry.lock - обеспечить согласованность между текущими установленными зависимостями и 
теми, которые вы указали в файле pyproject.toml
- requirements.txt - файл зависимостей для pip

### Директория share
- share - базовые (примеры) классы для models, repositories, services и т.д. которые доступны
во всём проекте
- share/interfaces - директория для классов интерфейсов
- share/interfaces/permissions - абстрактный класс permission
- share/interfaces/repository - абстрактный класс repository
- share/exceptions (errors) - классы exceptions
- share/generic - класс generic для сервисов
- share/models - класс базовой модели SqlAlchemy
- share/repository - класс базового repository для SqlAlchemy
- share/schemas - класс базовой модели Pydantic, с настройкой для интеграция с ORM (Ранее известный 
как "ORM Mode"/from_orm)
- share/service - базовый класс сервиса (CRUD) для взаимодействия с repository
- share/uow - реализация Unit of Work для использования нескольких репозиториев в одной сессии SqlAlchemy


### Файлы приложения

- repository.py - работа с БД (Postgres, Redis, MongoDB и т.д.)
- service.py - специфичная для модуля бизнес-логика
- models.py - моделей для БД
- schemas.py - pydantic модели
- routers.py - общие routers для всех контроллеров (endpoints, api) модуля
- dependencies.py - зависимости для приложения
- utils.py - функции, не относящиеся к бизнес-логике
- exceptions.py - специфические для модуля исключения
- constants.py - константы


