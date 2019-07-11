# import pygame library so we can use it!
import pygame
from pygame.locals import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources
# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (235, 235, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (65, 231, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# game code that needs to run only once
# rectangle variables
rectX = 50
rectY = 50
rectXSpeed = 1.1
rectYSpeed = .8

# fill entire screen with color
gameSurface.fill(BLACK)


# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame
    # clear display (redraw background)
    # gameSurface.fill(BLACK)

    # update
    # add speed to position
    rectX += rectXSpeed
    rectY += rectYSpeed

    # check if the rectangle has gone off the screen
    # doesn't use centers. There is a better way to do this with pygame rect object
    if rectX > display_width or rectX < 1:
        rectXSpeed *= -1
    if rectY > display_height or rectY < 1:
        rectYSpeed *= -1

    # draw
    pygame.draw.rect(gameSurface, WHITE, [rectX, rectY, 50, 50])



    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
