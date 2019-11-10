# -*- coding: utf-8 -*-

import pygame
from src.common import Direction, Colors



class Player():
    def __init__(self):
        self.isDead = False
        self.col = 0
        self.row = 0
        self.direction = Direction.Down

    def draw(self, screen, x, y, cellSize):
        cellSize2 = int(cellSize / 2)
        pygame.draw.circle(
            screen,
            Colors.Player.value,
            (x + cellSize2, y + cellSize2),
            cellSize2)
