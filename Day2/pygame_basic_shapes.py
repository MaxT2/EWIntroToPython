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

    # update stuff here

    # draw stuff here

    # draw all basic shapes

    # line (surface, color, (x,y),(x,y),width(optional))
    line(game_surface, BLUE, (600, 400), (600, 500), 10)

    # circle
    # circle(surface,color,(x,y), radius, width(optional)
    circle(game_surface, BLUE, (300, 200), 100)
    # do another!
    circle(game_surface, BLUE, (900, 200), 100)

    # rectangle
    # rect(surface, color, ((x,y), (width,height), width(optional))
    rect(game_surface, BLUE, [(300, 600), (600, 100)])

    # polygon
    # polygon(surface, color,(x1,y1,x2,y2))
    polygon(game_surface, BLUE, [(0, 100), (100, 50), (0, 0)])

    # lastly: update and redraw entire screen
    pygame.display.flip()
