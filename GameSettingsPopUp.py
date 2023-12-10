import pygame
from pygame.locals import *
import Constants
import SettingsPopUp
import StartscreenButton
import ThingieChooser
class GameSettingsPopUp(SettingsPopUp.SettingsPopUp):
    def __init__(self, win, x, y, width, height, title):
        super().__init__(win, x, y, width, height, title)
        self.startButton = StartscreenButton.StartscreenButton(420, 700, "START")
        self.matrixSizeList = (4, 5, 6, 7)
        self.matrixSizeChooser = ThingieChooser.ThingieChooser(win, self.matrixSizeList, 600, 390)

    def draw(self):
        super().draw()
        self.startButton.draw(self.win)

        font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 30)
        matrixSizeText = font.render("Matrix size:", True, Constants.DARKGREEN)
        self.win.blit(matrixSizeText, (210, 390, 200, 200))
        self.matrixSizeChooser.draw()
    
    def event(self, event):
        # if you take this out, there will be a click executed the first
        # time you open the game settings window
        # i dont know why, but this seems to work, so...
        if Constants.CNT2 > 0:
            self.matrixSizeChooser.event(event)
        Constants.CNT2 = Constants.CNT2 + 1
        # TODO: update the matrix when a setting is changed




