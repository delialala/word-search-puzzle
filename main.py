import pygame
from pygame.locals import *
 
# app is our main class
class App:
    # class that will be called automatically at the beginning
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 800
    
    # initialize all pygame modules
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    # check if quit ever happens
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    # events happening each loop
    def on_loop(self):
         # Fill the background with white
        self._display_surf.fill((255, 255, 255))
        # Draw a solid blue circle in the center
        pygame.draw.circle(self._display_surf, (0, 0, 255), (250, 250), 75)

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