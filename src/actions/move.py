# -*- coding: utf-8 -*-

import pygame
from src.actions.action import Action
from src.common import Direction, ItemType



class Move(Action):
    def __init__(self, game):
        super().__init__(game)
        self.direction = None
        surface = pygame.display.get_surface()
        self.windowWidth = surface.get_width()
        self.windowHeight = surface.get_height()

    def process(self):
        col = self.board.player.col
        row = self.board.player.row
        if self.direction == Direction.Up:
            self.tryMove(col, row - 1)
        elif self.direction == Direction.Right:
            self.tryMove(col + 1, row)
        elif self.direction == Direction.Down:
            self.tryMove(col, row + 1)
        elif self.direction == Direction.Left:
            self.tryMove(col - 1, row)

    def handle(self, event):
        if event.type == pygame.KEYUP:
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.direction = None
            x = event.pos[0] - self.windowWidth / 2
            y = event.pos[1] - self.windowHeight / 2
            if x > y:
                if x > -y:
                    self.direction = Direction.Right
                else:
                    self.direction = Direction.Up
            else:
                if x > -y:
                    self.direction = Direction.Down
                else:
                    self.direction = Direction.Left
            return self.direction != None

        return False

    def tryMove(self, col, row):
        if col < 0 : col = self.board.width - 1;
        if row < 0 : row = self.board.height - 1;
        if col >= self.board.width : col = 0
        if row >= self.board.height : row = 0

        itemType = self.board.itemType(col, row)
        if ItemType.Wall == itemType:
            return

        if ItemType.Exit == itemType:
            self.game.loadNextLevel()
            return

        self.board.setPlayerPosition(col, row)
        self.board.process()
