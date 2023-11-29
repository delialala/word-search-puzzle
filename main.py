import pygame
from pygame.locals import *
import Button
import Constants
import MatrixCell
import Matrix
import random
# app is our main class
class App:
    # class that will be called automatically at the beginning
    # basically a constructor
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1120, 1008

    # initialize all pygame modules
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.letterMatrix = Matrix.Matrix(self._display_surf, 9)
        # get words from words.txt
        word_list = []
        words = []
        text_file = open("words.txt", 'r')
        lines = text_file.readlines()
        text_file.close()
        for i in range(len(lines)):
            word_list.append(lines[i].strip())
        words = random.sample(word_list, 7)

        print(words)
        # make words global to this class
        # because it needs to be accessed by other functions too
        self.words = [x.upper() for x in words]
        self.letterMatrix.populateMatrix(words)

        # change the basic colors
        Constants.WHITE = (224 , 248, 208)
        Constants.LIGHTGREEN = (136, 192, 112)
        Constants.DARKGREEN = (52, 104, 86)
        Constants.BLACK = (8, 24, 23)

    # check when quit happens
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        self.letterMatrix.event(event, self.words)
    
    # events happening each loop
    def on_loop(self):
        pass

    # renders our objects each loop
    def on_render(self):
        pygame.display.flip()
        # fill the background with white
        self._display_surf.fill(Constants.LIGHTGREEN)
        # draw the matrix
        self.letterMatrix.draw()



    # quits the game
    def on_cleanup(self):
        pygame.quit()

    # loop for running the game
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        pygame.display.set_caption("Word Search Puzzle")
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()