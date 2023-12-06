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
        self.close_button = CloseButton.CloseButton(win, Constants.BLACK, x + width - 35, y + 12, 15, 20, 20, "X")
        self.close = False
        self.active = True
        
    # draw the settings pop up window
    def draw(self):
        if self.close == False:
            # draw the window
            pygame.draw.rect(self.win, Constants.WHITE, (self.x, self.y, self.width, self.height), 0)
            pygame.draw.rect(self.win, Constants.BLACK, (self.x, self.y, self.width, self.height), 4)

            # draw the pop up settings window's title
            title_font = pygame.font.Font("retro_computer_personal_use.ttf", 30)
            title_text = title_font.render(self.title, True, Constants.DARKGREEN)
            title = title_text.get_rect(center=(self.x + self.width // 2, self.y + 60))
            self.win.blit(title_text, title)

            # highlight the close button when the cursor is hovering over it
            if self.close_button.isOver():
                pygame.draw.rect(self.win, Constants.LIGHTGREEN, (1120 // 3 + 110 + 250 - 44, 1008 // 3 + 5, 40, 45), 0)
            # draw the close button
            self.close_button.draw()

