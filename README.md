# Flask Blog

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

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML5 / CSS3

## Project Structure

```text
flask-blog/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── new_post.html
│   ├── edit_post.html
│   └── post_detail.html
└── .gitignore
```

## Run Locally

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the app:

```bash
python app.py
```

5. Open `http://127.0.0.1:5000/` in your browser.

The SQLite database is created automatically on first run.

## What I Learned

This project helped me practice Flask routing, request handling, Jinja2 template inheritance, SQLAlchemy models and queries, CRUD workflows, server-side validation, flash messaging, and Git/GitHub version control.

## Production Next Steps

For a production deployment, I would move the secret key and database configuration into environment variables, disable Flask debug mode, add authentication/authorization, add automated tests, and deploy behind a production WSGI server.
