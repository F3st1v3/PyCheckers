'''
This code is NOT mine, and is posted at
https://github.com/russs123/pygame_tutorials/blob/main/Button/button.py
It's included here because I'm using the class, similarly to how one
uses a module. All credit for the code goes to the developer.
I have only modified a few things to better fit my needs.
'''

import pygame

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #hover = False

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

        #if not self.rect.collidepoint(pos):
            #hover = False
        

        # Draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return [action]

    def hover(self):
            
        hover = False

        # Getting the mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            
            hover = True
        
        return [hover]



