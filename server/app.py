from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # single SQLAlchemy instance

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # use your DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'

    db.init_app(app)

    from server.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app

# for running normally
app = create_app()
