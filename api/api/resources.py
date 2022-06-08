from flask_restful import Resource, Api
from flask import Blueprint
from .schemas import player_schema, player_schemas
from .schemas import opponent_schemas, opponent_schema
from .schemas import game_schema, game_schemas
from .schemas import point_schema, point_schemas
from .schemas import tournament_schema, tournament_schemas
from .schemas import player_point_schema
from .models import Player, Opponent, Game, Point, Tournament


resource_bp = Blueprint("resource_bp", __name__)
api = Api(resource_bp)


class PlayerListResource(Resource):
    def get(self):
        players = Player.query.all()
        print(players)
        return player_schemas.dump(players)


class PlayerPointResource(Resource):
    def get(self, player_id):
        player = Player.query.get_or_404(player_id)
        return player_point_schema.dump(player)


class PlayerResource(Resource):
    def get(self, player_id):
        player = Player.query.get_or_404(player_id)
        return player_schema.dump(player)


class OpponentListResource(Resource):
    def get(self):
        opponents = Opponent.query.all()
        return opponent_schemas.dump(opponents)


class OpponentResource(Resource):
    def get(self, opponent_id):
        opponent = Opponent.query.get_or_404(opponent_id)
        return opponent_schema.dump(opponent)


class GameListResource(Resource):
    def get(self):
        games = Game.query.all()
        return game_schemas.dump(games)


class GameResource(Resource):
    def get(self, game_id):
        game = Game.query.get_or_404(game_id)
        return game_schema.dump(game)


class TournamentListResource(Resource):
    def get(self):
        print("here")
        tournaments = Tournament.query.all()
        print(tournaments)
        return tournament_schemas.dump(tournaments)


class TournamentResource(Resource):
    def get(self, tournament_id):
        tournament = Tournament.query.get_or_404(tournament_id)
        return tournament_schema.dump(tournament)


class PointListResource(Resource):
    def get(self):
        points = Point.query.all()
        return point_schemas.dump(points)


class PointResource(Resource):
    def get(self, point_id):
        point = Point.query.get_or_404(point_id)
        return point_schema.dump(point)


api.add_resource(PlayerListResource, '/players')
api.add_resource(PlayerResource, '/players/<int:player_id>')
api.add_resource(PlayerPointResource, '/players/<int:player_id>/points')
api.add_resource(OpponentListResource, '/opponents')
api.add_resource(OpponentResource, '/opponents/<int:opponent_id>')
api.add_resource(GameListResource, '/games')
api.add_resource(GameResource, '/games/<int:game_id>')
api.add_resource(TournamentListResource, '/tournaments')
api.add_resource(TournamentResource, '/tournaments/<int:tournament_id>')
api.add_resource(PointListResource, '/points')
api.add_resource(PointResource, '/points/<int:point_id>')
