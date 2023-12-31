import pygame
import Constants
import MatrixCell
import random
from enum import Enum
import WordList

class Matrix():
    def __init__(self, win, length):
        self.win = win
        self.length = length
        self.size = 700
        self.fontSize = int((self.size/length) * 0.5)
        self.cellSize = int(self.size/length)
        self.cellGap = self.cellSize + 4
        self.borderSize = self.cellGap * self.length + 12
        self.xStart = 350
        self.yStart = 230
        self.formedWord = ''
        self.cnt = 0
        self.cellList = []
        self.InitialDirecton = "NOTCHOSEN"
        self.crtDirection = "NOTCHOSEN"
        self.matrix_enabled = True
        self.stop_adding_words = False

    # will place the random word in a random direction if possible
    def place_word(self, word, direction, word_positions, word_directions):
        if direction == "vertical":
            placement = self.place_vertical(word, word_positions)
        elif direction == "horizontal":
            placement = self.place_horizontal(word, word_positions)
        elif direction == "diagonal":
            placement = self.place_diagonal(word, word_positions)
        
        word_directions[word] = direction
        if placement == True:
            return True
        return False

    # vertical word placement
    def place_vertical(self, word, word_positions):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - len(word))
        rand_col = random.randint(0, self.length - 1)
        word_positions[word] = (rand_row, rand_col)

        row = rand_row
        for i in range(len(word)):
            if (self.cells[row * self.length + rand_col].text == word[i]
            or self.cells[row * self.length + rand_col].text == '' ):
                sw = 0
                if row < self.length:
                    row = row + 1
                else:
                    break
            else:
                sw = 1
                break
        
        if sw == 0:
            crtY = crtY + rand_row * self.cellGap
            if rand_col != 0:
                crtX = crtX + rand_col * self.cellGap
            for i in range(len(word)):
                crt = MatrixCell.MatrixCell(crtX, crtY, self.fontSize, word[i])
                self.cells[rand_row * self.length + rand_col] = crt
                rand_row = rand_row + 1
                crtY = crtY + self.cellGap
        elif sw == 1:
            return False
        return True

    # horizontal word placement
    def place_horizontal(self, word, word_positions):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - 1)
        rand_col = random.randint(0, self.length - len(word))
        word_positions[word] = (rand_row, rand_col)

        col = rand_col
        for i in range(len(word)):
            if (self.cells[rand_row * self.length + col].text == word[i]
            or self.cells[rand_row * self.length + col].text == '' ):
                sw = 0
                if col < self.length:
                    col = col + 1
                else:
                    break
            else:
                sw = 1
                break
        
        if sw == 0:
            crtX = crtX + rand_col * self.cellGap
            crtY = crtY + rand_row * self.cellGap
            for i in range(len(word)):
                crt = MatrixCell.MatrixCell(crtX, crtY, self.fontSize, word[i])
                self.cells[rand_row * self.length + rand_col] = crt
                rand_col = rand_col + 1
                crtX = crtX + self.cellGap
        elif sw == 1:
            return False
        return True

    # diagonal word placement
    def place_diagonal(self, word, word_positions):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - len(word))
        rand_col = random.randint(0, self.length - len(word))
        word_positions[word] = (rand_row, rand_col)

        row = rand_row
        col = rand_col
        for i in range(len(word)):
            if (self.cells[row * self.length + col].text == word[i]
            or self.cells[row * self.length + col].text == '' ):
                sw = 0
                if (row < self.length and col < self.length):
                    row = row + 1
                    col = col + 1
                else:
                    break
            else:
                sw = 1
                break
        
        if sw == 0:
            crtX = crtX + rand_col * self.cellGap
            crtY = crtY + rand_row * self.cellGap
            for i in range(len(word)):
                crt = MatrixCell.MatrixCell(crtX, crtY, self.fontSize, word[i])
                self.cells[rand_row * self.length + rand_col] = crt
                rand_row = rand_row + 1
                rand_col = rand_col + 1
                crtX = crtX + self.cellGap
                crtY = crtY + self.cellGap
        elif sw == 1:
            return False
        return True

    # populates the matrix with words placed in different directions
    def getRandomMatrixWords(self, words, words_in_matrix, word_positions, word_directions):
        for word in words:
            word = word.upper()
            direction = random.choice(["vertical", "horizontal", "diagonal"])
            if self.place_word(word, direction, word_positions, word_directions) == True:
                if self.stop_adding_words == False:
                    words_in_matrix.append(word)
                    if len(words_in_matrix) == 15:
                        self.stop_adding_words = True

    # populates the empty matrix cells with random letters
    def getRandomMatrixLetters(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        crtX = self.xStart
        crtY = self.yStart
        for row in range(self.length):
            for col in range(self.length):
                crt = MatrixCell.MatrixCell(crtX, crtY, self.fontSize, random.choice(alphabet))
                crtX = crtX + self.cellGap
                if self.cells[row * self.length + col].text == '':
                    self.cells[row * self.length + col] = crt
            crtY = crtY + self.cellGap
            crtX = self.xStart

    # populates the matrix
    def populateMatrix(self, words, words_in_matrix, word_positions, word_directions):
        self.cells = [MatrixCell.MatrixCell(0, 0, self.fontSize, '') for _ in range(self.length * self.length)]
        self.getRandomMatrixWords(words, words_in_matrix, word_positions, word_directions)
        self.getRandomMatrixLetters()

    def draw(self):
        # the border
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart + 4, self.yStart + 4, self.borderSize, self.borderSize), 0)
        #pygame.draw.rect(self.win, Constants.BLACK,(200,500,900,900), 0)
        # the matrix
        for crtCell in self.cells:
            crtCell.draw(self.win, self.matrix_enabled)

    # unclicks the currently selected cells
    def clearCellList(self):
        for myCell in self.cellList:
            myCell.setWasClicked(False)
        self.cellList = []
        self.InitialDirecton = "NOTCHOSEN"
        self.crtDirection = "NOTCHOSEN"

    # check if two cells are neighbors
    def isNeighbor(self, mainCell, secondCell):
        # neighbors to the left

        if mainCell.getX() - self.cellGap == secondCell.getX():
            if mainCell.getY() - self.cellGap == secondCell.getY():
                return True
            if mainCell.getY() == secondCell.getY():
                return True
            if mainCell.getY() + self.cellGap == secondCell.getY():
                return True
        # neighbors in the center
        if mainCell.getX() == secondCell.getX():
            if mainCell.getY() - self.cellGap == secondCell.getY():
                return True
            if mainCell.getY() == secondCell.getY():
                return True
            if mainCell.getY() + self.cellGap == secondCell.getY():
                return True
        # neighbors to the right
        if mainCell.getX() + self.cellGap == secondCell.getX():
            if mainCell.getY() - self.cellGap == secondCell.getY():
                return True
            if mainCell.getY() == secondCell.getY():
                return True
            if mainCell.getY() + self.cellGap == secondCell.getY():
                return True
        return False


    def event(self, event, words, found_words):
        pos = pygame.mouse.get_pos()

        # the matrix is disabled when there is a pop up window on the screen
        if self.matrix_enabled == False:
            return

        # only activates if the cursor is inside the matrix
        if (pos[0] > self.xStart and pos[0] < self.xStart + self.borderSize
        and pos[1] > self.yStart and pos[1] < self.yStart + self.borderSize):
                # for each cell:
                # - check the event
                # - update the currently formed word
                # - check if the selected cell has the same direction as the others
                # - check if the selected cell is a neighbor
                hasItBeenChanged = False
                for crtCell in self.cells:
                    (self.formedWord, self.cellList, direction) = crtCell.event(self.formedWord, self.cellList, event)
                    if len(self.cellList) == 2 and self.InitialDirecton == "NOTCHOSEN" and direction != "NOTCHOSEN":
                        self.InitialDirecton = direction
                    if len(self.cellList) >= 2 and direction != "NOTCHOSEN" and hasItBeenChanged == False:
                        hasItBeenChanged = True
                        self.crtDirection = direction

                # check if the last 2 cells are neighbors
                if len(self.cellList) >= 2:
                    if self.isNeighbor(self.cellList[-1], self.cellList[-2]) == False:
                        self.clearCellList()
                        self.formedWord = ''

                # check if the direction is correct
                if self.crtDirection != self.InitialDirecton and self.crtDirection != "NOTCHOSEN" and self.InitialDirecton != "NOTCHOSEN":
                    self.clearCellList()
                    self.formedWord = ''
                self.crtDirection = "NOTCHOSEN"

                # check if the user lets go of the mouse
                if pygame.mouse.get_pressed()[0] == False:
                    # check if the word formed can be found inside our world list
                    if self.formedWord in words:

                        found_words.append(self.formedWord)

                        # the cells remain clicked forever
                        for myCell in self.cellList:
                            myCell.setIsClicked4ever(True)
                    self.clearCellList()
                    self.formedWord = ''
        # if outside the matrix, clear the list
        else:
            self.formedWord = ''
            self.clearCellList()
