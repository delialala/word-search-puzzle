import pygame
import Constants
class Arrow():
    def __init__(self, win, x, y, direction):
        self.x = x
        self.y = y
        self.win = win
        self.direction = direction

    # call this method to draw the arrow on the screen
    def draw(self):
        if self.direction == "right":
            if self.isOver() == False:
                self.win.blit(Constants.arrow, (self.x, self.y))
            else:
                if pygame.mouse.get_pressed()[0]:
                    self.win.blit(Constants.arrowPressed, (self.x, self.y))
                else:
                    self.win.blit(Constants.arrowHover, (self.x-5, self.y-5))

        if self.direction == "left":
            if self.isOver() == False:
                self.win.blit(pygame.transform.flip(Constants.arrow, True, False), (self.x, self.y))
            else:
                if pygame.mouse.get_pressed()[0]:
                    self.win.blit(pygame.transform.flip(Constants.arrowPressed, True, False), (self.x, self.y))
                else:
                    self.win.blit(pygame.transform.flip(Constants.arrowHover, True, False), (self.x-5, self.y-5))

    def isOver(self):
        pos = pygame.mouse.get_pos()
        rect = Constants.arrow.get_rect(x=self.x, y = self.y)
        width = rect[2]
        height = rect[3]
        if pos[0] > self.x and pos[0] < self.x + width:
            if pos[1] > self.y and pos[1] < self.y + height:
                return True
        return False