# Flask Blog

[![CI](https://github.com/contractwithshoaibnoor-star/flask-blog/actions/workflows/ci.yml/badge.svg)](https://github.com/contractwithshoaibnoor-star/flask-blog/actions/workflows/ci.yml)

A clean, server-rendered CRUD blog application built with **Python, Flask, Flask-SQLAlchemy, SQLite, and Jinja2**.

## Features

- Create, read, update, and delete blog posts
- SQLite persistence through SQLAlchemy ORM
- Server-side form validation
- Flash messages for user feedback
- Post detail pages
- Reverse chronological post listing
- Reusable Jinja2 template layout
- Responsive, accessible UI
- Automated tests for core CRUD flows
- GitHub Actions CI on pushes and pull requests

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML5 / CSS3
- Pytest
- GitHub Actions

## Project Structure

```text
flask-blog/
├── .github/
│   └── workflows/
│       └── ci.yml
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── new_post.html
│   ├── edit_post.html
│   └── post_detail.html
├── tests/
│   └── test_app.py
├── app.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Run Locally

### 1. Clone

```bash
git clone https://github.com/contractwithshoaibnoor-star/flask-blog.git
cd flask-blog
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and set a strong `SECRET_KEY` for local development. The database defaults to SQLite when `DATABASE_URL` is not provided.

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

The SQLite database is created automatically on first run.

## Run Tests

```bash
pytest -q
```

GitHub Actions runs the test suite automatically for pushes and pull requests targeting `main`.

## API / Routes

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/` | List posts |
| GET | `/about` | About page |
| GET | `/posts/<id>` | View a post |
| GET, POST | `/posts/new` | Create a post |
| GET, POST | `/posts/<id>/edit` | Edit a post |
| POST | `/posts/<id>/delete` | Delete a post |

## What I Learned

This project helped me practice Flask routing, request handling, Jinja2 template inheritance, SQLAlchemy models and queries, CRUD workflows, server-side validation, flash messaging, automated testing, CI, and Git/GitHub version control.

## Engineering Decisions

- **SQLite** keeps local development simple and requires no separate database server.
- **SQLAlchemy ORM** keeps database operations in Python models and queries.
- **POST for deletion** avoids using a state-changing operation through a normal GET request.
- **Environment-based configuration** keeps secrets and deployment-specific settings out of source code.
- **Pytest + GitHub Actions** provides a repeatable safety check for future changes.

## Production Next Steps

For a production deployment, I would add authentication and authorization, CSRF protection, stronger error handling, database migrations, structured logging, production configuration, and deployment behind a production WSGI server.
