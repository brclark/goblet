from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from time import time


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://goblet:goblet-api@localhost:8889/goblet'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


@app.route('/time')
def get_current_time():
    return {'time': time()}


if __name__ == '__main__':
    app.run(debug=True)
