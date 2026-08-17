import pytest

from app import Post, app, db


@pytest.fixture()
def client():
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SECRET_KEY="test-secret",
    )

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Blog" in response.data


def test_crud_workflow(client):
    response = client.post(
        "/posts/new",
        data={"title": "Test Post", "body": "Test body"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Test Post" in response.data

    post = db.session.execute(db.select(Post)).scalar_one()

    response = client.get(f"/posts/{post.id}")
    assert response.status_code == 200
    assert b"Test body" in response.data

    response = client.post(
        f"/posts/{post.id}/edit",
        data={"title": "Updated Post", "body": "Updated body"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Updated Post" in response.data

    response = client.post(f"/posts/{post.id}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated Post" not in response.data


def test_empty_post_is_rejected(client):
    response = client.post(
        "/posts/new",
        data={"title": "", "body": ""},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Title and body are required." in response.data
