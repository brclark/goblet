from flask_marshmallow import Marshmallow
from .models import Tournament, Opponent, Player, Game, Point


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


ma = Marshmallow()


class TournamentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "nickname", "location")
        model = Tournament


tournament_schema = TournamentSchema()
tournament_schemas = TournamentSchema(many=True)


class OpponentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "nickname")
        model = Opponent


opponent_schema = OpponentSchema()
opponent_schemas = OpponentSchema(many=True)


class PlayerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "nickname")
        model = Player


player_schema = PlayerSchema()
player_schemas = PlayerSchema(many=True)


class GameSchema(ma.Schema):
    class Meta:
        fields = ("tournament", "opponent", "chalice_score", "opponent_score")
        model = Game


game_schema = GameSchema()
game_schemas = GameSchema(many=True)


class PointSchema(ma.Schema):
    player1 = ma.Nested(PlayerSchema)
    player2 = ma.Nested(PlayerSchema)
    player3 = ma.Nested(PlayerSchema)
    player4 = ma.Nested(PlayerSchema)
    player5 = ma.Nested(PlayerSchema)
    player6 = ma.Nested(PlayerSchema)
    player7 = ma.Nested(PlayerSchema)

    class Meta:
        fields = ("id", "chalice_score",
                  "opponent_score", "youtube_start", "youtube_end",
                  "player1", "player2", "player3", "player4", "player5",
                  "player6", "player7")
        model = Point
        ordered = True


point_schema = PointSchema()
point_schemas = PointSchema(many=True)
