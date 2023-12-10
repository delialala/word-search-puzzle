import pygame
from pygame.locals import *
import Button
import Constants

# a class for the "X" button of the pop up window
class CloseButton(Button.Button):
    def __init__(self, x, y, fontSize, width, height, name="X"):
        super().__init__(Constants.LIGHTGREEN, x, y, fontSize, width + 40, height + 40, name)
        self.textPosition = y

    def draw(self, win):

        font = pygame.font.Font('resources/retro_computer_personal_use.ttf', size = self.fontSize)
        text = font.render(self.text, 1, Constants.DARKGREEN)

        if self.isOver() == True:
            pygame.draw.rect(win, Constants.WHITE, (self.x, self.y, self.width, self.height), 0)
            
        else:
            pygame.draw.rect(win, Constants.LIGHTGREEN, (self.x, self.y, self.width, self.height), 0)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
