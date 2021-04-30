from peewee import *

db = SqliteDatabase('magic.db')

class Player(Model):
    username = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Game(Model):
    player1 = ForeignKeyField(Player, backref="player1")
    player2 = ForeignKeyField(Player, backref="player2")
    finished = BooleanField(default=False)

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Player, Game])


if __name__ == "__main__":
    initialize_db()
