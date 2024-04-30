import pygame, sys

from const import WIDTH, HEIGHT, LIGTH_GREY
from game import Game

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(LIGTH_GREY)

pygame.display.set_caption("Tetris")

CLOCK = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a:
                    game.move_block("left")
                case pygame.K_s:
                    game.move_block("down")
                case pygame.K_d:
                    game.move_block("right")
    
    game.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(60)