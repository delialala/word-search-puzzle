import pygame
import Button
import Constants

class StartscreenButton(Button.Button):
        def __init__(self, x, y, text):
            super().__init__(Constants.WHITE, x, y, 30, 50, 50, text)
        def draw(self, win):
            if self.text != '':
                font = pygame.font.Font('resources/retro_computer_personal_use.ttf', size=self.fontSize)
                text = font.render(self.text, 1, Constants.BLACK)
                self.width = 300
                self.height = text.get_height() + 10

            # draw selection box
            if self.isOver()==True:
                pygame.draw.rect(win, Constants.WHITE, (self.x-12, self.y-12, self.width+24, self.height+34), 0)
            # draw the button
            pygame.draw.rect(win, Constants.BLACK, (self.x-6, self.y-6, self.width+12, self.height+22), 0)
            pygame.draw.rect(win, Constants.LIGHTGREEN, (self.x, self.y, self.width, self.height+6), 0)
            pygame.draw.rect(win, Constants.WHITE, (self.x, self.y, self.width, self.height), 0)
            # draw the text
            if self.text != '':
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            return self.width
