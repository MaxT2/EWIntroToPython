# import pygame library so we can use it!
import pygame
import random
from pygame.locals import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

gameSurface = pygame.display.set_mode((display_width, display_height))

# setup resources
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (235, 235, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (65, 231, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# setup for text
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("Python Rocks", True, GREEN)

# main game loop
# when running is True game loop will run
running = True
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # do game stuff
    # fill entire screen with a color
    gameSurface.fill(WHITE)

    # rcolor = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
    # screen.fill(rcolor)

    # drawing shapes
    # (displayReference,color,location,size)
    pygame.draw.circle(gameSurface, BLUE, (300, 300), 75)
    pygame.draw.circle(gameSurface, BLUE, (700, 300), 75)
    # line(surface,color, (x1,y1),(x2,y2),thickness)
    pygame.draw.line(gameSurface, BLUE, (400, 700), (600, 700), 20)
    # rect(surface,color,(x,y,width,height))
    pygame.draw.rect(gameSurface, BLUE, (500, 550, 50, 50))
    # sufrace.blit(text, [x,y])
    gameSurface.blit(text, [350, 850])

    # extras
    # rect vs square
    # polygon - teach in house challenge instead?

    # update and redraw entire screen
    pygame.display.flip()
    # delay to slow random change. Wont work for a game
    pygame.time.delay(300)
