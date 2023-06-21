#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# uriartej

"""
Imports the the game demo and executes the main function.
"""

import sys
import pygame
import game

if __name__ == "__main__":
    # TODO: Prepare and run the game
    pygame.init()

    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Game")


    sys.exit(0)
