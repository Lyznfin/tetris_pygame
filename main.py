import pygame, sys

from grid import Grid
from const import WIDTH, HEIGHT, LIGTH_GREY
from blocks import *

# Initialize pygame
pygame.init()

# Create game windows
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Create clock to control framerate | like timeDelta or sum
CLOCK = pygame.time.Clock()

SCREEN.fill(LIGTH_GREY)

GAME_GRID = Grid()
# GAME_GRID.GRID[1][1] = 4
# GAME_GRID.GRID[1][2] = 4
# GAME_GRID.GRID[2][1] = 4
# GAME_GRID.GRID[2][2] = 4

GRID_BLOCK = LBlock()

# Create game loop
while True:
    # Event handling
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    GAME_GRID.draw(SCREEN)
    GRID_BLOCK.draw(SCREEN)
    # Updates display
    pygame.display.update()

    # Framerate | run how many times per second
    CLOCK.tick(60)