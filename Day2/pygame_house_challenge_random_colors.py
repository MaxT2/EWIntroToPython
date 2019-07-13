"""
Challenge: Draw a house!
"""

# import pygame library so we can use it!
import random

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
FPS = 1

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# add theses colors to your pygame_setup.py file if you want to have
# them for your next project
LIGHT_BLUE = (100, 200, 255)
DARK_GREEN = (16, 161, 0)
YELLOW = (255, 255, 0)



# fill entire screen with color before game starts
game_surface.fill(WHITE)

# TEACHER - Boolean for adding ground and sky
background = True

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

    # TEACHER
    if background:
        #draw ground
        rect(game_surface, DARK_GREEN, [(0, 500), (width, 300)])
        # draw sky
        rect(game_surface, LIGHT_BLUE, [(0, 0), (width, 500)])
        # draw sun
        circle(game_surface, YELLOW, (0, 0), 125)


    # setup random colors
    # create one then use CTR + D
    c_1 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    c_2 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    c_3 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    c_4 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    c_5 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    c_6 = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))



    # base rectangle
    rect(game_surface, c_1, [(200, 350), (800, 400)])

    # roof Triangle
    polygon(game_surface, c_2, [(200, 350), (1000, 350), (600,100)])

    # window 1
    rect(game_surface, c_3, [(275, 475), (175, 175)])

    # window 2
    rect(game_surface, c_4, [(750, 475), (175, 175)])

    # door
    rect(game_surface, c_5, [(525, 450), (150, 300)])

    # door knob
    circle(game_surface, c_6, (630, 600), 25)


    # lastly: update and redraw entire screen
    pygame.display.flip()
