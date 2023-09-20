# Базовый шаблон проекта для FastAPI

## Общее описание
### Директории

- core - директория для общих настроек
- core/database/db_config.py - настройки базы данных
- core/database/db_helper.py - получение сессии базы данных
- core/config.py - настройки для проекта
- share - базовые классы для models, repositories, services и т.д.
- migrations - директория alembic для миграций
- migrations/versions - файлы миграций
- migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
- migrations/env.py - скрипт alembic для работы миграций
- src - верхний уровень приложения, содержит общие маршруты, main.py, все сервисы (приложения)
- src/main.py - корень проекта, который запускает приложение FastAPI
- src/routes.py - общие routers для всех приложений проекта


### Файлы

- repository.py - repository
- controllers.py - ядро каждого модуля со всеми endpoints
- service.py - специфичная для модуля бизнес-логика
- models.py - для моделей БД
- schemas.py - для pydantic моделей
- routers.py - общие routers для всех контроллеров модуля
- dependencies.py - зависимости для приложения
- utils.py - функции, не относящиеся к бизнес-логике
- exceptions.py - специфические для модуля исключения
- constants.py - константы
