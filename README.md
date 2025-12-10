# Student Portal

Project: Student Portal — a Django-based student management application.

Description
-----------
A modular Django application with custom authentication and role-ready architecture, separate apps for `students` and `school`, static/media handling via WhiteNoise, and environment-driven configuration that supports SQLite for local development and PostgreSQL for Docker/production.

Tech stack
----------
- Python 3.10
- Django
- SQLite / PostgreSQL
- WhiteNoise (static file serving)
- python-dotenv (load `.env`)

Quick Start (Development)
-------------------------
1. Clone the repository:

```bash
git clone https://github.com/benah0987/student-portal.git
cd student-portal
```

2. Activate the virtual environment:

```bash
source Home/env/bin/activate
```

3. Install dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root (see `ENV SAMPLE` below).

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

7. Open your browser at `http://127.0.0.1:8000`.

Important files & structure
---------------------------
- `manage.py` — Django management entry point (run from repository root).
- `Home/Home/settings.py` — main settings (loads `.env` via `python-dotenv`).
- `Home/__init__.py` — outer package marker so `Home.Home.*` imports work.
- Apps: `home_auth`, `student`, `school` under the `Home/` package.

ENV SAMPLE
----------
Create a `.env` file in the project root with values like the following (do NOT commit secrets):

```env
SECRET_KEY=replace-this-with-your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=sqlite

# For Postgres (set DB_ENGINE=postgres to use these values)
POSTGRES_DB=student_portal
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
```

Commands (copy/paste)
---------------------
Run these from the repository root:

```bash
# change to project directory
cd ~/developer/student-portal

# activate virtualenv
source Home/env/bin/activate

# install dependencies (if needed)
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# run development server
python manage.py runserver 0.0.0.0:8000
```

Troubleshooting & notes
-----------------------
- If you see import errors for `Home.Home.*`, ensure you're running `manage.py` from the repository root and `Home/__init__.py` exists (it does).
- If Django cannot find the settings module, check `DJANGO_SETTINGS_MODULE` or ensure `PYTHONPATH` includes the repository root (export `PYTHONPATH="$PWD"`).
- If dependencies are missing, confirm the virtualenv is activated: `source Home/env/bin/activate`.
- For production, run `python manage.py collectstatic --noinput` and configure a proper WSGI server.
- To use PostgreSQL via Docker, set `DB_ENGINE=postgres`, run your database container (for example `docker-compose up -d`), then run migrations.

LinkedIn Post (Ready to publish)
--------------------------------
I'm excited to share "Student Portal" — a Django-based student management app I built to simplify school workflows.

Highlights:
- Custom user authentication & role-ready architecture
- Modular apps for students and schools
- Environment-driven settings (works with SQLite locally, Postgres in Docker/production)
- Static + media handling with WhiteNoise for easy deployment

Try it locally:

```bash
source Home/env/bin/activate
pip install -r requirements.txt
python manage.py migrate && python manage.py runserver 0.0.0.0:8000
```

Repository & demo: <link-to-repo-or-demo>

Feedback, suggestions, or contributions welcome — DM or open a PR!  
#Django #Python #WebDevelopment #OpenSource #EdTech

—
If you'd like, I can also:
- add a `.env.example` file to the repo,
- create a short `RUNNING.md` with troubleshooting screenshots, or
- open a commit/PR with these changes.

Files updated: `README.md`
