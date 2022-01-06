'''
Author: Victor Yustein
Date: November 23, 2021
Program name: Name display
Description: Displays my name in the middle of the screen using pygame
'''

# Importing pygame
import pygame

from ButtonClass import *
# Initializing pygame
pygame.init()

# Loading images
playImg = pygame.image.load("play.png").convert_alpha()
optionsImg = pygame.image.load("options.png").convert_alpha()
backImg = pygame.image.load("back.png").convert_alpha()
singleImg = pygame.image.load("single.png").convert_alpha()
multiIMg = pygame.image.load("multi.png").convert_alpha()

# Defining black as black's RGB value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (153, 76, 0)
YELLOW = (255, 255, 0)
PINK = (255, 133, 133)
ORANGE = (255, 178, 102)

# Defining x as 640
x = 600

# Defining y as 480
y = 600

# Defining display_surface as the display surface object of the dimensions x, y
display_surface = pygame.display.set_mode((x, y))

'''
# Creating a button class
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # Getting the mouse position
        pos = pygame.mouse.get_pos()

        # Check if the mouse is hovering over or clicking the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button
        display_surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
'''

# Creating button instances
playButton = Button(x / 2, y / 4, playImg, 1)

# Setting the pygame window name
pygame.display.set_caption("Checkers")

# Defining font as the system font with the size of 24
font = pygame.font.SysFont('Corbel', 72)

# Defining img as the rendered text "Victor" (My name) in black
img = font.render("Checkers", True, BROWN)

# Defining imgRect as img's rect
imgRect = img.get_rect()

# Setting the center of imgRect
imgRect.center = (x // 2, y // 4)


def menu():
    # Making the background white
    display_surface.fill(ORANGE)

    # Displaying img on the screen
    display_surface.blit(img, imgRect)

    # Updating the screen
    pygame.display.flip()

    if playButton.draw(display_surface):
        # Event
        return 0


def selection():
    return 0


# Starting an infinite loop
while True:

    menu()

    # Stopping the program if pygame.event.get() returns pygame.QUIT
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

    pygame.draw.rect(display_surface, BROWN, playButton)

    # Draws the surface object to the screen
    pygame.display.update()
