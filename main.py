import pygame, sys

# Initialize pygame
pygame.init()

# Create game windows
WIDTH = 450
HEIGTH = 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Tetris")

# Create clock to control framerate | like timeDelta or sum
CLOCK = pygame.time.Clock()

# Making color
DARK_BLUE = (44, 44, 162) # RGB something something

# Fill screen with a color
SCREEN.fill(DARK_BLUE)

# Create game loop
while True:
    # Event handling
    for event in pygame.event.get():

        # Check for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Updates display
    pygame.display.update()

    # Framerate | run how many times per second
    CLOCK.tick(90)