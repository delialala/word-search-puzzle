import pygame
from pygame.locals import *
import Constants
import SettingsPopUp
import StartscreenButton
import ThingieChooser
import UhohPopUp

class GameSettingsPopUp(SettingsPopUp.SettingsPopUp):
    def __init__(self, win, x, y, width, height, title):
        super().__init__(win, x, y, width, height, title)
        self.startButton = StartscreenButton.StartscreenButton(420, 700, "START")
        self.matrixSizeList = (5, 6, 7, 8, 9)
        self.matrixSizeChooser = ThingieChooser.ThingieChooser(win, self.matrixSizeList, 600, 390)
        self.matrix_size = 1

        self.domainList = ("YUMYUM", "LALA", "PEWPEW", "HOWDY", "SHREK", "RANDOM")
        self.domainChooser = ThingieChooser.ThingieChooser(win, self.domainList, 600, 480)
        self.domain = []

        # the player can choose if they want to play with a timer or not
        self.timerList = ("N/A", 10, 30, 45, 60, 75, 90, 120, 180)
        self.timerChooser = ThingieChooser.ThingieChooser(win, self.timerList, 600, 570)
        self.timer = 50
        self.timer_left = 0
        self.timer_running = False

    def draw(self):
        super().draw()
        self.startButton.draw(self.win)

        font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 30)
        matrixSizeText = font.render("Matrix size:", True, Constants.DARKGREEN)
        self.win.blit(matrixSizeText, (210, 395, 200, 200))
        self.matrixSizeChooser.draw()

        domainSizeText = font.render("Domain:", True, Constants.DARKGREEN)
        self.win.blit(domainSizeText, (210, 485, 200, 200))
        self.domainChooser.draw()

        timerSizeText = font.render("Timer:", True, Constants.DARKGREEN)
        self.win.blit(timerSizeText, (210, 575, 200, 200))
        self.timerChooser.draw()

    # draw the time left fort the player on the main game page
    def draw_timer(self):
        if self.timer != 'N/A':
            pygame.draw.rect(self.win, Constants.DARKGREEN,(35, 185, 275, 45), 0)
            pygame.draw.rect(self.win, Constants.WHITE,(43, 188, 265, 35), 0)
            time_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 25)
            time = int(self.timer_left / 1000)
            time_text = str(time)
            time_rendered = time_font.render("TIME LEFT: " + time_text, True, Constants.BLACK)
            self.win.blit(time_rendered, (45, 188))
    
    def event(self, event, all_words):
        # if you take this out, there will be a click executed the first
        # time you open the game settings window
        # i dont know why, but this seems to work, so...
        if Constants.CNT2 > 0:
            self.matrixSizeChooser.event(event)
            self.domainChooser.event(event)
            self.timerChooser.event(event)
            if self.timer != 'N/A':
                self.timer_left = self.timer * 1000

            # the timer will start as soon as the player enters the main game page
            if event.type == pygame.MOUSEBUTTONDOWN and self.startButton.isOver():
                self.timer_running = True

            self.matrix_size = self.matrixSizeChooser.list[self.matrixSizeChooser.crt]
            self.domain = self.domainChooser.list[self.domainChooser.crt]
            self.timer = self.timerChooser.list[self.timerChooser.crt]

            if self.timer != 'N/A':
                self.countdown_timer_event()

        Constants.CNT2 = Constants.CNT2 + 1

    # time count down
    def countdown_timer_event(self):
        if self.timer_running and self.timer != 'N/A':
            if self.timer_left > 0: 
                self.timer_left -= 1000
