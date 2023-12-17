import pygame
from pygame.locals import *
import Constants
import SettingsPopUp
import CloseButton
import Matrix

# hint pop-up window from main game page
class HintPopUp(SettingsPopUp.SettingsPopUp):
    def __init__(self, win, x, y, width, height, title, words):
        super().__init__(win, x, y, width, height, title)
        self.close_button = CloseButton.CloseButton(self.xCloseButton, self.yCloseButton - 30, 30, 10, 10)
        self.close = False
        self.active = False
        self.words = words
        self.index = -1

    # draw the words and hints
    def draw_hint_list(self, found_words, word_positions, word_directions):
        text_font = pygame.font.Font('resources/retro_computer_personal_use.ttf', 20)
        for i, word in enumerate(self.words):
            # the found words will not be part of the hint word list
            if word not in found_words:
                text = text_font.render(word, True, Constants.DARKGREEN)
                # draw word
                self.win.blit(text, (self.x + 20, self.y + 80 + i * 40))
                # the current word matches the saved index -> dislpay hints
                if self.index == i:
                    if word in word_positions:
                        # the hints are the position of the first letter of the word
                        row, col = word_positions[word]
                        # and the placement
                        dir = word_directions[word]
                        text = f"Row: {row}, Col: {col}, Pos: {dir}"
                        text_render = text_font.render(text, True, Constants.DARKGREEN)
                        # draw hints
                        self.win.blit(text_render,(self.x + 200, self.y + 80 + i*40))

    # draw the window
    def draw(self, found_words, word_positions, word_directions):
        if self.active == True:
            super().draw()
            # draw the close button
            self.close_button.draw(self.win)
            # draw the words and hints
            self.draw_hint_list(found_words, word_positions, word_directions)

    # click on "X" -> window closes
    def click_close(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.close_button.isOver():
            self.close = True

    # handle the click_on_word event
    def click_word(self, event, found_words, word_positions):
        text_font = pygame.font.Font('resources/retro_computer_personal_use.ttf', 20)
        # click happens
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y=event.pos
            for i, word in enumerate(self.words):
                if word not in found_words:
                    # checks if the click is within bounds of th word in the list
                    if (self.x+20 <= x <= self.x + 20 + text_font.size(word)[0] and
                    self.y+ 80 + i*40 <= y <= self.y + 80 + i*40 + text_font.size(word)[1]):
                        # will save the index
                        self.index = i
                        print("Word pressed: ", word)
