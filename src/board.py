# -*- coding: utf-8 -*-

from src.common import getSetting, Direction, ItemType, drawItem, drawPlayerItem
from src.level01 import Level01



class Board():
    def __init__(self, settings):
        self.level = Level01()
        self.width = self.level.width()
        self.height = self.level.height()
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.isDead = False
        self.playerPosition = self.startPosition()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for row in range(0, self.width):
            for column in range(0, self.height):
                x = row * self.cellSize
                y = column * self.cellSize
                item = ItemType(self.level.data[column][row])
                drawItem(item, screen, x, y, self.cellSize)
        x = self.playerPosition[0] * self.cellSize
        y = self.playerPosition[1] * self.cellSize
        drawPlayerItem(screen, x, y, self.cellSize)

    def process(self):
        pass

    def startPosition(self):
        for row in range(0, self.width):
            for column in range(0, self.height):
                item = self.level.data[column][row]
                if ItemType.PlayerStart == ItemType(item):
                    return (row, column)
        return (0, 0)
