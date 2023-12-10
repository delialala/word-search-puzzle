import pygame
from pygame.locals import *
import Constants

# the wordlist from the main game page
class WordList:
    def __init__(self, win, words):
        self.win = win
        self.words = words
        self.fontSize = 20
        self.xStart = 70
        self.yStart = 240
        self.wordGap = 30

    # draws the rectangles
    def draw_rect(self):
        #total_height = len(self.words) * self.wordGap + 50
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart - 35, self.yStart - 5, 250, 520), 0)
        pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 20, self.yStart, 230, 500), 0)

    # draws the list title and the underline
    def draw_list_title(self):
        title_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", 25)
        title = title_font.render("WORD LIST", True, Constants.BLACK)
        title_rect = title.get_rect()
        title_rect.midtop = (self.xStart + 95, self.yStart)
        underline = pygame.Rect(self.xStart, self.yStart + 30, 190, 2)

        pygame.draw.rect(self.win, Constants.BLACK, underline)
        self.win.blit(title, title_rect)

    # draws the words on the list 
    # and colors the found words in the same color as the background 
    def draw_words(self, found_words):
        start_y = self.yStart + self.wordGap - 20
        # puts the words in the list
        for i, word in enumerate(self.words):
            list_font = pygame.font.Font("resources/retro_computer_personal_use.ttf", size = self.fontSize)
            text_color = Constants.BLACK
            # words are colored in the same color as the background when found in matrix
            if word in found_words:
               text_color = Constants.WHITE
            text = list_font.render(word, True, text_color)
            self.win.blit(text, (self.xStart, start_y + (i + 1) * self.wordGap))

    # draws the list
    def draw(self, found_words):
        self.draw_rect()
        self.draw_list_title()
        self.draw_words(found_words)
