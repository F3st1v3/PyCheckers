from numpy.lib.function_base import disp
import pygame
from ButtonClass import *
pygame.init()

class a:

    def __init__(self):
        pass
    def pos(self, x, y):

        print((x, y))

myObj = a()

BROWN = (153, 76, 0)
YELLOW = (255, 255, 0)
PINK = (255, 133, 133)
PEACH = (225, 148, 72)
ORANGE = (255, 178, 102)

x = 600

# Defining y as 480
y = 600

display_surface = pygame.display.set_mode((x, y))


squarePixels = [75, 150, 225, 300, 375, 450, 525, 600]

display_surface.fill(ORANGE)



for j in range(4):
    for i in range(4):
        pygame.draw.rect(display_surface, BROWN, (150 * i, 150 * j, 75, 75))
    for i in range(4):
        pygame.draw.rect(display_surface, BROWN, (i * 150 + 75, 150 * j + 75, 75, 75))  
    for i in range(4):
        pygame.draw.rect(display_surface, PEACH, (i * 150 + 75, 150 * j, 75, 75))
    for i in range(4):
        pygame.draw.rect(display_surface, PEACH, (i * 150, j * 150 + 75, 75, 75))

spaceIndex = []
spaceCoords = []

for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76 + 76 + 76 + 76 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76 + 76 + 76 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76 + 76 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76 + 76])
for i in range(1, 9):
    spaceCoords.append([76 * i - 38+ 104, 38 + 76])
for i in range(1, 9): 
    spaceCoords.append([76 * i - 38 + 104, 38])

for i in range(64):
    spaceIndex.append(i)

spaces = {0: [142, 570], 1: [218, 570], 2: [294, 570], 3: [370, 570], 4: [446, 570], 5: [522, 570], 6: [598, 570], 7: [674, 570], 8: [142, 494], 9: [218, 494], 10: [294, 494], 11: [370, 494], 12: [446, 494], 13: [522, 494], 14: [598, 494], 15: [674, 494], 16: [142, 418], 17: [218, 418], 18: [294, 418], 19: [370, 418], 20: [446, 418], 21: [522, 418], 22: [598, 418], 23: [674, 418], 24: [142, 342], 25: [218, 342], 26: [294, 342], 27: [370, 342], 28: [446, 342], 29: [522, 342], 30: [598, 342], 31: [674, 342], 32: [142, 266], 33: [218, 266], 34: [294, 266], 35: [370, 266], 36: [446, 266], 37: [522, 266], 38: [598, 266], 39: [674, 266], 40: [142, 190], 41: [218, 190], 42: [294, 190], 43: [370, 190], 44: [446, 190], 45: [522, 190], 46: [598, 190], 47: [674, 190], 48: [142, 114], 49: [218, 114], 50: [294, 114], 51: [370, 114], 52: [446, 114], 53: [522, 114], 54: [598, 114], 55: [674, 114], 56: [142, 38], 57: [218, 38], 58: [294, 38], 59: [370, 38], 60: [446, 38], 61: [522, 38], 62: [598, 38], 63: [674, 38]}

print(list(spaces.values()))

playImg = pygame.image.load("Resources/playImg.png").convert_alpha()
button1 = Button(400, 200, playImg, 1)
button1.draw(display_surface)

while True:

    #pos = pygame.mouse.get_pos()

    #print(pos)
    if button1.click()[0]:

        print("asdsa")

        button1.move(display_surface, BROWN, 100, 200)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

    pygame.display.update()