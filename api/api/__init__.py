from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://goblet:goblet-api@localhost:8889/goblet'
    app.config['SQLALCHEMY_ECHO'] = True

    with app.app_context():
        from .models import db
        from .schemas import ma
        from .resources import resource_bp

        db.init_app(app)
        ma.init_app(app)
        app.db = db

        app.register_blueprint(resource_bp)

        CORS(app)

        return app
