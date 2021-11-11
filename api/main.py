from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from time import time
from resources import *


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


api.add_resource(PlayerListResource, '/players')
api.add_resource(PlayerResource, '/players/<int:player_id>')

api.add_resource(OpponentListResource, '/opponents')
api.add_resource(OpponentResource, '/opponents/<int:opponent_id>')

api.add_resource(GameListResource, '/games')
api.add_resource(GameResource, '/games/<int:game_id>')

api.add_resource(TournamentListResource, '/tournaments')
api.add_resource(TournamentResource, '/tournaments/<int:tournament_id>')

api.add_resource(PointListResource, '/points')
api.add_resource(PointResource, '/points/<int:point_id>')


if __name__ == '__main__':
    app.run(debug=True)
