import pygame
from pygame.locals import *
import Constants
import ThemesListPopUp
import StartscreenButton
import GameSettingsPopUp
class Intro:

    def __init__(self, win):
        self.win = win
        self.in_intro_page = True
        self.width = 1120
        self.height = 1008
        self.clickedStart = False
        self.clickedThemes = False
        # instances for the start and themes buttons
        self.start_button = StartscreenButton.StartscreenButton(570, 550, "START")
        self.themes_button = StartscreenButton.StartscreenButton(570, 650, "THEMES")

        # an instance for the pop up window for the themes
        self.themes_popup = ThemesListPopUp.ThemesListPopUp(self.win, 170, 300, 800, 500, "THEMES")
        self.themes_popup.active = False

        # an instance for the pop up window for the game settings
        self.settings_popup = GameSettingsPopUp.GameSettingsPopUp(self.win, 170, 300, 800, 500, "SETTINGS")
        self.settings_popup.active = False

        # load the image for the titlescreen
        self.titleScreenImage = Constants.titleScreenImage

        # load the image for the title
        self.titleImage = Constants.titleImage


    def draw(self):
        self.win.fill(Constants.LIGHTGREEN)

        self.win.blit(self.titleScreenImage, (0, 0))
        # draw game title
        self.win.blit(self.titleImage, (380, 380))
        # draw the buttons

        self.start_button.draw(self.win)
        self.themes_button.draw(self.win)

        # draw the pop up window after user clicks on settings button
        if self.clickedThemes == True:
            self.themes_popup.draw()
        if self.clickedStart == True:
            self.settings_popup.draw()

    # click start -> get to game window
    def click_start(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.start_button.isOver() and self.themes_popup.active == False and self.settings_popup.active == False:
                print("hello")
                self.clickedStart = True
                self.settings_popup.active = True
                self.draw()
                pygame.display.flip()
                #self.in_intro_page = False

    # click on settings -> pop up settings window appears
    def click_settings(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.themes_button.isOver():
                self.clickedThemes = True
                # pop up appears on screen
                self.themes_popup.active = True
                self.draw()
                pygame.display.flip()

    # click on "X" -> the pop up window closes
    def click_close(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if (self.clickedThemes or self.clickedStart) and self.themes_popup.close_button.isOver():
                Constants.CNT = 0
                self.clickedStart = False
                self.clickedThemes = False
                # pop up disappears
                self.themes_popup.active = False
                self.settings_popup.active = False
                self.draw()
                pygame.display.flip()

    # click on the start in the settings button
    def click_start_in_settings(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.settings_popup.active and self.settings_popup.startButton.isOver():
                self.settings_popup.active = False
                self.in_intro_page = False
                self.clickedStart = False

    # events when themes is clicked
    def clickTheme(self, event):
        if self.in_intro_page and self.clickedThemes and self.themes_popup.active:
            self.themes_popup.eventTheme(event)
            pygame.display.flip()

    # events when start is clicked
    def clickGameSettings(self, event):
        if self.in_intro_page and self.clickedStart and self.settings_popup.active:
            self.settings_popup.event(event)
            pygame.display.flip()