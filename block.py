import pygame
from pygame import Surface

from position import Position
from const import CELL_SIZE, COLORS

class Block:
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells = {}
        self.CELL_SIZE = CELL_SIZE
        self.rotation_state = 0
        self.COLORS = COLORS

    def draw(self, screen: Surface):
        tiles: list[Position] = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.CELL_SIZE + 1, tile.row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
            pygame.draw.rect(surface=screen, color=self.COLORS[self.id], rect=tile_rect)