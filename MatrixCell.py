import pygame
import Button
import Constants

# matrix cell inherits from the Button class
class MatrixCell(Button.Button):
    def __init__(self, xCell, yCell, fontSize, textCell=''):
        super().__init__(Constants.WHITE, xCell, yCell, fontSize, 50, 50, textCell)
        self.position = (0, 0)
    
    # call this method to draw the button on the screen
    def draw(self, win, outline = Constants.LIGHTGREEN):
        # check if theres any text and wrap the button size accordingly
        if self.text != '':
            font = pygame.font.Font('retro_computer_personal_use.ttf', size=self.fontSize)
            text = font.render(self.text, 1, Constants.BLACK)
            self.width = text.get_width() + 10
            self.height = text.get_height() + 10
            if self.width > self.height:
                self.height = self.width
            else:
                self.width = self.height
        # draw the button
        pygame.draw.rect(win, Constants.LIGHTGREEN, (self.x, self.y, self.width+12, self.height+12), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        # draw the text
        if self.text != '':
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        return self.width

