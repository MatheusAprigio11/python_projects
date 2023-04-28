import defs
from objects import *
from classes import *

def main():
    mode = defs.game_mode()

    if mode == "Singers":
        defs.play_singer(select_singer)

    elif mode == "Fruits":
        defs.play_fruits(select_fruit)

if __name__ == '__main__':
    main()

    