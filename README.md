# LMS Project (Django REST Framework)

Бэкенд для LMS-системы (онлайн-обучения), реализованный на Django + DRF.

## Функциональность

### Модели
- **User** — кастомная модель на основе `AbstractBaseUser` (вход по email). Поля: `email`, `phone`, `city`, `avatar`.
- **Course** — модель курса: `title`, `preview`, `description`, `owner` (владелец).
- **Lesson** — модель урока: `course` (FK на Course), `title`, `description`, `preview`, `video_link`.

Связь: один курс — много уроков (ForeignKey с `related_name='lessons'`).

### API (DRF)

**Курсы (ViewSet):**
- `GET/POST /api/courses/`
- `GET/PUT/PATCH/DELETE /api/courses/<id>/`

**Уроки (Generic):**
- `GET/POST /api/lessons/`
- `GET/PUT/PATCH/DELETE /api/lessons/<id>/`

**Пользователи (ViewSet, дополнительное задание):**
- `GET/POST /api/users/`
- `GET/PUT/PATCH/DELETE /api/users/<id>/`

## Технологии
- Python 3.14
- Django 6.1
- Django REST Framework 3.18
- Pillow (для `ImageField`)
- SQLite

## Установка и запуск

1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
Установите зависимости:

```powershell 
pip install -r requirements.txt
```
Примените миграции:

```powershell
python manage.py migrate
```

Создайте суперпользователя:

```powershell
python manage.py createsuperuser
```

Запустите сервер:

```powershell
python manage.py runserver
```

## Тестирование

- Browsable API: http://127.0.0.1:8000/api/

- Для проверки CRUD используется Postman или встроенные HTML-формы DRF.

## Лицензия

### MIT

