# -*- coding: utf-8 -*-

class Action():
    def __init__(self, board):
        self.board = board

    def process(self):
        pass

    def handle(self, event):
        return False
