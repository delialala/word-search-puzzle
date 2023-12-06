import pygame
from pygame.locals import *
import Constants
import Button
import SettingsPopUp

class Intro:
    def __init__(self, win):
        self.win = win
        self.in_intro_page = True
        self.width = 1120
        self.height = 1008
        self.clickedStart = False
        self.clickedSettings = False

        # title and font set up
        self.title_font = pygame.font.Font("retro_computer_personal_use.ttf", 45)
        self.title = self.title_font.render("Word Spy", True, Constants.BLACK)

        # instances for the start and settings buttons
        self.start_button = Button.Button(Constants.BLACK, self.width // 2 - 200 // 2 + 30, 400, 30, 200, 50, "START")
        self.settings_button = Button.Button(Constants.BLACK, self.width // 2 - 110, 500, 30, 200, 50, "SETTINGS")

        # an instance for the pop up window
        self.settings_popup = SettingsPopUp.SettingsPopUp(self.win, self.width // 3 + 10, self.height // 3, 350, 550, "SETTINGS")
        self.settings_popup.active = False


    def draw(self):
        self.win.fill(Constants.LIGHTGREEN)

        # draw game title
        title = self.title.get_rect(center=(self.width // 2, self.height // 4))
        self.win.blit(self.title, title)

        # draw highlight on buttons when the mouse hovers over them
        if self.start_button.isOver()==True:
            pygame.draw.rect(self.win, Constants.WHITE, (self.width // 2 - 200 // 2 + 18, 400 - 10, 150 + 14, 50 + 20), 0)

        if self.settings_button.isOver()==True:
            pygame.draw.rect(self.win, Constants.WHITE, (self.width // 2 - 110 - 12, 500 - 12, 200 + 24 + 15, 50 + 24), 0)

        # change the highligh color when the buttons are clicked
        if self.clickedStart == True:
            pygame.draw.rect(self.win, Constants.BLACK, (self.width // 2 - 200 // 2 + 18, 400 - 10, 150 + 14, 50 + 20), 0)

        if self.clickedSettings == True:
            pygame.draw.rect(self.win, Constants.BLACK, (self.width // 2 - 110 - 12, 500 - 12, 200 + 24 + 15, 50 + 24), 0)

        # draw the buttons
        self.start_button.draw(self.win, Constants.DARKGREEN)
        self.settings_button.draw(self.win, Constants.DARKGREEN)

        # draw the pop up window after user clicks on settings button
        if self.clickedSettings == True:
            self.settings_popup.draw()

    # click start -> get to game window
    def click_start(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.start_button.isOver() and self.settings_popup.active == False:
                self.clickedStart = True
                self.draw()
                pygame.display.flip()
                self.in_intro_page = False

    # click on settings -> pop up settings window appears
    def click_settings(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.settings_button.isOver():
                self.clickedSettings = True
                # pop up appears on screen
                self.settings_popup.active = True
                self.draw()
                pygame.display.flip()

    # click on "X" -> the pop up window closes
    def click_close(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.clickedSettings and self.settings_popup.close_button.isOver():
                self.clickedSettings = False
                # pop up disappears
                self.settings_popup.active = False
                self.draw()
                pygame.display.flip()