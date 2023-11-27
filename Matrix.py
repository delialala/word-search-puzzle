import pygame
import Constants
import MatrixCell
import random


class Matrix():
    def __init__(self, win, length):
        self.win = win
        self.length = length
        self.size = 700
        self.fontSize = int((self.size/length) * 0.5)
        self.cellSize = int(self.size/length)
        self.cellGap = self.cellSize + 4
        self.xStart = 300
        self.yStart = 250

    # will place the random word in a random direction if possible
    def place_word(self, word, direction):
        if direction == "vertical":
            placement = self.place_vertical(word)
        elif direction == "horizontal":
            placement = self.place_horizontal(word)
        elif direction == "diagonal":
            placement = self.place_diagonal(word)
        
        if placement == True:
            return True
        return False

    # vertical word placement
    def place_vertical(self, word):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - len(word))
        rand_col = random.randint(0, self.length - 1)
        print(f"{rand_row} {rand_col}")

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
    def place_horizontal(self, word):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - 1)
        rand_col = random.randint(0, self.length - len(word))
        print(f"{rand_row} {rand_col}")

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
    def place_diagonal(self, word):
        crtX = self.xStart
        crtY = self.yStart
        rand_row = random.randint(0, self.length - len(word))
        rand_col = random.randint(0, self.length - len(word))
        print(f"{rand_row} {rand_col}")

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
    def getRandomMatrixWords(self, words):
        for word in words:
            word = word.upper()
            direction = random.choice(["vertical", "horizontal", "diagonal"])
            print(f"{direction}")
            self.place_word(word, direction)

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
    def populateMatrix(self, words):
        self.cells = [MatrixCell.MatrixCell(0, 0, self.fontSize, '') for _ in range(self.length * self.length)]
        self.getRandomMatrixWords(words)
        self.getRandomMatrixLetters()

    def draw(self):
        # the border
        borderSize = self.cellGap * self.length + 12
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart + 4, self.yStart + 4, borderSize, borderSize), 0)

        # the matrix
        for crtCell in self.cells:
            crtCell.draw(self.win)
