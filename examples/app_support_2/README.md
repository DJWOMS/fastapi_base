# FastAPI application support #2

Проект демонстрация организации проекта FastAPI с использованием паттерна Repository.

- FastAPI
- SqlAlchemy
- Postgres
- Alembic
- Docker

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

## Старт без Docker
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

### Установка poetry (не обязательно)
```
pip install poetry
```
### Установка зависимостей
```
poetry install
```
или
```
pip install -r requirements.txt
```

### База данных
В файл `.env` прописать свои настройки Postgres

### Alembic migrate
```
alembic upgrade head
```

### Старт
```
python main.py
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\docs
```
