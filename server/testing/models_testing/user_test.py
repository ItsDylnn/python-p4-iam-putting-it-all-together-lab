import pytest
from server.models import User, Recipe

class TestUser:
    def test_has_attributes(self, app):
        with app.app_context():
            user = User(username="testuser", _password_hash="hashed")
            db = user.query.session
            db.add(user)
            db.commit()
            assert hasattr(user, "username")
            assert hasattr(user, "_password_hash")
            assert hasattr(user, "image_url")
            assert hasattr(user, "bio")

    def test_requires_username(self, app):
        from sqlalchemy.exc import IntegrityError
        with app.app_context():
            from server.models import db
            user = User(_password_hash="hashed")
            db.session.add(user)
            with pytest.raises(IntegrityError):
                db.session.commit()
            db.session.rollback()
