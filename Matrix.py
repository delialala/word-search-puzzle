import pygame
import Constants
import MatrixCell


class Matrix():
    def __init__(self, win, length):
        self.win = win
        self.length = length
        self.size = 700
        self.fontSize = int((self.size/length) * 0.5)
        self.cellSize = int(self.size/length)
        self.cellGap = self.cellSize + 4;
        self.xStart = 300
        self.yStart = 250

    # TODO: make the matrix containing the randomized words and letters
    def getRandomMatrix():
        pass

    def populateMatrix(self):
        # for testing purposes, i left the matrix be filled with D
        # TODO: replace the Ds with the matrix found in the getRandomMatrix function here
        self.cells = []
        crtX = self.xStart
        crtY = self.yStart
        for row in range(self.length):
            for col in range(self.length):
                crt = MatrixCell.MatrixCell(crtX, crtY, self.fontSize, 'D')
                crtX = crtX + self.cellGap
                self.cells.append(crt)
            crtY = crtY + self.cellGap
            crtX = self.xStart

    def draw(self):
        # the border
        borderSize = self.cellGap * self.length + 12
        pygame.draw.rect(self.win, Constants.DARKGREEN, (self.xStart + 4, self.yStart + 4, borderSize, borderSize), 0)

        # the matrix
        for crtCell in self.cells:
            crtCell.draw(self.win)
