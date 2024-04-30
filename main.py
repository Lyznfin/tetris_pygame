import pygame, sys
from grid import Grid

# Initialize pygame
pygame.init()

# Create game windows
WIDTH = 300
HEIGTH = 600 # Maintain a 2:1 ratio
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Tetris")

# Create clock to control framerate | like timeDelta or sum
CLOCK = pygame.time.Clock()

# Making color
DARK_BLUE = (44, 44, 162) # RGB something something

# Fill screen with a color
SCREEN.fill(DARK_BLUE)

GAME_GRID = Grid()
GAME_GRID.GRID[0][0] = 2
GAME_GRID.GRID[0][1] = 2
GAME_GRID.GRID[1][0] = 2
GAME_GRID.GRID[1][1] = 2

# Create game loop
while True:
    # Event handling
    for event in pygame.event.get():

        # Check for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    GAME_GRID.draw(SCREEN)

    # Updates display
    pygame.display.update()

    # Framerate | run how many times per second
    CLOCK.tick(60)

# Grid
# Tetris grid is 20 rows (HEIGTH) and 10 column (WIDTH)
# Its a 2D list (col * heigth)
# Empty = 0
# Color = unique num id