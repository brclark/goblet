from flask_marshmallow import Marshmallow
from .models import Tournament, Opponent, Player, Game, Point


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
        fields = ("id", "tournament", "opponent",
                  "chalice_score", "opponent_score", "youtube_url")
        model = Game
        ordered = True

    tournament = ma.Nested(TournamentSchema(only=("id", "nickname")))
    opponent = ma.Nested(OpponentSchema(only=("id", "nickname")))


game_schema = GameSchema()
game_schemas = GameSchema(many=True)


class PointSchema(ma.Schema):
    class Meta:
        fields = ("id", "chalice_score",
                  "opponent_score", "youtube_start", "youtube_end", "game",
                  "players")
        model = Point
        ordered = True

    game = ma.Nested(GameSchema(only=("id", "youtube_url")))
    players = ma.Nested(PlayerSchema, many=True)


point_schema = PointSchema()
point_schemas = PointSchema(many=True)


class PlayerPointSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "nickname", "points")

    points = ma.Nested(PointSchema(only=("id", "chalice_score",
                                         "opponent_score", "youtube_start",
                                         "youtube_end", "game")), many=True)


player_point_schema = PlayerPointSchema()
