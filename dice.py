import random

from .utils import read_config


def roll_element():
    element_choices = read_config()["dice_faces"]["elements"]
    return random.choice(element_choices)

def roll_symbol():
    return "symbol"
