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

    def tryMove(self, x, y):
        if x < 0 : x = self.board.width - 1;
        if y < 0 : y = self.board.height - 1;
        if x >= self.board.width : x = 0
        if y >= self.board.height : y = 0

        itemType = self.board.itemType(x, y)
        if ItemType.Wall == itemType:
            return

        if ItemType.Exit == itemType:
            self.game.loadNextLevel()
            return

        self.board.setPlayerPosition((x, y))
        self.board.process()
