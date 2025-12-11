Render deployment guide
======================

This project can be deployed quickly to Render (https://render.com). Render connects to GitHub, builds your project, and provides a public URL and automatic TLS.

Steps to deploy on Render
1. Ensure your repo is pushed to GitHub and up-to-date.
2. Confirm `gunicorn` is present in `requirements.txt` (already included).
3. In your Render dashboard, create a new **Web Service** and connect to this repository and the `main` branch.
   - Build command: leave blank (Render will run `pip install -r requirements.txt`) or set `pip install -r requirements.txt`.
   - Start command: leave blank if you added a `Procfile` (Procfile `web: gunicorn Home.wsgi:application --bind 0.0.0.0:$PORT`).
4. Add environment variables in the Render service settings (Environment -> Environment Variables):
   - `SECRET_KEY` (set to a secure random value)
   - `DEBUG` = `false`
   - `ALLOWED_HOSTS` = your domain(s) or the Render service URL
   - `DATABASE_URL` if you use a managed Postgres database (recommended)
5. (Optional) Add a managed Postgres database on Render and set the `DATABASE_URL` accordingly.
6. Configure static files:
   - This project uses WhiteNoise (listed in `requirements.txt`). Ensure `whitenoise.middleware.WhiteNoiseMiddleware` is in `MIDDLEWARE` in `Home/Home/settings.py` and `STATIC_ROOT` is configured. Render will serve static files when `collectstatic` runs.
7. Migrations / collectstatic:
   - You can run migrations and collectstatic in a Render build hook or via the shell after deploy:
     - `python manage.py migrate`
     - `python manage.py collectstatic --noinput`

Notes
- Do not commit real secrets. Use the Render environment variable editor.
- For file uploads (media), use S3 or another persistent storage in production — Render's ephemeral filesystem will not persist uploaded files between deploys.

Quick local test
----------------
Run gunicorn locally to confirm the app starts:
```bash
source Home/env/bin/activate
pip install -r requirements.txt
gunicorn Home.wsgi:application --bind 0.0.0.0:8000
```
