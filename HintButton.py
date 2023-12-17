import pygame
from pygame.locals import *
import Button
import Constants

# hint button in main game page
class HintButton(Button.Button):
    def __init__(self, win, xStart, yStart, fontSize, textCell=''):
        super().__init__(Constants.WHITE, xStart, yStart, fontSize, 70, 70, textCell)
        self.win = win
        self.fontSize = 40
        self.xStart = xStart
        self.yStart = yStart
        self.is_enabled = True

        self.clicked_hint = False

    # draw the hint button
    def draw(self):
        # draw selection box
        if self.isOver() and self.is_enabled:
            pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 44, self.yStart - 13, 180, 140), 0)

        # draw the rectangles
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart - 35, self.yStart - 5, 160, 120), 0)
        pygame.draw.rect(self.win, Constants.WHITE, (self.xStart - 20, self.yStart, 140, 90), 0)
        text_font = pygame.font.Font('resources/retro_computer_personal_use.ttf', self.fontSize)
        text1 = text_font.render("HINT", True, Constants.DARKGREEN)
        text1_rect = text1.get_rect(center=(self.xStart + 52, self.yStart + 42))
        # draw text on the button
        self.win.blit(text1, text1_rect)
        text2 = text_font.render("HINT", True, Constants.LIGHTGREEN)
        text2_rect = text2.get_rect(center=(self.xStart + 50, self.yStart + 40))
        # draw text on the button
        self.win.blit(text2, text2_rect)

    # handle click_on_hint_button event
    def click_hint(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.isOver() and self.is_enabled:
            self.clicked_hint = True
