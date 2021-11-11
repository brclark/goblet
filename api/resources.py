from flask_restful import Resource
from schemas import player_schema, player_schemas
from schemas import opponent_schemas, opponent_schema
from schemas import game_schema, game_schemas
from schemas import point_schema, point_schemas
from schemas import tournament_schema, tournament_schemas
from models import Player, Opponent, Game, Point, Tournament


class PlayerListResource(Resource):
    def get(self):
        players = Player.query.all()
        print(players)
        return player_schemas.dump(players)


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
