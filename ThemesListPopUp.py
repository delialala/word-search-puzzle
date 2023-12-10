import pygame
from pygame.locals import *
import Constants
import SettingsPopUp

class ThemesListPopUp(SettingsPopUp.SettingsPopUp):
    def __init__(self, win, x, y, width, height, title):
        super().__init__(win, x, y, width, height, title)
        self.xStartList = x + 20
        self.yStartList = y + 20
        self.gap = 50
        self.themesList = ["CLASSIC GREEN", "BLACK AND WHITE", "DELIAS CHOICE", "RUSTIC", "AQUA", "PUMPKIN LOVE", "NEERG CISSALC", "DIANAS CHOICE", "FOOTBALL", "PEACH PARTY", "GIRLYPOP", "SPOOKY SEASON", "CANDY ROCK", "BANANANANA"]
        self.win = win
        self.cellWidth = 0
        self.xStartList2 = x + 20 + self.cellWidth
        self.cellHeight = 0
        self.yList = []
        self.isFirstTime = True
        self.cellThatIsClicked = 0
        self.cnt = 0


    def draw(self):
        super().draw()
        start_y = self.yStartList + self.gap - 20
        xStartCurrent = self.xStartList
        yList = self.yList
        toSubtract = 0
        # puts the words in the list
        for i, theme in enumerate(self.themesList):
            
            if i>=7:
                xStartCurrent = self.xStartList + self.cellWidth + 80
                yList = self.yList
                toSubtract = 7
            list_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", size = 25)
            text_color = Constants.DARKGREEN
            text = list_font.render(theme, True, text_color)

            # for the first time drawing, find the width of the longest theme
            # and put the themes' starting y and i in an array

            if self.isFirstTime == True:
                if self.cellWidth < text.get_width():
                    self.cellWidth = text.get_width()
                self.yList.append(start_y + (i+1)*self.gap)
            # draw a white box if the mouse is hovering
            if i == self.whichIsOver() and self.isFirstTime == False:
                pygame.draw.rect(self.win, Constants.WHITE, (xStartCurrent - 10, start_y + (i + 1 - toSubtract) * self.gap - 10, self.cellWidth + 20, self.cellHeight + 20), 4)

            # change the color if it is clicked
            
            if self.cellThatIsClicked == i:
                text_color = Constants.WHITE
                pygame.draw.rect(self.win, Constants.DARKGREEN, (xStartCurrent - 10, start_y + (i + 1 - toSubtract) * self.gap - 10, self.cellWidth + 20, self.cellHeight + 20), 0)
                pygame.draw.rect(self.win, Constants.BLACK, (xStartCurrent-5, start_y + (i + 1 - toSubtract) * self.gap-5 , self.cellWidth + 10, self.cellHeight + 10), 0)
                text = list_font.render(theme, True, text_color)

            self.win.blit(text, (xStartCurrent, start_y + (i + 1 - toSubtract) * self.gap))
        
        if self.isFirstTime == True:
            self.cellHeight = text.get_height()
            self.isFirstTime = False


    def whichIsOver(self):
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.cellWidth and pos[1] < 750:
            for yStart in self.yList:
                if pos[1] > yStart and pos[1] < yStart + self.cellHeight:
                    return self.yList.index(yStart)
        if pos[0] > self.x + 70 + self.cellWidth and pos[0] < self.x + 70 + 2*self.cellWidth:
            for yStart in self.yList:
                if pos[1] > yStart and pos[1] < yStart + self.cellHeight:
                    return self.yList.index(yStart) + 7
        return -1
    
    def changeEverything(self, white, lightGray, darkGray, black):
        Constants.titleScreenImage = Constants.changeThemeImage(Constants.titleScreenImage, white, lightGray, darkGray, black)
        Constants.titleImage = Constants.changeThemeImage(Constants.titleImage,  white, lightGray, darkGray, black)
        Constants.arrow = Constants.changeThemeImage(Constants.arrow,  white, lightGray, darkGray, black)
        Constants.arrowHover = Constants.changeThemeImage(Constants.arrowHover,  white, lightGray, darkGray, black)
        Constants.arrowPressed = Constants.changeThemeImage(Constants.arrowPressed,  white, lightGray, darkGray, black)
        Constants.WHITE = white
        Constants.LIGHTGREEN = lightGray
        Constants.DARKGREEN = darkGray
        Constants.BLACK = black

    def changeTheme(self, i):
        if(self.themesList[i] == "DELIAS CHOICE"):
            self.changeEverything((246, 198, 168, 0), (209, 124, 124, 0), (45, 87, 123, 0), (28, 27, 36, 0))
        if(self.themesList[i] == "CLASSIC GREEN"):
            self.changeEverything((224 , 248, 208, 0), (136, 192, 112, 0), (52, 104, 86, 0), (8, 24, 23, 0))
        if(self.themesList[i] == "BLACK AND WHITE"):
            self.changeEverything((228, 228, 228, 0), (152, 152, 152, 0), (78, 78, 78, 0), (10, 10, 10, 0))
        if(self.themesList[i] == "RUSTIC"):
            self.changeEverything((237, 180, 161, 0), (169, 104, 104, 0), (118, 68, 98, 0), (44, 33, 55, 0))
        if(self.themesList[i] == "AQUA"):
            self.changeEverything((231, 247, 244, 0), (104, 186, 188, 0), (0, 95, 140, 0), (0, 43, 89, 0))
        if(self.themesList[i] == "PUMPKIN LOVE"):
            self.changeEverything((247, 219, 126, 0), (224, 110, 22, 0), (25, 105, 44, 0), (20, 43, 35, 0))
        if(self.themesList[i] == "NEERG CISSALC"):
            self.changeEverything((9, 25, 24, 0), (53, 105, 87, 0), (137, 193, 113, 0), (225 , 249, 209, 0))
        # TODO: choose your theme!
        if(self.themesList[i] == "DIANAS CHOICE"):
            self.changeEverything((224 , 248, 208, 0), (136, 192, 112, 0), (52, 104, 86, 0), (8, 24, 23, 0))
        if(self.themesList[i] == "FOOTBALL"):
            self.changeEverything((235, 238, 231, 0), (134, 135, 121, 0), (170, 33, 29, 0), (42, 32, 30, 0))
        if(self.themesList[i] == "PEACH PARTY"):
            self.changeEverything((255, 219, 203, 0), (214, 130, 128, 0), (71, 116, 0, 0), (34, 41, 3, 0))
        if(self.themesList[i] == "GIRLYPOP"):
            self.changeEverything((255, 255, 255, 0), (255, 143, 132, 0), (148, 58, 58, 0), (1, 1, 1, 0))
        if(self.themesList[i] == "SPOOKY SEASON"):
            self.changeEverything((248, 240, 136, 0), (248, 144, 32, 0), (96, 40, 120, 0), (48, 0, 48, 0))
        if(self.themesList[i] == "CANDY ROCK"):
            self.changeEverything((249, 220, 222, 0), (147, 138, 193, 0), (53, 98, 133, 0), (36, 45, 103, 0))
        if(self.themesList[i] == "BANANANANA"):
            self.changeEverything((207, 171, 81, 0), (157, 101, 76, 0), (77, 34, 44, 0), (33, 11, 27, 0))

    def eventTheme(self, event):
        # for each theme check if it is clicked and if the mouse is hovering over it
        for i, themes in enumerate(self.themesList):
            if event.type == pygame.MOUSEBUTTONDOWN and i == self.whichIsOver() and Constants.CNT > 12:
                self.cellThatIsClicked = i
                self.changeTheme(i)
            Constants.CNT = Constants.CNT + 1





