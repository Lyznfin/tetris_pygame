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
                case pygame.K_a | pygame.K_LEFT:
                    game.move_block("left")
                case pygame.K_s | pygame.K_DOWN:
                    game.move_block("down")
                case pygame.K_d | pygame.K_RIGHT:
                    game.move_block("right")
                case pygame.K_q:
                    game.rotate_block("left")
                case pygame.K_e:
                    game.rotate_block("right")
    
    game.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(60)