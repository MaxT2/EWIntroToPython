"""
This file is the basis of all pygame drawings and games.
Once students have writen this file they will copy it
and use it as the base of all other pygame projects
"""

# import pygame library so we can use it!
import pygame
# import draw methods for drawing!
from pygame.draw import *

# game code that needs to run only once

# initialize pygame code
pygame.init()

# setup display size variables
width = 1200
height = 800

# create game surface (the screen we will draw onto)
game_surface = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Window Caption!')

# setup framerate stuff
clock = pygame.time.Clock()
FPS = 10

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# fill entire screen with color before game starts
game_surface.fill(WHITE)


# main game loop. Loops until running = False.
running = True
while running == True:
    # get input events and respond to them
    # go over each event that happened
    for event in pygame.event.get():
        # if the event is us closing the game window
        if event.type == pygame.QUIT:
            # stop our loop
            running = False

    # game code that repeats every frame
    # store and print current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print("X = ", mouse_x, "Y = ", mouse_y)

    # limit the frame rate of your game
    clock.tick(FPS)

    # update stuff

    # draw stuff

    # lastly: update and redraw entire screen
    pygame.display.flip()
