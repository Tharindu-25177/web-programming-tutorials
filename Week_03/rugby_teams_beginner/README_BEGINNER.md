# Rugby Teams Django Project (Beginner Version)

This project follows the Week 03 Django practical ideas:
- Django project and app
- Models and a many-to-many relationship
- Database migrations
- Admin site
- CSV data import using `django-extensions`

## 1. Open the project

Extract the ZIP file. Open the `rugby_teams_beginner` folder in VS Code.

Open the VS Code terminal:
**Terminal > New Terminal**

## 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt terminal:

```bat
venv\Scripts\activate.bat
```

## 3. Install packages

```bash
python -m pip install -r requirements.txt
```

## 4. Create the database tables

```bash
python manage.py makemigrations teams
python manage.py migrate
```

## 5. Create an admin login

```bash
python manage.py createsuperuser
```

Enter a username, email (optional), and password.

## 6. Run the website

```bash
python manage.py runserver
```

Open this address in your browser:

http://127.0.0.1:8000/admin/

Sign in using the superuser details. Add and view Players and Positions.

## 7. Import the sample CSV data

The sample file `players.csv` is in the main project folder.

Run:

```bash
python manage.py runscript load_rugby_data
```

Refresh the Admin page to see the positions and players.

If Django says `runscript` is unknown, check that `django-extensions` is installed and that `django_extensions` is in `INSTALLED_APPS`.

## 8. How the models work

- One Player can have many Positions.
- One Position can belong to many Players.
- This is a many-to-many relationship.
- The three specialist positions are Tight Head Prop, Hooker, and Loose Head Prop.
- A player must have `specialist_eligible` selected before assigning one of those specialist positions in the Admin form.

## 9. Important beginner notes

- `models.py` describes the database tables.
- `admin.py` makes the models visible in Django Admin.
- `makemigrations` prepares database changes.
- `migrate` applies those changes to the SQLite database.
- `load_rugby_data.py` reads each row in `players.csv` and creates database records.

The CSV contains example data only. Replace it with your own class data if your tutor supplied a separate CSV.
