import pygame
from pygame.locals import *
import Constants
import Matrix
import WordList
import random
import Intro
import ReturnButton
import GameSettingsPopUp
import CongratsPopUp
import UhohPopUp
import HintButton
import HintPopUp
found_words = []
words = []
words_in_matrix = []
matrix_size = 0
all_words = False
TIMER_EVENT = pygame.USEREVENT + 1
word_positions = {}
word_directions = {}

# app is our main class
class App:
    # class that will be called automatically at the beginning
    # basically a constructor
    def __init__(self):
        pygame.font.init()
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1120, 1008
        self.main_game_initialized = False

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

    # check when quit happens
    def on_event(self, event, found_words):
        if event.type == pygame.QUIT:
            self._running = False
        # handle the countdown evet
        elif event.type == TIMER_EVENT and self.intro_page.settings_popup.timer != 'N/A':
            self.intro_page.settings_popup.countdown_timer_event()
        # handle the intro page events
        elif self.intro_page.in_intro_page:
            self.intro_page.click_start(event)
            self.intro_page.click_settings(event)
            self.intro_page.click_close(event)
            self.intro_page.clickTheme(event)
            self.intro_page.click_start_in_settings(event)
            self.intro_page.clickGameSettings(event, all_words)
        # handle main page events
        elif self.main_game_initialized:
                self.letterMatrix.event(event, self.words, found_words)
                self.returnButton.event(event, self.intro_page)
                self.hintButton.click_hint(event)
                self.hintPopUp.click_word(event, found_words, word_positions)
                self.hintPopUp.click_close(event)
                if event.type == pygame.MOUSEBUTTONDOWN and self.congratsPopUp.main_screen_button.isOver():
                    self.reset_and_return()
                if event.type == pygame.MOUSEBUTTONDOWN and self.uhohPopUp.main_screen_button.isOver():
                    self.reset_and_return()


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
            if self.main_game_initialized == True:
                self._display_surf.blit(Constants.titleImage, (200, 60))
                # draw the matrix
                self.letterMatrix.draw()
                # draw the word list
                self.wordList.draw(found_words, False)
                # draw hint button
                self.hintButton.draw()
                # draw return button
                self.returnButton.draw()

                # if player finds all the words congrats window pops up
                if len(self.words) == len(found_words):
                    self.congratsPopUp.active = True
                    self.intro_page.settings_popup.timer_running = False
                    self.congratsPopUp.draw()

                # if the congrats window is not active and the set timer ran out
                # it means the player failed and the Uhoh window pops up
                if self.congratsPopUp.active == False:
                    if self.intro_page.settings_popup.timer_left == 0:
                        self.uhohPopUp.active = True
                        self.uhohPopUp.draw()

                # the hint button was clicked -> hint window pops up
                if self.hintButton.clicked_hint == True:
                    self.hintPopUp.active = True
                    self.hintPopUp.draw(found_words, word_positions, word_directions)

                # the hint pop up is on the screen but the close button was clicked
                # -> closes hint window
                if self.hintPopUp.active == True and self.hintPopUp.close == True:
                    #print("YES")
                    self.hintPopUp.active = False
                    self.hintPopUp.close = False
                    self.hintButton.clicked_hint = False

                # click return button -> go to intro game page
                if self.returnButton.clicked == True:
                    self.reset_and_return()

                # the matrix will not work when there is a pop up on the screen
                if self.congratsPopUp.active or self.uhohPopUp.active or self.hintPopUp.active:
                    #print("OK")
                    self.letterMatrix.matrix_enabled = False

                # the matrix will work if there is no pop up on the screen
                if not self.congratsPopUp.active and not self.uhohPopUp.active and not self.hintPopUp.active:
                    #print("VERY OK")
                    self.letterMatrix.matrix_enabled = True

                # the hint button will not work when there is a pop up on the screen
                if self.congratsPopUp.active or self.uhohPopUp.active or self.hintPopUp.active:
                    self.hintButton.is_enabled = False

                # the hint button will work if there is no pop up on the screen
                if not self.congratsPopUp.active and not self.uhohPopUp.active and not self.hintPopUp.active:
                    self.hintButton.is_enabled = True

                # the return button will not work when there is a pop up on the screen
                if self.congratsPopUp.active or self.uhohPopUp.active or self.hintPopUp.active:
                    self.returnButton.is_enabled = False

                # the return button will work if there is no pop up on the screen
                if not self.congratsPopUp.active and not self.uhohPopUp.active and not self.hintPopUp.active:
                    self.returnButton.is_enabled = True

                # draws the timer on main game page
                self.intro_page.settings_popup.draw_timer()
                
        pygame.display.flip()

    # quits the game
    def on_cleanup(self):
        pygame.quit()

    # initializes the main game page
    def init_main_game(self):
        # player is in the main game page -> timer starts
        self.intro_page.settings_popup.timer_running = True
        # get the matrix size and domain chosen by the player
        matrix_size = self.intro_page.settings_popup.matrix_size
        domain = self.intro_page.settings_popup.domain

        if self.main_game_initialized == False:
            self.letterMatrix = Matrix.Matrix(self._display_surf, matrix_size)
            word_list = []

            if domain == "YUMYUM":
                text_file = open("food.txt", 'r')
            if domain == "LALA":
                text_file = open("music.txt", 'r')
            if domain == "PEWPEW":
                text_file = open("war.txt", 'r')
            if domain == "HOWDY":
                text_file = open("howdy.txt", 'r')
            if domain == "SHREK":
                text_file = open("shrek.txt", 'r')
            if domain == "RANDOM":
                text_file = open("words.txt", 'r')
            lines = text_file.readlines()
            text_file.close()
            aux = 0
            for i in range(len(lines)):
                cuv = lines[i].strip()
                if len(cuv) <= matrix_size:
                    word_list.append(cuv)
                    aux += 1
                words = random.sample(word_list, aux)
            print(words)
            
            self.letterMatrix.populateMatrix(words, words_in_matrix, word_positions, word_directions)
            self.words = [x.upper() for x in words_in_matrix]
            print(f"{len(self.words)}")
            self.wordList = WordList.WordList(self._display_surf, self.words)
            self.returnButton = ReturnButton.ReturnButton(self._display_surf, 70, 800)
            self.congratsPopUp = CongratsPopUp.CongratsPopUp(self._display_surf, 325, 350, 500, 300, "CONGRATS!")
            self.uhohPopUp = UhohPopUp.UhohPopUp(self._display_surf, 325, 350, 500, 300, "TIME IS UP!")
            self.hintButton = HintButton.HintButton(self._display_surf, 210, 800, 30, "HINT")
            self.hintPopUp = HintPopUp.HintPopUp(self._display_surf, 220, 250, 650, 600, "HINTS", self.words)

            self.main_game_initialized = True

    # resets the game and goes from the main game page to the intro page
    # used by the MainScreenButton
    def reset_and_return(self):
        self.intro_page.settings_popup.timer_running = False
        self.intro_page.in_intro_page = True
        self.intro_page.toMain = False
        self.main_game_initialized = False
        del found_words[:]
        del words[:]
        del words_in_matrix[:]
        del self.words[:]
        del self.wordList.words[:]
        matrix_size = 0
        all_words = False


    # loop for running the game
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        pygame.display.set_caption("WORD SPY")
        pygame.time.set_timer(TIMER_EVENT, 1000)
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event, found_words)
            if self.intro_page.toMain:
                self.init_main_game()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()