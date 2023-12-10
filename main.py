import pygame
from pygame.locals import *
import Constants
import Matrix
import WordList
import random
import Intro
import ReturnButton
found_words = []

# app is our main class
class App:
    # class that will be called automatically at the beginning
    # basically a constructor
    def __init__(self):
        pygame.font.init()
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1120, 1008

    # initialize all pygame modules 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        # load the image for the titlescreen
        Constants.titleScreenImage = pygame.image.load("resources/TITLESCREEN_CLASSICGREEN.png").convert()
        # load the image for the title
        Constants.titleImage = pygame.image.load("resources/TITLE_CLASSICGREEN.png")
        Constants.arrow = pygame.image.load("resources/ARROW.png")
        Constants.arrowHover = pygame.image.load("resources/ARROW_HOVER.png")
        Constants.arrowPressed = pygame.image.load("resources/ARROW_PRESSED.png")

        self.intro_page = Intro.Intro(self._display_surf)
        
        self.letterMatrix = Matrix.Matrix(self._display_surf, 9)
        # get words from words.txt
        word_list = []
        words = []
        words_in_matrix = []
        text_file = open("words.txt", 'r')
        lines = text_file.readlines()
        text_file.close()
        for i in range(len(lines)):
            word_list.append(lines[i].strip())
        words = random.sample(word_list, 7)

        print(words)
        # make words global to this class
        # because it needs to be accessed by other functions too
        self.letterMatrix.populateMatrix(words, words_in_matrix)
        self.words = [x.upper() for x in words_in_matrix]
        self.wordList = WordList.WordList(self._display_surf, self.words)
        self.returnButton = ReturnButton.ReturnButton(self._display_surf, 70, 800)
    # check when quit happens
    def on_event(self, event, found_words):
        if event.type == pygame.QUIT:
            self._running = False
        elif self.intro_page.in_intro_page:
            self.intro_page.click_start(event)
            self.intro_page.click_settings(event)
            self.intro_page.click_close(event)
            self.intro_page.clickTheme(event)
            self.intro_page.click_start_in_settings(event)
            self.intro_page.clickGameSettings(event)
        else:
            self.letterMatrix.event(event, self.words, found_words)
            self.returnButton.event(event, self.intro_page)


    # events happening each loop
    def on_loop(self):
        pass

    # renders our objects each loop
    def on_render(self):
        # fill the background with the general color
        self._display_surf.fill(Constants.LIGHTGREEN)
        if self.intro_page.in_intro_page:
            # draw intro page
            self.intro_page.draw()
        else:
            self._display_surf.blit(Constants.titleImage, (200, 60))
            # draw the matrix
            self.letterMatrix.draw()
            # draw the word list
            self.wordList.draw(found_words)
            self.returnButton.draw()


        pygame.display.flip()

    # quits the game
    def on_cleanup(self):
        pygame.quit()

    # loop for running the game
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        pygame.display.set_caption("WORD SPY")
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event, found_words)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()