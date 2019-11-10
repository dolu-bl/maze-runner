# -*- coding: utf-8 -*-

import pygame
from src.board import Board
from src.common import getSetting
from src.actions.move import Move
from src.actions.quit import Quit
from src.levels.level01 import Level01
from src.levels.level02 import Level02



class Game():
    def __init__(self, settings):
        self.isRunning = True
        self.fps = getSetting(settings, "fps", 30)
        self.board = Board(settings)
        self.loadNextLevel()

        width = self.board.width * self.board.cellSize
        height = self.board.height * self.board.cellSize

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.actions = []
        self.actions.append(Move(self))
        self.actions.append(Quit(self))

    def run(self):
        action = None
        while self.isRunning:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                for action in self.actions:
                    if action.handle(event) : action.process()

            self.board.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

    def loadNextLevel(self):
        if None == self.board.level : self.board.loadLevel(Level01())
        elif 0 == self.board.level.order : self.board.loadLevel(Level02())
        else : self.isRunning = False
