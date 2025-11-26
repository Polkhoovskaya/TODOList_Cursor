# Django TODO List

Simple TODO tracker built with Django. You can create, edit, delete, and resolve TODO items with optional due dates.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate  # (On macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt  # or pip install django if you prefer
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000 to start managing tasks. Use the Django admin (`python manage.py createsuperuser`) if you want to manage TODOs through the admin interface.
