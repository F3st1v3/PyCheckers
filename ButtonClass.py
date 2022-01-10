'''
This code is NOT mine, and is posted at
https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py
It's included here because I'm using the class, similarly to how one
uses a module. All credit for the idea, some of the code, and the structure
goes to the developer. I have only modified a few things to better fit my needs.
'''

from os import name
import pygame
from pygame import display

class Button:
    def __init__(self, x, y, image, scale, kingImage=False, name="None"):
        
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
        if kingImage != False:

            self.kingImage = kingImage

    def draw(self, surface):
        
           
            # Draw button
            surface.blit(self.image, (self.rect.x, self.rect.y))

    def hover(self):


            hover = False

            # Getting the mouse position
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
            
                hover = True
        
            return hover
    
    def erase(self, surface, colour):

        height = self.imageDimensions[1]
        width = self.imageDimensions[0]
        center = self.rect.center

        tempRect = pygame.Rect(0, 0, width, height)
        
        tempRect.center = center

        pygame.draw.rect(surface, colour, tempRect)
        
    def move(self, surface, colour, x, y):

        self.erase(surface, colour)

        self.rect.center = (x, y)

        self.draw(surface)

    def kingCheck(self):

        if self.king == True:
            
            self.image = self.kingImage
            
    def click(self):

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
        
    def select(self, image, list):

        self.oldimage = self.image
        self.image = image
        self.selected = True
        
        list.append(self.name)
    
    def unselect(self, list):

        self.image = self.oldimage
        self.selected = False

        list.clear()

    def is_collide(self, x, y):

        if self.rect.collidepoint((x, y)) == True:

            return [True, self.name]

        else: 
            
            return [False, self.name]
    
    def checkerMove(self, square, dict, surface):

        if square % 2 == 0:

            colour = (153, 76, 0)
        
        elif square % 2 == 1:

            colour = (225, 148, 72)

        self.move(surface, colour, dict[square][0], dict[square][1])