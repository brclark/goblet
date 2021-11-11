from flask_marshmallow import Schema
from models import Tournament, Opponent, Player, Game, Point


# class RequestPathParamsSchema(ma.Schema):
#     pass
#
#
# class RequestQueryParamsSchema(ma.Schema):
#     pass
#
#
# class RequestBodyParamsSchema(ma.Schema):
#     pass


class TournamentSchema(Schema):
    class Meta:
        fields = ("id", "name", "nickname", "location")
        model = Tournament


tournament_schema = TournamentSchema()
tournament_schemas = TournamentSchema(many=True)


class OpponentSchema(Schema):
    class Meta:
        fields = ("nickname")
        model = Opponent


opponent_schema = OpponentSchema()
opponent_schemas = OpponentSchema(many=True)


class PlayerSchema(Schema):
    class Meta:
        fields = ("nickname")
        model = Player


player_schema = PlayerSchema()
player_schemas = PlayerSchema(many=True)


class GameSchema(Schema):
    class Meta:
        fields = ("tournament", "opponent", "chalice_score", "opponent_score")
        model = Game


game_schema = GameSchema()
game_schemas = GameSchema(many=True)


class PointSchema(Schema):
    class Meta:
        fields = ("id", "game", "player1", "player2", "player3",
                  "player4", "player5", "player6", "player7", "chalice_score",
                  "opponent_score", "youtube_start", "youtube_end")
        model = Point


point_schema = PointSchema()
point_schemas = PointSchema(many=True)
