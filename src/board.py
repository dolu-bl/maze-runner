# -*- coding: utf-8 -*-

from src.common import getSetting, Direction, ItemType, drawItem, drawPlayerItem
from src.level01 import Level01

class Board():
    def __init__(self, settings):
        self.level = Level01()
        self.boardWidth = self.level.width()
        self.boardHeight = self.level.height()
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.isDead = False
        self.playerPosition = self.startPosition()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for row in range(0, self.boardWidth):
            for column in range(0, self.boardHeight):
                x = row * self.cellSize
                y = column * self.cellSize
                item = ItemType(self.level.data[column][row])
                drawItem(item, screen, x, y, self.cellSize)
        x = self.playerPosition[0] * self.cellSize
        y = self.playerPosition[1] * self.cellSize
        drawPlayerItem(screen, x, y, self.cellSize)

    def process(self, moveDirection):
        self.move(moveDirection)

    def move(self, direction):
        x = self.playerPosition[0]
        y = self.playerPosition[1]
        if direction == Direction.Up:
            self.tryMove(x, y - 1)
        elif direction == Direction.Right:
            self.tryMove(x + 1, y)
        elif direction == Direction.Down:
            self.tryMove(x, y + 1)
        elif direction == Direction.Left:
            self.tryMove(x - 1, y)

    def tryMove(self, x, y):
        if x < 0 : x = self.boardWidth - 1;
        if y < 0 : y = self.boardHeight - 1;
        if x >= self.boardWidth : x = 0
        if y >= self.boardHeight : y = 0

        self.playerPosition = (x, y)

    def startPosition(self):
        for row in range(0, self.boardWidth):
            for column in range(0, self.boardHeight):
                item = self.level.data[column][row]
                if ItemType.PlayerStart == ItemType(item):
                    return (row, column)
        return (0, 0)
