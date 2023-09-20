# FastAPI application support

## Folders

- core - directory for common settings
- core/db.py - database settings
- core/settings.py - project settings
- core/db/session.py - database session settings
- core/share - base classes for controllers, models, services, etc.
- media - media files: images, PDFs, etc.
- static - static files: CSS, JS, etc.
- migrations - alembic directory for database migrations
- migrations/versions - migration files
- migrations/base.py - file with imported model modules for migration auto generation
- migrations/env.py - alembic script for migrations
- src - top-level directory of the application, contains common routes, main.py, all services (applications)
- src/main.py - project root that launches the FastAPI application
- src/routers.py - common routers for all project applications

## Files
Each package (application) has its own routers, schemas, models, etc.

- repository.py - repository
- controllers.py - core of each module with all endpoints
- service.py - module-specific business logic
- models.py - database models
- schemas.py - pydantic models
- routers.py - common routers for all module controllers
- dependencies.py - dependencies for the application
- utils.py - utility functions not related to the business logic
- exceptions.py - module-specific exceptions
- constants.py - constants


## Start

### Virtualenv
```
python -m venv venv
```
- Linux / MacOS
```
venv/bin/activate
```
- Windows
```
python venv\Scripts\activate
```

### Install poetry
```
pip install poetry
```
### Install requirements
```
poetry install
```

### Alembic migrate
```
alembic upgrade head
```

### Start
```
python main.py
```

### Go to
```
http:\\127.0.0.1:8000\docs
```
