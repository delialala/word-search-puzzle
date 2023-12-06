import pygame
from pygame.locals import *
import Button
import Constants
import SettingsPopUp
import tkinter as tk
from tkinter import ttk

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
        self.settings_popup = SettingsPopUp.SettingsPopUp(self.win)

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

    # click on settings -> pop up settings window appears
    def click_settings_button(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isOver() and self.settings_popup.pop_up_shown == False:
                # the settings button has been clicked
                self.clicked_settings = True
                # creates the pop up window
                self.settings_popup.show_settings_popup()