import pygame
from pygame import Surface

from position import Position
from const import CELL_SIZE, COLORS

class Block:
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells = {}
        self.rotation_state = 0

    def draw(self, screen: Surface) -> None:
        tiles: list[Position] = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * CELL_SIZE + 1, tile.row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(surface=screen, color=COLORS[self.id], rect=tile_rect)