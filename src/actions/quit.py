# -*- coding: utf-8 -*-

import pygame
from src.actions.action import Action



class Quit(Action):
    def process(self):
        self.game.isRunning = False

    def handle(self, event):
        if event.type == pygame.QUIT:
            return True

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return True

        return False
