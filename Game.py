'''
Author: F3st1v3
Date: January 25 2022
Program name: Checkers
Description: Simulates checkers
'''

# Importing pygame
import pygame

from ButtonClass import *

# Initializing pygame
pygame.init()

# Defining black as black's RGB value
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (153, 76, 0)
YELLOW = (255, 255, 0)
PINK = (255, 133, 133)
ORANGE = (255, 178, 102)

# Defining x as 640
x = 800

# Defining y as 480
y = 600

# Defining display_surface as the display surface object of the dimensions x, y
display_surface = pygame.display.set_mode((x, y))



# Loading images

playImg = pygame.image.load("Resources/playImg.png").convert_alpha()
playImgHover = pygame.image.load("Resources/playImgHover2.jpg").convert_alpha()
boardImg = pygame.image.load("Resources/board.png").convert_alpha()
'''
optionsImg = pygame.image.load("options.png").convert_alpha()
backImg = pygame.image.load("back.png").convert_alpha()
'''

# Creating button instances
playButton = Button(x / 2, y / 2, playImg, 0.4)
playButtonHover = Button(x / 2, y / 2, playImgHover, 0.5)

# Setting the pygame window name
pygame.display.set_caption("Checkers")

# Defining font as the system font with the size of 72
font = pygame.font.SysFont('Corbel', 72)

# Defining img as the rendered text "Victor" (My name) in black
img = font.render("Checkers", True, BROWN)

# Defining imgRect as img's rect
imgRect = img.get_rect()

# Setting the center of imgRect
imgRect.center = (x // 2, y // 4)

scene = "menu"

def game():

    display_surface.fill(ORANGE)

    display_surface.blit(boardImg, (100, 0))

def menu():

    # Making the background white
    display_surface.fill(ORANGE)

    # Displaying img on the screen
    display_surface.blit(img, imgRect)

    if playButton.draw(display_surface):
        
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

    # pygame.draw.rect(display_surface, BROWN, playButton)
