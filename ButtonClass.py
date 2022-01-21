'''
Author: F3st1v3
Date: January 21 2022
Program name: ButtonClass
Description: A class for buttons used in the main program. I seperated the files to make it more clear.
'''
# Imports pygame (Needs to be imported to work properly)
import pygame

# Defines the Button class
class Button:
    def __init__(self, x, y, image, scale, surface, highlight = None, kingImage=False, name="None", checkerPiece=False, square=10, squareDict=False, selectedImg = False, kingSelectedImg = False):
        '''
        initializing the button
        '''
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.imageDimensions = [width, height]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.king = False
        self.name = name
        self.selected = False
        self.oldimage = False
        self.oldrectcenter = False
        self.checkerPiece = checkerPiece
        self.square = square
        self.surface = surface
        self.highlight = highlight
        self.squareDict = squareDict
        self.selectedImg = selectedImg
        self.selectedKingImg = kingSelectedImg
        if kingImage != False:

            self.kingImage = kingImage

    def getPixelColour(self, square):
        '''
        Gets the pixel colour at a given square

        returns the pixel's colour
        '''

        return self.surface.get_at((self.squareDict[square][0], self.squareDict[square][1]))[:3]

    def draw(self):
        '''
        Draws the button onto the screen
        '''
           
        # Draw button
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def hover(self):
        '''
        Detects when the cursor is hovering over a button
        '''
        hover = False

        # Getting the mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            
            hover = True
        
        return hover
    
    def erase(self, colour):
        '''
        "Erases" a button
        '''
        height = self.imageDimensions[1]
        width = self.imageDimensions[0]
        center = self.rect.center

        tempRect = pygame.Rect(0, 0, width, height)
        
        tempRect.center = center

        pygame.draw.rect(self.surface, colour, tempRect)
        
    def move(self, colour, x, y):
        '''
        Moves the button
        '''
        self.erase(colour)

        self.oldrectcenter = self.rect.center

        self.rect.center = (x, y)

        self.draw()

    def kingCheck(self):
        '''
        Checks if the piece is supposed to be a king or not, then makes them one if they are
        '''
        if self.name[0] == "b":

            if self.square > 55:

                self.king = True

                if self.selected == False:
                    
                    self.image = self.kingImage
        
        elif self.name[0] == "w":

            if self.square < 8:

                self.king = True

                if self.selected == False:
                    
                    self.image = self.kingImage
            
    def click(self):
        '''
        Detects if the button gets clicked
        '''
        action = False
        #hover = False

        name = self.name

        # Getting the mouse position
        pos = pygame.mouse.get_pos()

        # Check if the mouse is hovering over or clicking the button
        if self.rect.collidepoint(pos):
            #hover = True
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
        return [action, name]
        
    def select(self, list):
        '''
        "Selects" a checker piece
        '''
        self.oldimage = self.image

        if self.king == True:

            self.image = self.selectedKingImg
        
        else:

            self.image = self.selectedImg
        
        self.selected = True
        
        
        list.append(self.name)
    
    def unselect(self, list):
        '''
        Unselects a selected checker piece
        '''
        self.image = self.oldimage
        self.selected = False

        list.clear()

    def is_collide(self, x, y):
        '''
        Checks if a button is colliding with a given tuple of coordinates
        '''
        if self.rect.collidepoint((x, y)) == True:

            return [True, self.name]

        else: 
            
            return [False, self.name]

    def checkerMove(self, square, dict):
        '''
        Moves a checker piece to a given square
        '''
        if square % 2 == 0:

            colour = (151, 77, 0)
        
        elif square % 2 == 1:

            colour = (225, 148, 72)

        # self.move()
        self.erase(colour)
        self.oldrectcenter = self.rect.center
        self.rect.center = self.oldrectcenter
        self.draw()

        # self.move(colour, dict[square][0], dict[square][1])

        if self.name[0] == "b" and self.surface.get_at((dict[square][0], dict[square][1]))[:3] == (253, 231, 70) or self.name[0] == "w":

            self.move(colour, dict[square][0], dict[square][1])
        
            oldSquare = self.square

            self.square = square

        if self.rect.center == self.oldrectcenter:

            return [False]

        else:
            
            return [True, oldSquare]
    
    def checkerMoves(self, silent):
        '''
        Checks or highlights the possible moves of the black pieces

        if silent is True it returns the possible moves and the button's name
        '''
        choices = []

        if self.selected == True or silent == True:

            highlightRect = pygame.Rect(0, 0, 76, 76)

            # If the square is on the left column
            if (self.square + 8) % 8 == 0:
                
                if self.square < 55:

                    # If the piece's only valid move is on an empty square, highlight that square
                    if self.getPixelColour(self.square + 9) == (151, 77, 0):

                        if silent == False:

                            highlightRect.center = self.squareDict[self.square + 9]

                            self.surface.blit(self.highlight, highlightRect)
                        
                        elif silent == True:

                            choices.append("choice")
                        

                if self.square < 46:

                    # Or, if the user's only move is on an enemy square, check if the enemy's piece can be captured, and display that as an option
                    if self.getPixelColour(self.square + 9) == (255, 255, 255):

                            if self.getPixelColour(self.square + 18) == (151, 77, 0):

                                if silent == False:

                                    highlightRect.center = self.squareDict[self.square + 18]

                                    self.surface.blit(self.highlight, highlightRect)

                                elif silent == True:

                                    choices.append("choice")

                if self.king == True:

                    if self.square > 6:

                        # If the piece's only valid move is on an empty square, highlight that square
                        if self.getPixelColour(self.square - 7) == (151, 77, 0):

                            if silent == False:

                                highlightRect.center = self.squareDict[self.square - 7]

                                self.surface.blit(self.highlight, highlightRect)

                            elif silent == True:

                                choices.append("choice")

                        # Or, if the user's only move is on an enemy square, check if the enemy's piece can be captured, and display that as an option
                        elif self.getPixelColour(self.square - 7) == (255, 255, 255):

                            if self.square > 13:

                                if self.getPixelColour(self.square - 14) == (151, 77, 0):

                                    if silent == False:
                                        
                                        highlightRect.center = self.squareDict[self.square - 14]

                                        self.surface.blit(self.highlight, highlightRect)

                                    elif silent == True:

                                        choices.append("choice")

            # If the square is on the right column
            elif (self.square + 1) % 8 == 0:
                
                if self.square < 57:

                    if self.getPixelColour(self.square + 7) == (151, 77, 0):
                    
                        if silent == False:

                            highlightRect.center = self.squareDict[self.square + 7]

                            self.surface.blit(self.highlight, highlightRect)

                        elif silent == True:

                            choices.append("choice")

                if self.square < 50:

                    if self.getPixelColour(self.square + 7) == (255, 255, 255):

                        if self.getPixelColour(self.square + 14) == (151, 77, 0):

                            if silent == False:

                                highlightRect.center = self.squareDict[self.square + 14]

                                self.surface.blit(self.highlight, highlightRect)

                            elif silent == True:

                                choices.append("choice")

                if self.king == True:

                    if self.square > 8:

                        # If the piece's only valid move is on an empty square, highlight that square
                        if self.getPixelColour(self.square - 9) == (151, 77, 0):
                    
                            if silent == False:
                                
                                highlightRect.center = self.squareDict[self.square - 9]

                                self.surface.blit(self.highlight, highlightRect)

                            elif silent == True:

                                choices.append("choice")

                    if self.square > 17:

                        # Or, if the user's only move is on an enemy square, check if the enemy's piece can be captured, and display that as an option
                        if self.getPixelColour(self.square - 9) == (255, 255, 255):

                                if self.getPixelColour(self.square - 18) == (151, 77, 0):

                                    if silent == False:

                                        highlightRect.center = self.squareDict[self.square - 18]

                                        self.surface.blit(self.highlight, highlightRect)

                                    elif silent == True:

                                        choices.append("choice")

            else:
                
                if self.square < 57:

                    if self.getPixelColour(self.square + 7) == (151, 77, 0):

                        if silent == False:

                            highlightRect.center = self.squareDict[self.square + 7]

                            self.surface.blit(self.highlight, highlightRect)
                
                        elif silent == True:

                            choices.append("choice")

                if self.square < 55:

                    if self.getPixelColour(self.square + 9) == (151, 77, 0):

                        if silent == False:

                            highlightRect.center = self.squareDict[self.square + 9]

                            self.surface.blit(self.highlight, highlightRect)

                        elif silent == True:

                            choices.append("choice")

                if self.square < 46:

                    if self.getPixelColour(self.square + 9) == (255, 255, 255):
                    
                        if self.getPixelColour(self.square + 18) == (151, 77, 0):

                            if silent == False:
                            
                                highlightRect.center = self.squareDict[self.square + 18]
                            
                                self.surface.blit(self.highlight, highlightRect)

                            elif silent == True:

                                choices.append("choice")

                if self.square < 50:

                    if self.getPixelColour(self.square + 7) == (255, 255, 255):

                        if self.getPixelColour(self.square + 14) == (151, 77, 0):

                            if silent == False:

                                highlightRect.center = self.squareDict[self.square + 14]

                                self.surface.blit(self.highlight, highlightRect)
                
                            elif silent == True:

                                choices.append("choice")

                if self.king == True:

                    if self.square > 6:

                        if self.getPixelColour(self.square - 7) == (151, 77, 0):

                            if silent == False:

                                highlightRect.center = self.squareDict[self.square - 7]

                                self.surface.blit(self.highlight, highlightRect)

                            elif silent == True:

                                choices.append("choice")

                    if self.square > 8:

                        if self.getPixelColour(self.square - 9) == (151, 77, 0):    

                            if silent == False:

                                highlightRect.center = self.squareDict[self.square - 9]

                                self.surface.blit(self.highlight, highlightRect)
                    
                            elif silent == True:

                                choices.append("choice")

                    if self.square > 17:

                        if self.getPixelColour(self.square - 9) == (255, 255, 255):
                    
                            if self.getPixelColour(self.square - 18) == (151, 77, 0):

                                if silent == False:    

                                    highlightRect.center = self.squareDict[self.square - 18]

                                    self.surface.blit(self.highlight, highlightRect)
                    
                                elif silent == True:

                                    choices.append("choice")

                    if self.square > 13:

                        if self.getPixelColour(self.square - 7) == (255, 255, 255):
                    
                            if self.getPixelColour(self.square - 14) == (151, 77, 0):

                                if silent == False:

                                    highlightRect.center = self.squareDict[self.square - 14]

                                    self.surface.blit(self.highlight, highlightRect)

                                elif silent == True:

                                    choices.append("choice")
        
        if not choices:

            choices.append("None")
        
        return [choices, self.name]

    def enemyMoves(self):
        '''
        Checks the possible moves a piece has

        returns the possible moves and the piece's name
        '''
        choices = []

        if (self.square + 8) % 8 == 0:

            if self.square > 6:

                if self.getPixelColour(self.square - 7) == (151, 77, 0):

                    choices.append(self.square - 7)

            if self.square > 13:

                if self.getPixelColour(self.square - 7) == (0, 0, 0):
            
                    if self.getPixelColour(self.square - 14) == (151, 77, 0):
                    
                        choices.append(self.square - 14)
            
            if self.king == True:

                if self.square < 55:

                    if self.getPixelColour(self.square + 9) == (151, 77, 0):
                    
                        choices.append(self.square + 9)

                if self.square < 46:

                    # Or, if the user's only move is on an enemy square, check if the enemy's piece can be captured, and display that as an option
                    if self.getPixelColour(self.square + 9) == (0, 0, 0):

                        if self.getPixelColour(self.square + 18) == (151, 77, 0):

                            choices.append(self.square + 18)
                

        elif (self.square + 1) % 8 == 0:

            if self.square > 8:

                if self.getPixelColour(self.square - 9) == (151, 77, 0):

                    choices.append(self.square - 9)

            if self.square > 17:

                if self.getPixelColour(self.square - 9) == (0, 0, 0):
            
                    if self.getPixelColour(self.square - 18) == (151, 77, 0):
                    
                        choices.append(self.square - 18)
            
            if self.king == True:

                if self.square < 57:

                    if self.getPixelColour(self.square - 7) == (151, 77, 0):

                        choices.append(self.square - 7)

                if self.square < 50:

                    if self.getPixelColour(self.square - 7) == (0, 0, 0):
            
                        if self.getPixelColour(self.square - 14) == (151, 77, 0):
                    
                            choices.append(self.square - 14)

        else:

            if self.square > 6:

                if self.getPixelColour(self.square - 7) == (151, 77, 0):

                    choices.append(self.square - 7)

            if self.square > 13:
            
                if self.getPixelColour(self.square - 7) == (0, 0, 0):
            
                    if self.getPixelColour(self.square - 14) == (151, 77, 0):
                    
                        choices.append(self.square - 14)
            
            if self.square > 8:

                if self.getPixelColour(self.square - 9) == (151, 77, 0):

                    choices.append(self.square - 9)

            if self.square > 17:

                if self.getPixelColour(self.square - 9) == (0, 0, 0):
            
                    if self.getPixelColour(self.square - 18) == (151, 77, 0):
                    
                        choices.append(self.square - 18)

            if self.king == True:

                if self.square < 55:

                    if self.getPixelColour(self.square + 9) == (151, 77, 0):
                    
                        choices.append(self.square + 9)

                if self.square < 46:

                    # Or, if the user's only move is on an enemy square, check if the enemy's piece can be captured, and display that as an option
                    if self.getPixelColour(self.square + 9) == (0, 0, 0):

                        if self.getPixelColour(self.square + 18) == (151, 77, 0):

                            choices.append(self.square + 18)
                
                if self.square < 57:

                    if self.getPixelColour(self.square + 7) == (151, 77, 0):

                        choices.append(self.square + 7)

                if self.square < 50:

                    if self.getPixelColour(self.square + 7) == (0, 0, 0):
            
                        if self.getPixelColour(self.square + 14) == (151, 77, 0):
                    
                            choices.append(self.square + 14)

        if not choices:

            choices.append("None")

        return [choices, self.name]

    def seeSquare(self):
        '''
        returns the utton's square and name
        '''
        return [self.square, self.name]

    def changeCenter(self):
        '''
        Changes the play button's rect's center
        '''
        self.rect.center = (808 // 2, 608 // 4)

    def isKing(self):
        '''
        Checks if a piece is a king or not
        '''
        if self.king == True:

            return True

        else:

            return False