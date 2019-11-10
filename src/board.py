# -*- coding: utf-8 -*-

from src.common import getSetting, ItemType, drawItem, drawPlayerItem



class Board():
    def __init__(self, settings):
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.isDead = False
        self.level = None

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

    def itemType(self, row, column):
        return ItemType(self.level.data[column][row])

    def loadLevel(self, level):
        self.level = level
        self.width = self.level.width()
        self.height = self.level.height()
        self.playerPosition = self.startPosition()
