import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///blog.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-change-me")

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


@app.route("/")
def home():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)


@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()

        if not title or not body:
            flash("Title and body are required.")
            return redirect(url_for("new_post"))

        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        flash("Post published successfully!")
        return redirect(url_for("home"))

    return render_template("new_post.html")


@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()

        if not title or not body:
            flash("Title and body are required.")
            return redirect(url_for("edit_post", post_id=post.id))

        post.title = title
        post.body = body
        db.session.commit()
        flash("Post updated successfully!")
        return redirect(url_for("post_detail", post_id=post.id))

    return render_template("edit_post.html", post=post)


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Post.query.count() == 0:
            seed_posts = [
                Post(
                    title="Welcome to Flask Blog",
                    body="This is a sample post demonstrating the Flask, SQLAlchemy and SQLite stack.",
                ),
                Post(
                    title="Getting Started",
                    body="Create, edit and delete posts to explore the CRUD workflow.",
                ),
            ]
            db.session.add_all(seed_posts)
            db.session.commit()

    app.run(debug=os.getenv("FLASK_DEBUG", "0") == "1")
