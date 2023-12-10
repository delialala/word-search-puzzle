import pygame
from pygame.locals import *
import Constants
import Button
import CloseButton

# the pop up window for the settings
class SettingsPopUp(Button.Button):
    def __init__(self, win, x, y, width, height, title):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.xCloseButton = x + width - 70
        self.yCloseButton = y + 40
        self.close_button = CloseButton.CloseButton(self.xCloseButton, self.yCloseButton - 30, 30, 10, 10)
        self.close = False
        self.active = True
        
    # draw the settings pop up window
    def draw(self):
        if self.close == False:
            # draw the window
            pygame.draw.rect(self.win, Constants.WHITE, (self.x-16, self.y-16, self.width+32, self.height+32), 0)
            pygame.draw.rect(self.win, Constants.DARKGREEN, (self.x-8, self.y-8, self.width+16, self.height+16), 0)
            pygame.draw.rect(self.win, Constants.LIGHTGREEN, (self.x, self.y, self.width, self.height), 0)

            # draw the pop up settings window's title
            title_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 30)
            title_text = title_font.render(self.title, True, Constants.DARKGREEN)
            title = title_text.get_rect(center=(self.x + 120, self.yCloseButton))
            self.win.blit(title_text, title)
            pygame.draw.rect(self.win, Constants.DARKGREEN, (self.x + 35, self.yCloseButton + 27, self.width - 50, 6), 0)
            # draw the close button
            self.close_button.draw(self.win)

