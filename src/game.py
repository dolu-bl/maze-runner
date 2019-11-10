# -*- coding: utf-8 -*-

import pygame
from src.board import Board
from src.common import getSetting
from src.actions.move import Move



class Game():
    def __init__(self, settings):
        self.isRunning = True
        self.fps = getSetting(settings, "fps", 30)
        self.speed = getSetting(settings, "speed", 1)
        self.board = Board(settings)

        width = self.board.width * self.board.cellSize
        height = self.board.height * self.board.cellSize

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.actions = []
        self.actions.append(Move(self.board))

    def run(self):
        action = None
        while self.isRunning:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT : self.isRunning = False
                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_ESCAPE : self.isRunning = False

                for action in self.actions:
                    if action.handle(event) : action.process()

            self.board.process()
            self.board.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
