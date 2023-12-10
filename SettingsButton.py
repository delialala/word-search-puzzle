import pygame
from pygame.locals import *
import Button
import Constants
import ThemesListPopUp
# the settings button for the main game page
class SettingsButton(Button.Button):
    def __init__(self, win, xStart, yStart, fontSize, textCell=''):
        super().__init__(Constants.WHITE, xStart, yStart, fontSize, 70, 70, textCell)
        self.win = win
        self.fontSize = 20
        self.xStart = 70
        self.yStart = 800

        self.clicked_settings = False

        # an instance of the pop up window
        self.settings_popup = ThemesListPopUp.ThemesListPopUp(self.win, 170, 300, 800, 500, "THEMES")
        self.settings_popup.active = False

        # the gear image on the button
        self.button_image = pygame.image.load("gear_retro.png")
        self.button_image = pygame.transform.scale(self.button_image, (120,70))

    # draws the settings button
    def draw(self):
        # draws a highlight when hovering over the button
        if self.isOver():
            pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 45, self.yStart - 15, 110, 110), 0)

        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart - 35, self.yStart - 5, 90, 90), 0)
        pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 20, self.yStart, 70, 70), 0)

        # draws the gear image
        self.win.blit(self.button_image, (self.xStart - 45, self.yStart))

        if self.clicked_settings:
            self.settings_popup.draw()

    # click on settings -> pop up settings window appears
    def click_settings_button(self, event, matrix_instance):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isOver() and self.settings_popup.active == False:
                # the settings button has been clicked
                self.clicked_settings = True
                # the settings window will pop up on the screen
                self.settings_popup.active = True
                # the matrix will not be functional as long as the pop up window is on the screen
                matrix_instance.matrix_enabled = False

    # click on "X" -> the pop up window closes
    def click_close_button(self, event, matrix_instance):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.clicked_settings and self.settings_popup.close_button.isOver():
                self.clicked_settings = False
                # the pop up window disappears
                self.settings_popup.active = False
                # the matrix will be functional again
                matrix_instance.matrix_enabled = True