import pytest
from server.models import Recipe, db

class TestRecipe:
    def test_has_attributes(self, app):
        with app.app_context():
            recipe = Recipe(title="Test", instructions="x"*50, minutes_to_complete=10)
            db.session.add(recipe)
            db.session.commit()
            assert hasattr(recipe, "title")
            assert hasattr(recipe, "instructions")
            assert hasattr(recipe, "minutes_to_complete")

    def test_requires_title(self, app):
        from sqlalchemy.exc import IntegrityError
        with app.app_context():
            recipe = Recipe(instructions="x"*50)
            db.session.add(recipe)
            with pytest.raises(IntegrityError):
                db.session.commit()
            db.session.rollback()
