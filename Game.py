'''
Author: F3st1v3
Date: January 21 2022
Program name: Checkers
Description: Simulates checkers
'''

# Importing modules
import time
import pygame
from ButtonClass import *
from copy import deepcopy
import numpy as np
import random

# Initializing pygame
pygame.init()

# Defining the colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (151, 77, 0)
YELLOW = (255, 255, 0)
PINK = (255, 133, 133)
ORANGE = (255, 178, 102)
ORANGE2 = (225, 148, 72)
YELLOW2 = (253, 231, 70)


# Defining x length
x = 808

# Defining y length
y = 608

# Setting the pygame logo
pygame.display.set_icon(pygame.image.load("Resources/logo.png"))

# Setting the pygame window name
pygame.display.set_caption("Checkers")

# Defining display_surface as the display surface object of the dimensions x, y
display_surface = pygame.display.set_mode((x, y))

# Initializing images
playImg = pygame.image.load("Resources/playImg.png").convert_alpha()
playImgHover = pygame.image.load("Resources/playImgHover2.jpg").convert_alpha()
boardImg = pygame.image.load("Resources/board.png").convert_alpha()
blackPieceImg = pygame.image.load("Resources/blackPiece.png").convert_alpha()
blackPieceSelectImg = pygame.image.load("Resources/blackPieceSelect.jpg").convert_alpha()
whitePieceImg = pygame.image.load("Resources/whitePiece.png").convert_alpha()
highlightImg = pygame.image.load("Resources/highlight.jpg").convert_alpha()
winImg = pygame.image.load("Resources/win.png").convert_alpha()
loseImg = pygame.image.load("Resources/lose.png").convert_alpha()
menuImg = pygame.image.load("Resources/menuImg.png").convert_alpha()
menuImgHover = pygame.image.load("Resources/menuImgHover.png").convert_alpha()
playAgainImg = pygame.image.load("Resources/playAgainImg.png").convert_alpha()
playAgainImgHover = pygame.image.load("Resources/playAgainImgHover.png").convert_alpha()
exitImg = pygame.image.load("Resources/exitImg.png").convert_alpha()
exitImgHover = pygame.image.load("Resources/exitImgHover.png").convert_alpha()
blackPieceKingImg = pygame.image.load("Resources/blackPieceKingImg.png").convert_alpha()
blackPieceKingImgSelect = pygame.image.load("Resources/blackPieceKingImgSelect.png").convert_alpha()
whitePieceKingImg = pygame.image.load("Resources/whitePieceKingImg.png").convert_alpha()

# Creating menu button instances
playButton = Button(x / 2, y / 2, playImg, 0.4, display_surface)
playButtonHover = Button(x / 2, y / 2, playImgHover, 0.5, display_surface)
menuButton = Button(x / 2, y / 2, menuImg, 1, display_surface)
menuButtonHover = Button(x / 2, y / 2, menuImgHover, 1.1, display_surface)
playAgainButton = Button(x / 2, y // 2 + 115, playAgainImg, 1, display_surface)
playAgainButtonHover = Button(x / 2, y // 2 + 115, playAgainImgHover, 1.1, display_surface)
exitButton = Button(x / 2, y // 2 + 230, exitImg, 1, display_surface)
exitButtonHover = Button(x / 2, y // 2 + 230, exitImgHover, 1.1, display_surface)

# Defining font as Corbel with the size 72
font = pygame.font.SysFont('Corbel', 72)

# Defining img as the rendered text "Checkers" in brown (Title sequence)
img = font.render("Checkers", True, BROWN)

# Defining imgRect as img's rect
imgRect = img.get_rect()

# Setting the center of imgRect
imgRect.center = (x // 2, y // 4)

# Setting the default scene to menu. Because of this, the first page the user sees is the menu.
scene = "menu"

# Defining the coordinates of the centers of the squares (Calculations were done in another file to conserve performance)
spaces = {0: [142, 570], 1: [218, 570], 2: [294, 570], 3: [370, 570], 4: [446, 570], 5: [522, 570], 6: [598, 570], 7: [674, 570], 8: [142, 494], 9: [218, 494], 10: [294, 494], 11: [370, 494], 12: [446, 494], 13: [522, 494], 14: [598, 494], 15: [674, 494], 16: [142, 418], 17: [218, 418], 18: [294, 418], 19: [370, 418], 20: [446, 418], 21: [522, 418], 22: [598, 418], 23: [674, 418], 24: [142, 342], 25: [218, 342], 26: [294, 342], 27: [370, 342], 28: [446, 342], 29: [522, 342], 30: [598, 342], 31: [674, 342], 32: [142, 266], 33: [218, 266], 34: [294, 266], 35: [370, 266], 36: [446, 266], 37: [522, 266], 38: [598, 266], 39: [674, 266], 40: [142, 190], 41: [218, 190], 42: [294, 190], 43: [370, 190], 44: [446, 190], 45: [522, 190], 46: [598, 190], 47: [674, 190], 48: [142, 114], 49: [218, 114], 50: [294, 114], 51: [370, 114], 52: [446, 114], 53: [522, 114], 54: [598, 114], 55: [674, 114], 56: [142, 38], 57: [218, 38], 58: [294, 38], 59: [370, 38], 60: [446, 38], 61: [522, 38], 62: [598, 38], 63: [674, 38]}

# Defining resetting as a False bool. This is variable determines whether the game should reset or not.
resetting = False

def setupPieces():
    '''
    Initializes the pieces

    returns a dictionary of the whitePieces and the blackPieces
    '''


    # Declaring blackPiece and blackPieceIndex as lists
    blackPiece = []
    blackPieceIndex = []

    # Setting the counters to 0
    j = 0
    piece = 0
    square = 0

    # Creating black pieces for row 1
    for i in range(0, 8, 2):
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1, display_surface, highlightImg, blackPieceKingImg, "blackPiece{0}".format(piece), True, square, spaces, blackPieceSelectImg, blackPieceKingImgSelect))
        j += 1
        piece += 1
        square += 2
    
    # Resetting the counter
    j = 0
    square += 1

    # Creating black pieces for row 2
    for i in range(9, 17, 2):
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1,  display_surface, highlightImg, blackPieceKingImg, "blackPiece{0}".format(piece), True, square, spaces, blackPieceSelectImg, blackPieceKingImgSelect))
        j += 1
        piece += 1
        square += 2

    # Resetting the counter
    j = 0
    square -= 1

    # Creating black pieces for row 3
    for i in range(16, 24, 2):
        blackPiece.append(Button(spaces[i][0], spaces[i][1], blackPieceImg, 1, display_surface, highlightImg, blackPieceKingImg, "blackPiece{0}".format(piece), True, square, spaces, blackPieceSelectImg, blackPieceKingImgSelect))
        j += 1
        piece += 1
        square += 2

    # Declaring whitePiece and whitePieceIndex as lists
    whitePiece = []
    whitePieceIndex = []

    # Resetting the counter
    j = 0
    piece = 0

    # Creating white pieces for row 6
    for i in range(41, 48, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1, display_surface, None, whitePieceKingImg, "whitePiece{0}".format(piece), True, i, spaces))
        j += 1
        piece += 1

    # Resetting the counter
    j = 0

    # Creating white pieces for row 7
    for i in range(48, 56, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1, display_surface, None, whitePieceKingImg, "whitePiece{0}".format(piece), True, i, spaces))
        j += 1
        piece += 1

    # Resetting the counter
    j = 0

    # Creating white pieces for row 8
    for i in range(57, 64, 2):
        whitePiece.append(Button(spaces[i][0], spaces[i][1], whitePieceImg, 1, display_surface, None, whitePieceKingImg, "whitePiece{0}".format(piece), True, i, spaces))
        j += 1
        piece += 1

    # Setting up the index for both piece types
    for i in range(12):
        blackPieceIndex.append("blackPiece" + str(i))
        whitePieceIndex.append("whitePiece" + str(i))

    # Turning the 4 lists into 2 dictionaries
    blackPieceDict = dict(zip(blackPieceIndex, blackPiece))
    whitePieceDict = dict(zip(whitePieceIndex, whitePiece))

    # Returns the dictionaries in a list
    return [blackPieceDict, whitePieceDict]

# Setting global variables for the pieces
setupList = setupPieces()
blackPiece = setupList[0]
whitePiece = setupList[1]

# Defining turn as True as the user starts first
turn = True

# Setting the black and white piece counts to 12
blackPieces = 12
whitePieces = 12

# Declaring selectedList as a list
selectedList = []

# Declaring possibleEnemyMoves as a list
possibleEnemyMoves = []

def closest_node(node, nodes):
    '''
    Gets the closest node out of a list of nodes to a set node

    returns the closest node
    '''
    
    # Making sure nodes is a tuple
    nodes = tuple(nodes)
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    
    return np.argmin(dist_2)

def win():
    '''
    Creates the win scene
    '''

    # Accessing global variables
    global scene
    global resetting

    # Defining the win image
    winImgRect = pygame.Rect(0, 0, 400, 400)
    winImgRect.center = (x // 2, y // 4)

    # Setting the backgroud to orange
    display_surface.fill(ORANGE)

    # Displays the win image on screen
    display_surface.blit(winImg, winImgRect)

    # Draws the button onto the screen
    menuButton.draw()
    playAgainButton.draw()
    exitButton.draw()

    # If the menu button is clicked, go to the menu scene
    if menuButton.click()[0] == True:
        
        resetting = True
        scene = "menu"

    # If the play again button is clicked, go to the game scene
    if playAgainButton.click()[0] == True:

        resetting = True
        scene = "game"
    
    # If the exit button is clicked, close the program
    if exitButton.click()[0] == True:

        exit()

    # Hover animation for the menu button
    if menuButton.hover():

        menuButton.erase(ORANGE)

        menuButtonHover.draw()

    # Hover animation for the menu button
    if playAgainButton.hover():

        playAgainButton.erase(ORANGE)

        playAgainButtonHover.draw()
    
    # Hove animation for the exit button
    if exitButton.hover():

        exitButton.erase(ORANGE)

        exitButtonHover.draw()


def lose():
    '''
    Creates the lose scene
    '''


    # Accessing global variables
    global scene
    global resetting

    # Defining the lose image
    loseImgRect = pygame.Rect(0, 0, 400, 400)
    loseImgRect.center = (x // 2, y // 4)

    # Setting the background to orange
    display_surface.fill(ORANGE)

    # Draws the lose image
    display_surface.blit(loseImg, loseImgRect)

    # Draws the button onto the screen
    menuButton.draw()
    playAgainButton.draw()
    exitButton.draw()

    # If the menu button is clicked, go to the menu scene
    if menuButton.click()[0] == True:
        
        resetting = True
        
        scene = "menu"

    # If the play again button is clicked, go to the game scene
    if playAgainButton.click()[0] == True:

        resetting = True

        scene = "game"
    
    # If the exit button is clicked, exit the game
    if exitButton.click()[0] == True:

        exit()

    # Hover animation for the menu button
    if menuButton.hover():

        menuButton.erase(ORANGE)

        menuButtonHover.draw()

    # Hove animation for the play again button
    if playAgainButton.hover():

        playAgainButton.erase(ORANGE)

        playAgainButtonHover.draw()
    
    # Hover animation for the exit button
    if exitButton.hover():

        exitButton.erase(ORANGE)

        exitButtonHover.draw()

def game():
    '''
    Runs the game scene
    '''

    # Allows Access to the global variables
    global turn
    global whitePieces
    global blackPieces
    global scene
    global resetting
    global whitePiece
    global blackPiece

    # If the game should reset, it resets
    if resetting:

        setupList = setupPieces()
        blackPiece = setupList[0]
        whitePiece = setupList[1]
        whitePieces = 12
        blackPieces = 12
        resetting = False

    # Updates king values for all black pieces
    for i in blackPiece.values():

        i.kingCheck()

    # Updates king values for all white pieces
    for i in whitePiece.values():

        i.kingCheck()

    # Sets the background to orange
    display_surface.fill(ORANGE)

    # Displays the board
    display_surface.blit(boardImg, (104, 0))

    # Draws the pieces
    for k, v in blackPiece.items():

        v.draw()
    for k, v in whitePiece.items():

        v.draw()

    # If it's the user's turn, let the user make a move
    if turn == True:

        # If there are no black pieces left, the user loses
        if not blackPiece:

            time.sleep(0.25)

            scene = "lose"

        # Checks if the pieces have moves or not, and appends them to noMoves if they don't
        tempList = list(map(lambda x: x.checkerMoves(True)[1], blackPiece.values()))
        tempList1 = list(map(lambda x: x.checkerMoves(True)[0], blackPiece.values()))
        tempDict = dict(zip(tempList, tempList1))
        
        # If the same amount of pieces have no moves as the amount of pieces that exist (If all pieces have no moves), the user loses
        noneCount = 0
        piecesWithMoves = {}

        for k, v in tempDict.items():

            if v == ['None']:

                noneCount += 1

            else:

                piecesWithMoves[k] = v

        if noneCount == blackPieces:

            scene = "lose"

        # Get the events of the user every frame
        event = pygame.event.poll()

        # If the user clicks once, it checks if they clicked on a piece, then selects that piece.
        if event.type == pygame.MOUSEBUTTONDOWN:

                    # Gets the position of the user's mouse
                    pos = pygame.mouse.get_pos()

                    # Gets whether or not the user clicked on a button and stores it in a dictionary
                    blackPieceRectValues = list(map(lambda x: x.is_collide(pos[0], pos[1])[0], blackPiece.values()))
                    blackPieceRectKeys = list(map(lambda x: x.is_collide(pos[0], pos[1])[1], blackPiece.values()))
                    blackPieceRectDict = dict(zip(blackPieceRectKeys, blackPieceRectValues))

                    # Deepcopies the dictionary because you can't iterate over a dictionary and modify it at the same time in python3
                    blackPieceRectDictDC = deepcopy(blackPieceRectDict)

                    # Removes all values except for True in the dictionary (only items that remain are the pieces that were clicked)
                    for key, value in blackPieceRectDict.items():

                        if value != True:

                            del blackPieceRectDictDC[key]

                    # If there are any items left (If the user clicked on any pieces)
                    if blackPieceRectDictDC:

                        # Selects the piece that the user clicked on
                        for key in blackPieceRectDictDC.keys():

                            # Unselects the selected piece before selecing the next one
                            if selectedList:

                                blackPiece[selectedList[0]].unselect(selectedList)

                            # Selects the next piece
                            blackPiece[key].select(selectedList)
        
        # Highlights the moves the user's selected piece can do
        if selectedList:

            # highlights the moves for the selected piece
            blackPiece[selectedList[0]].checkerMoves(False)

        # If the user clicks again, it checks to see if they selected a valid square to move to
        if event.type == pygame.MOUSEBUTTONDOWN:            
                    
                    # if the user has any pieces selected
                    if selectedList:

                        # gets the closest square's coordinate
                        closestSquareCoord = closest_node(pos, list(spaces.values()))

                        # Uses a list comprehension to get the closest square
                        closestSquare = [k for k, v in spaces.items() if v == spaces[closestSquareCoord]][0]

                        movedList = blackPiece[selectedList[0]].checkerMove(closestSquare, spaces)

                        # If the user has moved, unselect their piece and set the turn to false (ends the turn)
                        if movedList[0] == True:

                            oldSquare = movedList[1]

                            tempList = list(map(lambda x: x.seeSquare()[1], whitePiece.values()))
                            tempList1 = list(map(lambda x: x.seeSquare()[0], whitePiece.values()))
                            tempDict = dict(zip(tempList, tempList1))

                            if closestSquare - oldSquare == 18:

                                for k, v in tempDict.items():

                                    if v == oldSquare + 9:

                                        del whitePiece[k]

                                        whitePieces -= 1

                            elif closestSquare - oldSquare == 14:

                                for k, v in tempDict.items():

                                    if v == oldSquare + 7:

                                        del whitePiece[k]

                                        whitePieces -= 1

                            if blackPiece[selectedList[0]].isKing():

                                if oldSquare - closestSquare == 18:

                                    for k, v in tempDict.items():

                                        if v == oldSquare - 9:

                                            del whitePiece[k]

                                            whitePieces -= 1

                                elif oldSquare - closestSquare == 14:

                                    for k, v in tempDict.items():

                                        if v == oldSquare - 7:

                                            del whitePiece[k]

                                            whitePieces -= 1

                            blackPiece[selectedList[0]].unselect(selectedList)

                            

                            turn = False

    # If it's not the user's turn
    else:

        # Update the display
        pygame.display.update()

        tempList = list(map(lambda x: x.enemyMoves()[1], whitePiece.values()))
        tempList1 = list(map(lambda x: x.enemyMoves()[0], whitePiece.values()))
        tempDict = dict(zip(tempList, tempList1))

        noneCount = 0
        piecesWithMoves = {}

        for k, v in tempDict.items():

            if v == ['None']:

                noneCount += 1

            else:

                piecesWithMoves[k] = v
        
        # Gets the squares of the black pieces and puts it into a dictionary with the piece names
        tempList = list(map(lambda x: x.seeSquare()[1], blackPiece.values()))
        tempList1 = list(map(lambda x: x.seeSquare()[0], blackPiece.values()))
        tempDict = dict(zip(tempList, tempList1))

        # If there are pieces with moves, choose a random piece and a random move, then move it
        if piecesWithMoves:

            currentPiece = random.choice(list(piecesWithMoves.keys()))

            enemyMoves0 = whitePiece[currentPiece].enemyMoves()

            enemyMove = random.choice(enemyMoves0[0])

            oldWhiteSquare = whitePiece[currentPiece].seeSquare()[0]

            whitePiece[currentPiece].checkerMove(enemyMove, spaces)

            newWhiteSquare = whitePiece[currentPiece].seeSquare()[0]

            # Checking if a piece should be captured or not after the white piece moves

            if oldWhiteSquare - newWhiteSquare == 18:

                for k, v in tempDict.items():

                    if v == newWhiteSquare + 9:

                        del blackPiece[k]

                        blackPieces -= 1

            elif oldWhiteSquare - newWhiteSquare == 14:

                for k, v in tempDict.items():

                    if v == newWhiteSquare + 7:

                        del blackPiece[k]

                        blackPieces -= 1
            
            if whitePiece[currentPiece].isKing() == True:

                if newWhiteSquare - oldWhiteSquare == 18:

                    for k, v in tempDict.items():

                        if v == newWhiteSquare - 9:

                            del blackPiece[k]

                            blackPieces -= 1

                if newWhiteSquare - oldWhiteSquare == 14:

                    for k, v in tempDict.items():

                        if v == newWhiteSquare - 7:

                            del blackPiece[k]

                            blackPieces -= 1

        # If no white pieces can move, change to the win scene
        if noneCount == whitePieces:

            time.sleep(0.25)

            scene = "win"
        
        # Ends the turn
        turn = True

        

def menu():
    '''
    Runs the menu scene
    '''

    # Making the background white
    display_surface.fill(ORANGE)

    # Displaying img on the screen
    display_surface.blit(img, imgRect)

    # Draws the button onto the screen
    playButton.draw()

    # If the play button is clicked, go to the game scene
    if playButton.click()[0] == True:
        
        global scene
        scene = "game"

    # Hover animation
    if playButton.hover():

        playButton.erase(ORANGE)

        playButtonHover.draw()

        pygame.display.update(playButton)
        
    

    # Updating the screen
    pygame.display.flip()

# Setting the clock
clock = pygame.time.Clock()

# Starting the game loop
while True:

    # Sets the frames per second to 30
    clock.tick(30)

    # Checks to see if the scene should be menu or game, and sets the scene accordingly
    if scene == "menu":
        menu()
    elif scene == "game":
        game()
    elif scene == "win":
        win()
    elif scene == "lose":
        lose()

    # Stopping the program if pygame.event.get() returns pygame.QUIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()
            

    # Draws the surface object to the screen
    pygame.display.update()
