# -*- coding: utf-8 -*-

from src.player import Player
from src.common import getSetting, ItemType, drawItem



class Board():
    def __init__(self, settings, width, height):
        self.cellSize = getSetting(settings, "cellSize", 10)
        self.level = None
        self.centerX = int(width / 2 - self.cellSize / 2)
        self.centerY = int(height / 2 - self.cellSize / 2)
        self.offsetX = 0
        self.offsetY = 0
        self.player = Player()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for row in range(0, self.width):
            for col in range(0, self.height):
                x = row * self.cellSize + self.offsetX
                y = col * self.cellSize + self.offsetY
                item = ItemType(self.level.data[col][row])
                drawItem(item, screen, x, y, self.cellSize)
        self.player.draw(screen, self.centerX, self.centerY, self.cellSize)

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
        startPosition = self.startPosition()
        self.setPlayerPosition(startPosition[0], startPosition[1])

    def setPlayerPosition(self, col, row):
        self.offsetX = self.centerX - col * self.cellSize
        self.offsetY = self.centerY - row * self.cellSize
        self.player.col = col
        self.player.row = row
