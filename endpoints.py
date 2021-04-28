from flask import Flask, abort

# import dice
from .dice import roll_element, roll_rune


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

    @app.errorhandler(422)
    def bad_argument(error):
        return f"Error 422", error
    
    return app

app = create_app()
