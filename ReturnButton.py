import pygame
from pygame.locals import *
import Button
import Constants

# the settings button for the main game page
class ReturnButton(Button.Button):
    def __init__(self, win, xStart, yStart):
        super().__init__(Constants.WHITE, xStart, yStart, 10, 70, 70, '')
        self.win = win
        self.fontSize = 20
        self.xStart = 70
        self.yStart = 800
        self.is_enabled = True
        self.clicked = False

        self.button_image = Constants.arrow

    # draws the settings button
    def draw(self):
        # draws a highlight when hovering over the button
        if self.isOver() and self.is_enabled:
            pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 45, self.yStart - 15, 140, 140), 0)

        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart - 35, self.yStart - 5, 120, 120), 0)
        pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 20, self.yStart, 100, 90), 0)

        # draws the arrow image
        self.win.blit(self.button_image, (self.xStart-7, self.yStart + 10))
    
    def event(self, event, intro):
       if event.type == pygame.MOUSEBUTTONDOWN and self.is_enabled:
            if self.isOver():
                self.clicked = True

