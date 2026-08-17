from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.secret_key = "change-this-later-to-something-random"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


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
            flash("Title aur body dono zaroori hain.")
            return redirect(url_for("new_post"))

        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        flash("Post successfully create ho gaya!")
        return redirect(url_for("home"))

    return render_template("new_post.html")


@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        body = request.form.get("body", "").strip()

        if not title or not body:
            flash("Title aur body dono zaroori hain.")
            return redirect(url_for("edit_post", post_id=post.id))

        post.title = title
        post.body = body
        db.session.commit()
        flash("Post update ho gaya!")
        return redirect(url_for("post_detail", post_id=post.id))

    return render_template("edit_post.html", post=post)


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post delete ho gaya.")
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Post.query.count() == 0:
            seed1 = Post(title="Mera Pehla Post", body="Ye maine apne Flask blog ka pehla post likha hai. Database working hai!")
            seed2 = Post(title="Dusra Post", body="Ye dusra fake post hai jo humne testing ke liye add kiya, taake home page pe kuch dikhe.")
            db.session.add_all([seed1, seed2])
            db.session.commit()
    app.run(debug=True)