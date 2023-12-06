import pygame
from pygame.locals import *
import Button
import Constants

# a class for the "X" button of the pop up window
class CloseButton(Button.Button):
    def __init__(self, win, color, x, y, fontSize, width, height, name="X"):
        self.win = win
        self.color = color
        self.x = x
        self.y = y
        self.fontSize = fontSize
        self.width = width
        self.height = height
        self.name = name
        self.close_button = Button.Button(color, x, y, fontSize, width, height, name)

    def draw(self):
        self.close_button.draw(self.win, Constants.DARKGREEN)