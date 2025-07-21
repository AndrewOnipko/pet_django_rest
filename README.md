# Task Tracker

Минималистичное приложение для практики в Rest и Django для управления задачами с авторизацией.

---

## Стек

- **Backend**: Django 5 + Django REST Framework
- **Frontend**: React + Vite
- **Auth**: JWT (djangorestframework-simplejwt)
- **DB**: PostgreSQL (Docker)
- **Dev tools**: Docker Compose, Axios

---

## Быстрый старт (через Docker)

```bash
# 1. Склонировать проект
git clone https://github.com/your-user/django_rest_proj.git
cd django_rest_proj

# 2. Создать .env файл
cp .env.example .env
# (Заполните переменные при необходимости)

# 3. Запустить контейнеры
docker-compose up --build

# 4. Открыть в браузере
Backend: http://localhost:8000  
Frontend: http://localhost:5173
```

## Структура проекта

```bash
tasks_tracker/
├── config/               # Настройки Django
├── core/
│   └── enums/            # Перечисления (TaskStatus и т.д.)
├── tasks/
│   ├── models/           # Модели (MyTask)
│   ├── services/         # Бизнес-логика
│   ├── repositories/     # Работа с ORM и SQL
│   ├── selectors/        # Чтение из БД
│   ├── views_drf.py      # DRF Views
│   ├── serializers.py
│   └── routers/          # Разделённые маршруты
├── users/                # Расширение или настройка auth
└── ...
```

## Авторизация

- Используется JWT (/api/token/)

- После входа токен сохраняется в localStorage

- Все API-запросы требуют Bearer токен


```env
# .env (частично)
DJANGO_SUPERUSER_USERNAME=some_name
DJANGO_SUPERUSER_PASSWORD=some_pass
```

## Команды для запуска

```bash
# В директории проекта:
npm run dev

# Активировать Pyton в Django (допустим если работаете не напрямую в контейнере)
docker exec -it django bash

# Создать миграции
python manage.py makemigrations

# Провести миграции
python manage.py migrate
```

## TODO 

Когда нибуть потом:

1. Добавить сервисный слой (services/) - для write-операций, чтобы views были как можно тоньше.

2. Селекторы (selectors/) - для кастомных read-запросов (например, сортировка, фильтрация).

3. Типизация.

4. Тесты - для практики в unit-тестах на модели, сериализаторы и views.

5. Проверка прав доступа - если буду реализовывать различные роли.

6. Разделить views на файлы по ресурсу, особенно если будут другие модели.
