import pygame
from pygame import Surface

from const import ROW, COLUMN, CELL_SIZE, COLORS

class Grid:
    def __init__(self) -> None:
        self.GRID = [[0 for _ in range(COLUMN)] for _ in range(ROW)]
    
    def draw(self, screen: Surface) -> None:
        for row in range(ROW):
            for column in range(COLUMN):
                cell_value = self.GRID[row][column]
                cell_rect = pygame.Rect(column * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1)
                pygame.draw.rect(surface=screen, color=COLORS[cell_value], rect=cell_rect)

    def is_inside(self, row: int, column: int) -> bool:
        if row >= 0 and row < ROW and column >= 0 and column < COLUMN:
            return True
        return False
    
    def is_empty(self, row: int, column: int) -> bool:
        if self.GRID[row][column] == 0:
            return True
        return False