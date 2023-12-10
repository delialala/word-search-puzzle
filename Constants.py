import pygame
# constants for the colors
WHITE = (224 , 248, 208)
LIGHTGREEN = (136, 192, 112)
DARKGREEN = (52, 104, 86)
BLACK = (8, 24, 23)
# these are used to fix a silly bug that happens
# when you click either "start" or "themes" in the intro page
CNT = 0
CNT2 = 0
# fills an image with transparency
def myFill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))
    return surface

# swaps oldcolor in an image with newcolor
def palette_swap(image, oldColor, newColor):
    imgCopy = image.copy()
    if image.get_height() < 120:
        myFill(imgCopy, newColor)
    else:
        imgCopy.fill(newColor)

    imgNew = image.copy()
    imgNew.set_colorkey(oldColor)
    image.blit(imgCopy, (0, 0))
    image.blit(imgNew, (0, 0))

    return image

def changeThemeImage(image, white, lightGray, darkGray, black):
    image = palette_swap(image, BLACK, black)
    image = palette_swap(image, WHITE, white)
    image = palette_swap(image, DARKGREEN, darkGray)
    image = palette_swap(image, LIGHTGREEN, lightGray)
    return image


# titlescreen
titleScreenImage = 9
# title
titleImage = 9
# arrow
arrow = 9
arrowPressed = 0
arrowHover = 0

