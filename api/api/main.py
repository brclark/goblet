from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from time import time


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://khcwijqquknjzc:a724588a50a8a689dea14299f55faa50560f9640321056783bae130416738eab@ec2-34-236-56-112.compute-1.amazonaws.com:5432/d9dfei58nqd9t4'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/time')
def get_current_time():
    return {'time': time()}


if __name__ == '__main__':
    app.run(debug=True)
