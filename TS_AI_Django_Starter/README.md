# TS AI Django Starter

A ready-to-run Django + DRF project with a multi-tab frontend (Bootstrap), CRUD for Users/Products/Tasks/Orders, analytics, search, and test endpoints.

## Quickstart

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r ../requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver 5000
```

Open: http://127.0.0.1:5000/

API base: `/api/`
