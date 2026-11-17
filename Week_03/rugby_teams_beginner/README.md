# Week 03 - Introduction to Django

This project contains only the Rugby Players and Positions task from the tutorial.

## Run in VS Code on Windows

Open this folder in VS Code and open Terminal > New Terminal.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runscript load_players
python manage.py runserver
```

Open the Admin site: http://127.0.0.1:8000/admin/

## GitHub

The `venv` folder and local SQLite database are excluded using `.gitignore`.
