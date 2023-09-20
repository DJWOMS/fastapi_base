# Базовый шаблон проекта для FastAPI

Директории

core - директория для общих настроек
core/db.py - настройки базы данных
core/settings.py - настройки для проекта
core/db/session.py - настройки сессии БД
core/share - базовые классы для controllers, models, services и т.д.
media - media файлы: картинки, pdf и т.д.
static - static файлы: css, js и т.д.
migrations - директория alembic для миграций
migrations/versions - файлы миграций
migrations/base.py - файл с импортированными модулями моделей для работы автогенерации миграций
migrations/env.py - скрипт alembic для работы миграций
src - верхний уровень приложения, содержит общие маршруты, main.py, все сервисы (приложения)
src/main.py - корень проекта, который запускает приложение FastAPI
src/routers.py - общие routers для всех приложений проекта


Файлы
Каждый пакет (приложение) имеет свои router, schemas, models и т.д.

repository.py - repository
controllers.py - ядро каждого модуля со всеми endpoints
service.py - специфичная для модуля бизнес-логика
models.py - для моделей БД
schemas.py - для pydantic моделей
routers.py - общие routers для всех контроллеров модуля
dependencies.py - зависимости для приложения
utils.py - функции, не относящиеся к бизнес-логике
exceptions.py - специфические для модуля исключения
constants.py - константы
