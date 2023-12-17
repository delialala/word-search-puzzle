import pygame
import Arrow
import Constants
class ThingieChooser:
    def __init__(self, win, list, x, y):
        self.win = win
        self.list = list
        self.x = x
        self.y = y
        self.arrowLeft = Arrow.Arrow(win, x - 100, y, "right")#x
        self.arrowRight = Arrow.Arrow(win, x + 200, y, "left")#x+200
        self.crt = 0

    def draw(self):
        self.arrowLeft.draw()
        self.arrowRight.draw()

        font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 30)
        matrixSizeText = font.render(str(self.list[self.crt]), True, Constants.DARKGREEN)
        item_width = matrixSizeText.get_width()
        text_x = self.x + 80 - item_width/2
        self.win.blit(matrixSizeText, (text_x, self.y, 200, 200))#x+120
    
    # decrease or increase the current index
    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.arrowLeft.isOver():
            self.crt = self.crt - 1
            if self.crt == -1:
                self.crt = len(self.list) - 1

        if event.type == pygame.MOUSEBUTTONDOWN and self.arrowRight.isOver():
            self.crt = self.crt + 1
            if self.crt == len(self.list):
                self.crt = 0

