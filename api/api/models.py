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


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    nickname = db.Column(db.String(30))
    gender_matching = db.Column(db.String(20))

    def __repr__(self):
        return '<Player %s>' % self.nickname


class Point(db.Model):
    __tablename__ = 'point'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    game = db.relationship("Game", backref=db.backref('game', uselist=False))
    player1_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player2_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player3_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player4_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player5_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player6_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player7_id = db.Column(db.Integer, db.ForeignKey('player.id'))

    player1 = db.relationship("Player", foreign_keys=[player1_id])
    player2 = db.relationship("Player", foreign_keys=[player2_id])
    player3 = db.relationship("Player", foreign_keys=[player3_id])
    player4 = db.relationship("Player", foreign_keys=[player4_id])
    player5 = db.relationship("Player", foreign_keys=[player5_id])
    player6 = db.relationship("Player", foreign_keys=[player6_id])
    player7 = db.relationship("Player", foreign_keys=[player7_id])

    chalice_score = db.Column(db.Integer)
    opponent_score = db.Column(db.Integer)
    youtube_start = db.Column(db.Integer)
    youtube_end = db.Column(db.Integer)
