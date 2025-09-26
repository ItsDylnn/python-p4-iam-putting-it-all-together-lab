from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from server.models import db, User  # make sure your User model exists

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TESTING"] = True

    db.init_app(app)

    # -----------------------------
    # Signup route
    # -----------------------------
    @app.route("/signup", methods=["POST"])
    def signup():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"error": "Missing username or password"}, 422

        # Check if username exists
        if User.query.filter_by(username=username).first():
            return {"error": "Username already exists"}, 422

        user = User(username=username)
        user.set_password(password)  # make sure you have a set_password method
        db.session.add(user)
        db.session.commit()

        return {"id": user.id, "username": user.username}, 201

    return app
