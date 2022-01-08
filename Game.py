'''
Author: F3st1v3
Date: January 25 2022
Program name: Checkers
Description: Simulates checkers
'''

# Importing pygame
import pygame

# Importing ButtonClass.py
from ButtonClass import *

# Initializing pygame
pygame.init()

# Defining the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (153, 76, 0)
YELLOW = (255, 255, 0)
PINK = (255, 133, 133)
ORANGE = (255, 178, 102)

# Defining x as 640
x = 808

# Defining y as 480
y = 608

# Defining display_surface as the display surface object of the dimensions x, y
display_surface = pygame.display.set_mode((x, y))

# Loading images
playImg = pygame.image.load("Resources/playImg.png").convert_alpha()
playImgHover = pygame.image.load("Resources/playImgHover2.jpg").convert_alpha()
boardImg = pygame.image.load("Resources/board.png").convert_alpha()
blackPieceImg = pygame.image.load("Resources/blackPiece.png").convert_alpha()
whitePieceImg = pygame.image.load("Resources/whitePiece.png").convert_alpha()
'''
optionsImg = pygame.image.load("options.png").convert_alpha()
backImg = pygame.image.load("back.png").convert_alpha()
'''

# Creating button instances
playButton = Button(x / 2, y / 2, playImg, 0.4)
playButtonHover = Button(x / 2, y / 2, playImgHover, 0.5)

# Setting the pygame window name
pygame.display.set_caption("Checkers")

# Defining font as Corbel with the size 72
font = pygame.font.SysFont('Corbel', 72)

# Defining img as the rendered text "Checkers" in brown
img = font.render("Checkers", True, BROWN)

# Defining imgRect as img's rect
imgRect = img.get_rect()

# Setting the center of imgRect
imgRect.center = (x // 2, y // 4)

# Setting the default scene to menu
scene = "menu"

# Defining the coordinates of the centers of the squares (Calculations were done in another file to conserve performance)
spaces = {0: [142, 570], 1: [218, 570], 2: [294, 570], 3: [370, 570], 4: [446, 570], 5: [522, 570], 6: [598, 570], 7: [674, 570], 8: [142, 494], 9: [218, 494], 10: [294, 494], 11: [370, 494], 12: [446, 494], 13: [522, 494], 14: [598, 494], 15: [674, 494], 16: [142, 418], 17: [218, 418], 18: [294, 418], 19: [370, 418], 20: [446, 418], 21: [522, 418], 22: [598, 418], 23: [674, 418], 24: [142, 342], 25: [218, 342], 26: [294, 342], 27: [370, 342], 28: [446, 342], 29: [522, 342], 30: [598, 342], 31: [674, 342], 32: [142, 266], 33: [218, 266], 34: [294, 266], 35: [370, 266], 36: [446, 266], 37: [522, 266], 38: [598, 266], 39: [674, 266], 40: [142, 190], 41: [218, 190], 42: [294, 190], 43: [370, 190], 44: [446, 190], 45: [522, 190], 46: [598, 190], 47: [674, 190], 48: [142, 114], 49: [218, 114], 50: [294, 114], 51: [370, 114], 52: [446, 114], 53: [522, 114], 54: [598, 114], 55: [674, 114], 56: [142, 38], 57: [218, 38], 58: [294, 38], 59: [370, 38], 60: [446, 38], 61: [522, 38], 62: [598, 38], 63: [674, 38]}


def setupPieces():

    # Declaring blackPiece as a list
    blackPiece = []
    blackPieceIndex = []

    # Setting j (counter) to 0
    j = 0

    # Creating black pieces for row 1
    for i in range(0, 8, 2):
        
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1))
        j += 1
    
    # Resetting the counter
    j = 0

    # Creating black pieces for row 2
    for i in range(9, 17, 2):
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1))
        j += 1

    # Resetting the counter
    j = 0

    # Creating black pieces for row 3
    for i in range(16, 24, 2):
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1))
        j += 1

    # Declaring whitePiece as a list
    whitePiece = []
    whitePieceIndex = []

    # Resetting the counter
    j = 0

    # Creating white pieces for row 6
    for i in range(41, 48, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1))
        j += 1
    
    # Resetting the counter
    j = 0

    # Creating white pieces for row 7
    for i in range(48, 56, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1))
        j += 1

    j = 0

    for i in range(57, 64, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1))
        j += 1

    for i in range(12):
        blackPieceIndex.append("blackPiece" + str(i))
        whitePieceIndex.append("whitePiece" + str(i))

    blackPieceDict = dict(zip(blackPieceIndex, blackPiece))
    whitePieceDict = dict(zip(whitePieceIndex, whitePiece))

    return [blackPieceDict, whitePieceDict]

setupList = setupPieces()
blackPiece = setupList[0]
whitePiece = setupList[1]
turn = True

def game():

    display_surface.fill(ORANGE)

    display_surface.blit(boardImg, (104, 0))

    for i in range(12):
        
        blackPiece["blackPiece" + str(i)].draw(display_surface)
    
    for i in range(12):

        whitePiece["whitePiece" + str(i)].draw(display_surface)

    global turn

    if turn == True:

        

        # Ends the turn
        turn = False

    else:

        # Ends the turn
        turn = True

        

def menu():

    # Making the background white
    display_surface.fill(ORANGE)

    # Displaying img on the screen
    display_surface.blit(img, imgRect)

    playButton.draw(display_surface)

    if playButtonHover.click():
        
        global scene
        scene = "game"

    if playButton.hover():

        playButton.erase(display_surface, ORANGE)

        playButtonHover.draw(display_surface)

        pygame.display.update(playButton)
        
    

    # Updating the screen
    pygame.display.flip()

clock = pygame.time.Clock()

def selection():
    return 0


# Starting an infinite loop
while True:

    clock.tick(30)

    if scene == "menu":
        menu()
    elif scene == "game":
        game()

    # Stopping the program if pygame.event.get() returns pygame.QUIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

    # Draws the surface object to the screen
    pygame.display.update()
