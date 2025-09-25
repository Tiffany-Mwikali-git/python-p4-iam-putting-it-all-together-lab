import pytest
from app import app, db

@pytest.fixture(scope="session")
def test_app():
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        TESTING=True,
        SECRET_KEY="test-secret",
    )
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
