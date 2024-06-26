import pygame
from pygame import Surface

from position import Position
from const import CELL_SIZE, COLORS

class Block:
    def __init__(self, id: int) -> None:
        self.id = id
        
        self.cells = {}
        self.rotation_state = 0

        self.row_offset = 0
        self.column_offset = 0
        self.move(0, 3)

    def draw(self, screen: Surface, offset: int) -> None:
        tiles: list[Position] = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * CELL_SIZE + offset, tile.row * CELL_SIZE + offset, CELL_SIZE - 1, CELL_SIZE - 1)
            pygame.draw.rect(surface=screen, color=COLORS[self.id], rect=tile_rect)

    def move(self, rows: int, columns: int) -> None:
        self.row_offset += rows
        self.column_offset += columns

    def rotate(self, value: int):
        self.rotation_state += value
        if self.rotation_state >= len(self.cells):
            self.rotation_state = 0
        if self.rotation_state < 0:
            self.rotation_state = 3

    def get_cell_positions(self):
        tiles: list[Position] = self.cells[self.rotation_state]
        # moved_tiles: list[Position] = [Position(position.row + self.row_offset, position.column + self.column_offset) for position in tiles]
        moved_tiles: list[Position] = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles