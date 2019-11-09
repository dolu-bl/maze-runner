# -*- coding: utf-8 -*-
from src.game import Game

def main():
    game = Game({ "cellSize" : 30
                , "speed" : 2
                })
    game.run()

if __name__ == "__main__":
    main()
