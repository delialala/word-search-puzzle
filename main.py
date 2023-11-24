import pygame
from pygame.locals import *
import Button
import Constants
import MatrixCell
import Matrix
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

        self.letterMatrix = Matrix.Matrix(self._display_surf, 7)
        self.letterMatrix.populateMatrix()

    # check when quit happens
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    # events happening each loop
    def on_loop(self):
        # fill the background with white
        self._display_surf.fill(Constants.LIGHTGREEN)
        # draw the matrix
        self.letterMatrix.draw()

    # renders our objects each loop
    def on_render(self):
        pygame.display.flip()
    
    # quits the game
    def on_cleanup(self):
        pygame.quit()

    # loop for running the game
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()