import pygame
from pygame.locals import *
import Constants
import SettingsPopUp
import CloseButton
import MainScreenButton

# will pop up if the timer runs out and the player does not find all the words
class UhohPopUp():
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
        self.main_screen_button = MainScreenButton.MainScreenButton(self.x + 25,self. yCloseButton + 150, "WANNA PLAY AGAIN?")
        self.active = False
        
    # draw the Uhoh pop up window
    def draw(self):
        # draw the window
        pygame.draw.rect(self.win, Constants.WHITE, (self.x-16, self.y-16, self.width+32, self.height+32), 0)
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.x-8, self.y-8, self.width+16, self.height+16), 0)
        pygame.draw.rect(self.win, Constants.LIGHTGREEN, (self.x, self.y, self.width, self.height), 0)

        # draw the pop up Uhoh window's messages
        title_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 40)
        title_text = title_font.render(self.title, True, Constants.DARKGREEN)
        title = title_text.get_rect(center=(self.x + 250, self.yCloseButton + 30))
        self.win.blit(title_text, title)
        text1_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 30)
        text1_text = text1_font.render("DON'T BE SAD :(", True, Constants.DARKGREEN)
        text1 = text1_text.get_rect(center=(self.x + 250, self.yCloseButton + 80))
        self.win.blit(text1_text, text1)

        # draw the button that takes the player to the intro page
        self.main_screen_button.draw(self.win)
