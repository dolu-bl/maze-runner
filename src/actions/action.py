# -*- coding: utf-8 -*-

class Action():
    def __init__(self, game):
        self.game = game
        self.board = game.board

    def process(self):
        pass

    def handle(self, event):
        return False
