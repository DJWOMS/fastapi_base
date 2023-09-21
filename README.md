# Базовый шаблон проекта для FastAPI

## Общее описание

### Примеры
В директории examples находятся примеры проектов.

Структура проекта, где все файлы разбиты по своим модулям. 
- [Пример #1](./examples/app_support)

Структура проекта, где файлы разбиты по приложениям проекта. 
- [Пример #2](./examples/app_support_2)

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

fastapi-project
├── alembic/
├── src
│ ├── auth
│ │ ├── router.py
│ │ ├── schemas.py # pydantic models
│ │ ├── models.py # db models
│ │ ├── dependencies.py
│ │ ├── config.py # local configs
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── aws
│ │ ├── client.py # client model for external service communication
│ │ ├── schemas.py
│ │ ├── config.py
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ └── utils.py
│ └── posts
│ │ ├── router.py
│ │ ├── schemas.py
│ │ ├── models.py
│ │ ├── dependencies.py
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── config.py # global configs
│ ├── models.py # global models
│ ├── exceptions.py # global exceptions
│ ├── pagination.py # global module e.g. pagination
│ ├── database.py # db connection related stuff
│ └── main.py
├── tests/
│ ├── auth
│ ├── aws
│ └── posts
├── templates/
│ └── index.html
├── requirements
│ ├── base.txt
│ ├── dev.txt
│ └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.in
