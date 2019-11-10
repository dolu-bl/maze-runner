# -*- coding: utf-8 -*-

import pygame
from enum import Enum, auto

def getSetting(settings, value, defaultValue):
    if settings.__contains__(value):
        return settings[value]
    return defaultValue

class Direction(Enum):
    Up = auto()
    Right = auto()
    Down = auto()
    Left = auto()

class ItemType(Enum):
    Empty = 0
    Wall = 1
    PlayerStart = 2
    Enemy = 3
    Exit = 4
    Apple = 5

class Colors(Enum):
    EmptyBorder = (64, 64, 64)
    Wall = (128, 128, 128)
    PlayerStart = (32, 32, 64)
    Player = (64, 196, 64)
    Enemy = (128, 32, 32)
    Exit = (64, 128, 64)
    Apple = (196, 128, 128)

def drawItem(itemType, screen, x, y, cellSize):
    if ItemType.Empty == itemType : drawEmptyItem(screen, x, y, cellSize)
    elif ItemType.Wall == itemType : drawWallItem(screen, x, y, cellSize)
    elif ItemType.PlayerStart == itemType : drawPlayerStartItem(screen, x, y, cellSize)
    elif ItemType.Enemy == itemType : drawEnemyItem(screen, x, y, cellSize)
    elif ItemType.Exit == itemType : drawExitItem(screen, x, y, cellSize)
    elif ItemType.Apple == itemType : drawAppleItem(screen, x, y, cellSize)

def drawEmptyItem(screen, x, y, cellSize):
    pygame.draw.rect(
        screen,
        Colors.EmptyBorder.value,
        (x, y, cellSize, cellSize),
        1)

def drawWallItem(screen, x, y, cellSize):
    pygame.draw.rect(
        screen,
        Colors.Wall.value,
        (x, y, cellSize, cellSize))

def drawPlayerStartItem(screen, x, y, cellSize):
    pygame.draw.rect(
        screen,
        Colors.PlayerStart.value,
        (x, y, cellSize, cellSize))

def drawEnemyItem(screen, x, y, cellSize):
    cellSize2 = int(cellSize / 2)
    pygame.draw.polygon(
        screen,
        Colors.Enemy.value,
        ((x + cellSize2, y)
        ,(x + cellSize, y + cellSize2)
        ,(x + cellSize2, y + cellSize)
        ,(x, y + cellSize2))
        )

def drawExitItem(screen, x, y, cellSize):
    pygame.draw.rect(
        screen,
        Colors.Exit.value,
        (x, y, cellSize, cellSize))

def drawAppleItem(screen, x, y, cellSize):
    cellSize2 = int(cellSize / 2)
    pygame.draw.circle(
        screen,
        Colors.Apple.value,
        (x + cellSize2, y + cellSize2),
        cellSize2)
