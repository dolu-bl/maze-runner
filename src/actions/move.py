# -*- coding: utf-8 -*-

import pygame
from src.actions.action import Action
from src.common import Direction



class Move(Action):
    def __init__(self, board):
        super().__init__(board)
        self.direction = None

    def process(self):
        x = self.board.playerPosition[0]
        y = self.board.playerPosition[1]
        if self.direction == Direction.Up:
            self.tryMove(x, y - 1)
        elif self.direction == Direction.Right:
            self.tryMove(x + 1, y)
        elif self.direction == Direction.Down:
            self.tryMove(x, y + 1)
        elif self.direction == Direction.Left:
            self.tryMove(x - 1, y)

    def handle(self, event):
        if event.type != pygame.KEYUP:
            return False

        self.direction = None
        if event.key == pygame.K_UP:
            self.direction = Direction.Up
        elif event.key == pygame.K_RIGHT:
            self.direction = Direction.Right
        elif event.key == pygame.K_DOWN:
            self.direction = Direction.Down
        elif event.key == pygame.K_LEFT:
            self.direction = Direction.Left
        return self.direction != None

    def tryMove(self, x, y):
        if x < 0 : x = self.board.width - 1;
        if y < 0 : y = self.board.height - 1;
        if x >= self.board.width : x = 0
        if y >= self.board.height : y = 0

        self.board.playerPosition = (x, y)
