from flask import Flask


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

        app.register_blueprint(resource_bp)

        return app
