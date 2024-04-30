import pygame, sys

from const import WIDTH, HEIGHT, DARK_GREY, WHITE, LIGTH_GREY
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 40)
score_inteface = title_font.render("Score", True, (255, 255, 255))
next_interface = title_font.render("Next", True, (255, 255, 255))
game_over_interface = title_font.render("Its Over", True, (255, 255, 255))

score_rect = pygame.Rect(325, 55, 170, 60)
next_rect = pygame.Rect(325, 215, 170, 180)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(LIGTH_GREY)

pygame.display.set_caption("Tetris")

CLOCK = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game.game_over:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a | pygame.K_LEFT:
                        game.move_block("left")
                    case pygame.K_s | pygame.K_DOWN:
                        game.move_block("down")
                        game.update_score(0, 1)
                    case pygame.K_d | pygame.K_RIGHT:
                        game.move_block("right")
                    case pygame.K_q:
                        game.rotate_block("left")
                    case pygame.K_e:
                        game.rotate_block("right")
            if event.type == GAME_UPDATE:
                game.move_block("down")
        if game.game_over:
            if event.type == pygame.KEYDOWN:
                game.reset()
    
    score_value_interface = title_font.render(str(game.score), True, (255, 255, 255))

    SCREEN.blit(score_inteface, (370, 20, 50, 50))
    SCREEN.blit(next_interface, (380, 180, 50, 50))

    pygame.draw.rect(SCREEN, DARK_GREY, score_rect, 0, 10)
    SCREEN.blit(score_value_interface, score_value_interface.get_rect(
    centerx = score_rect.centerx, centery = score_rect.centery
    ))
    pygame.draw.rect(SCREEN, DARK_GREY, next_rect, 0, 10)

    game.draw(SCREEN)

    if game.game_over:
        SCREEN.blit(game_over_interface, (350, 450, 50, 50))

    pygame.display.update()
    CLOCK.tick(60)