from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Game(db.Model):

    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    tournament = db.relationship(
        "Tournament", backref=db.backref("tournament", uselist=False))
    opponent_id = db.Column(db.Integer, db.ForeignKey('opponent.id'))
    opponent = db.relationship(
        "Opponent", backref=db.backref("opponent", uselist=False))
    youtube_url = db.Column(db.String(60))

    chalice_score = db.Column(db.Integer)
    opponent_score = db.Column(db.Integer)


class Tournament(db.Model):
    __tablename__ = 'tournament'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    nickname = db.Column(db.String(25))
    location = db.Column(db.String(50))

    def __repr__(self):
        return '<Tournament %s>' % self.nickname


class Opponent(db.Model):
    __tablename__ = 'opponent'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(40))
    nickname = db.Column(db.String(40))


player_points = db.Table('player_points',
                         db.Column('player_id', db.Integer,
                                   db.ForeignKey('player.id')),
                         db.Column('point_id', db.Integer,
                                   db.ForeignKey('point.id'))
                         )


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    nickname = db.Column(db.String(30))
    gender_matching = db.Column(db.String(20))
    points = db.relationship("Point", secondary=player_points)

    def __repr__(self):
        return '<Player %s>' % self.nickname


class Point(db.Model):
    __tablename__ = 'point'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    game = db.relationship("Game", backref=db.backref('game', uselist=False))
    players = db.relationship("Player", secondary=player_points)

    chalice_score = db.Column(db.Integer)
    opponent_score = db.Column(db.Integer)
    youtube_start = db.Column(db.Integer)
    youtube_end = db.Column(db.Integer)

    def __repr__(self):
        return '<Point %s %d-%d %s>' % (self.game.tournament.nickname,
                                        self.chalice_score,
                                        self.opponent_score,
                                        self.game.opponent.nickname)
