# FastAPI application support #1

Проект демонстрация организации проекта FastAPI с использованием паттерна Repository. 


## Старт
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
