from flask import Flask, abort

# import dice
from .dice import roll_element, roll_rune
from .model import Player, Game
# from peewee import model


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello world!"

    @app.route('/roll_dice/<kind>')
    def roll_dice(kind: str):
        if kind == "element":
            # return dice.roll_element()
            return roll_element()
        elif kind == "rune":
            return roll_rune()
        else:
            abort(422)


    @app.route("/new_game/<you>,<other>")
    def new_game(you, other):
        
        your_player, _ = Player.get_or_create(username=you)
        other_player, _ = Player.get_or_create(username=other)

        try:
            game = Game.get(Game.get(
                (Game.player1 == your_player and Game.player2 == other_player and not Game.finished) or
                (Game.player2 == your_player and Game.player1 == other_player and not Game.finished)
            ))
        except Game.DoesNotExist:
            game = Game(player1=your_player, player2=other_player)
            game.save()
        
        return {"game_id": game.id, "player1": game.player1.username, "player2": game.player2.username}

    @app.errorhandler(422)
    def bad_argument(error):
        return f"Error 422", error
    
    return app

app = create_app()
