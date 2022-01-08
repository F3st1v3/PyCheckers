import pygame

pygame.init()

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

spaceIndex = []
spaceCoords = []

for j in range(4):
    for i in range(4):
        pygame.draw.rect(display_surface, BROWN, (150 * i, 150 * j, 75, 75))
        spaceCoords.append([])
    for i in range(4):
        pygame.draw.rect(display_surface, BROWN, (i * 150 + 75, 150 * j + 75, 75, 75))  
    for i in range(4):
        pygame.draw.rect(display_surface, PEACH, (i * 150 + 75, 150 * j, 75, 75))
    for i in range(4):
        pygame.draw.rect(display_surface, PEACH, (i * 150, j * 150 + 75, 75, 75))


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

    pygame.display.update()