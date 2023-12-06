import pygame
from pygame.locals import *
import Constants
import Button
import SettingsPopUp
import tkinter as tk
from tkinter import ttk

class Intro:
    def __init__(self, win):
        self.win = win
        self.in_intro_page = True
        self.width = 1120
        self.height = 1008
        self.clickedStart = False
        self.clickedSettings = False

        self.title_font = pygame.font.Font("retro_computer_personal_use.ttf", 45)
        self.title = self.title_font.render("Word Spy", True, Constants.BLACK)

        self.start_button = Button.Button(Constants.BLACK, self.width // 2 - 200 // 2 + 30, 400, 30, 200, 50, "START")
        self.settings_button = Button.Button(Constants.BLACK, self.width // 2 - 110, 500, 30, 200, 50, "SETTINGS")

        # an instance of the pop up window
        self.settings_popup = SettingsPopUp.SettingsPopUp(self.win)

    def draw(self):
        self.win.fill(Constants.LIGHTGREEN)

        # the game title
        title = self.title.get_rect(center=(self.width // 2, self.height // 4))
        self.win.blit(self.title, title)

        # creates a highligh when hovering over the buttons
        if self.start_button.isOver()==True:
            pygame.draw.rect(self.win, Constants.WHITE, (self.width // 2 - 200 // 2 + 18, 400 - 10, 150 + 14, 50 + 20), 0)

        if self.settings_button.isOver()==True:
            pygame.draw.rect(self.win, Constants.WHITE, (self.width // 2 - 110 - 12, 500 - 12, 200 + 24 + 15, 50 + 24), 0)

        # changes the highlight color when clicking the buttons
        if self.clickedStart == True:
            pygame.draw.rect(self.win, Constants.BLACK, (self.width // 2 - 200 // 2 + 18, 400 - 10, 150 + 14, 50 + 20), 0)

        if self.clickedSettings == True:
            pygame.draw.rect(self.win, Constants.BLACK, (self.width // 2 - 110 - 12, 500 - 12, 200 + 24 + 15, 50 + 24), 0)

        # draws the buttons
        self.start_button.draw(self.win, Constants.DARKGREEN)
        self.settings_button.draw(self.win, Constants.DARKGREEN)

    # will get the user to the game page
    def click_start(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.start_button.isOver():
                # the start button has been clicked
                self.clickedStart = True
                #draws the highlights
                self.draw()
                pygame.display.flip()
                # signals we are no longer in the intro page
                self.in_intro_page = False

    # click on settings -> pop up settings window appears
    def click_settings(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.in_intro_page:
            if self.settings_button.isOver() and self.settings_popup.pop_up_shown == False:
                # the settings button has been clicked
                self.clickedSettings = True
                # creates the pop up window
                self.settings_popup.show_settings_popup()
                # draws the highlights
                self.draw()
                pygame.display.flip()
