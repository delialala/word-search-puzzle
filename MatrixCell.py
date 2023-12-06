import pygame
import Button
import Constants
import Matrix

# matrix cell inherits from the Button class
class MatrixCell(Button.Button):
    def __init__(self, xCell, yCell, fontSize, textCell=''):
        super().__init__(Constants.WHITE, xCell, yCell, fontSize, 50, 50, textCell)
        self.position = (0, 0)
        self.wasClicked = False
        self.isClicked4ever = False
        self.direction = "NOTCHOSEN"
    
    def setIsClicked4ever(self, myBool):
        self.isClicked4ever = myBool
    def setWasClicked(self, myBool):
        self.wasClicked = myBool
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getText(self):
        return self.text
    # call this method to draw the button on the screen
    def draw(self, win, matrix_enabled):
        # check if theres any text and wrap the button size accordingly
        if self.text != '':
            font = pygame.font.Font('retro_computer_personal_use.ttf', size=self.fontSize)
            text = font.render(self.text, 1, Constants.BLACK)
            self.width = text.get_width() + 10
            self.height = text.get_height() + 10
            if self.width > self.height:
                self.height = self.width
            else:
                self.width = self.height

        mainColor = Constants.WHITE
        outlineColor = Constants.LIGHTGREEN
        letterColor = Constants.BLACK

        # draw selection box
        if self.isOver()==True and matrix_enabled == True:
            pygame.draw.rect(win, Constants.WHITE, (self.x-6, self.y-6, self.width+24, self.height+24), 0)
            # check if button is pressed
        if self.wasClicked == True or self.isClicked4ever == True:
            mainColor = Constants.BLACK
            outlineColor = Constants.DARKGREEN
            letterColor = Constants.WHITE

        # update text
        font = pygame.font.Font('retro_computer_personal_use.ttf', size=self.fontSize)
        text = font.render(self.text, 1, letterColor)
        # draw the button
        pygame.draw.rect(win, outlineColor, (self.x, self.y, self.width+12, self.height+12), 0)
        pygame.draw.rect(win, mainColor, (self.x, self.y, self.width, self.height), 0)
        # draw the text
        if self.text != '':
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        return self.width

    # checks the direction the user should be going
    # after clicking on the 2nd cell
    def checkDirection(self, mainCell, secondCell):
        # vertical to each other
        if mainCell.getX() == secondCell.getX():
            if mainCell.getY() < secondCell.getY():
                return "UP"
            return "DOWN"
        # horizontal to each other
        if mainCell.getY() == secondCell.getY():
            if mainCell.getX() < secondCell.getX():
                return "RIGHT"
            return "LEFT"
        # second cell is somewhere to the right
        if mainCell.getX() < secondCell.getX():
            if mainCell.getY() < secondCell.getY():
                return "UPRIGHT"
            return "DOWNRIGHT"
        # second cell is somewhere to the left
        if mainCell.getY() < secondCell.getY():
            return "UPEFT"
        return "DOWNLEFT"


    def event(self, formedWord, cellList, event):
        # first check if the cursor is hovering over the button
        if self.isOver()==True:
            # now check if the mouse button is pressed
            if pygame.mouse.get_pressed()[0] == True:
                # if it hasnt been pressed before, mark it as pressed
                # add the letter to our current word too
                if self.wasClicked == False:
                    self.wasClicked = True
                    formedWord = formedWord + self.text
                    # add the button to a "pressed buttons" list
                    cellList.append(self)
        # check the direction of the last 2 cells
        if len(cellList) >= 2:
            dir = self.checkDirection(cellList[-1], cellList[-2])
            self.direction = dir

        return (formedWord, cellList, self.direction)