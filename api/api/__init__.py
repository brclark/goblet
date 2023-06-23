from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://khcwijqquknjzc:a724588a50a8a689dea14299f55faa50560f9640321056783bae130416738eab@ec2-34-236-56-112.compute-1.amazonaws.com:5432/d9dfei58nqd9t4'
    app.config['SQLALCHEMY_ECHO'] = True

    with app.app_context():
        from .models import db
        from .schemas import ma
        from .resources import resource_bp

        db.init_app(app)
        db.create_all()

        
        # ma.init_app(app)
        # app.db = db

        # app.register_blueprint(resource_bp)

        # CORS(app)

        return app
