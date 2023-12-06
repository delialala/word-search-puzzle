import pygame
import Constants
class Button():
    def __init__(self, color, x, y, fontSize, width = 50, height = 50, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.fontSize = fontSize;
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False
    # call this method to draw the button on the screen
    def draw(self, win, outline=None):
        # check if theres any text and wrap the button size accordingly
        if self.text != '':
            font = pygame.font.Font('retro_computer_personal_use.ttf', size = self.fontSize)
            text = font.render(self.text, 1, Constants.WHITE)
            self.width = text.get_width() + 10
            self.height = text.get_height() + 10

        if outline:
            pygame.draw.rect(win, outline, (self.x-4, self.y-4, self.width+8, self.height+8), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # checks if mouse is hovering over the button
    # will be used when adding functionality to our buttons
    def isOver(self):
        pos = pygame.mouse.get_pos()
        # pos is the mouse position (a tuple of (x, y) coordinates)
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False