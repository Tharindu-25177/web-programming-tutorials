# Week 04 Django Templates and ORM – Beginner Project

## Run in VS Code (Windows)

Open this folder in VS Code and choose Terminal > New Terminal.

1. Create a virtual environment:
```powershell
python -m venv venv
```
2. Activate it:
```powershell
.\venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in the same terminal, then activate again. Or use Command Prompt: `venv\Scripts\activate.bat`.

3. Install Django:
```bash
python -m pip install -r requirements.txt
```
4. Create database tables:
```bash
python manage.py makemigrations myApp
python manage.py migrate
```
5. Add example students and modules:
```bash
python manage.py load_sample_data
```
6. Start the server:
```bash
python manage.py runserver
```

Open:
- Home: http://127.0.0.1:8000/
- Student 1: http://127.0.0.1:8000/myApp/1/
- Admin: http://127.0.0.1:8000/admin/

To create an admin login, open a second terminal while the server is running and run `python manage.py createsuperuser`.

## What this project demonstrates
- ORM: `Student.objects.all()`
- Student detail lookup using the URL's integer `student_id`
- URL configuration with `include()`
- Templates: `home.html` and `student_detail.html`
- Template inheritance using `base.html`
- Many-to-many relationship: `student.modules.all()`

Sample records are included through the `load_sample_data` command. If students already exist, it does not add duplicate sample students.
