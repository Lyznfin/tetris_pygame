import pygame
from pygame import Surface

from const import ROW, COLUMN, CELL_SIZE, COLORS

class Grid:
    def __init__(self) -> None:
        self.set_grid()

    def set_grid(self) -> None:
        self.GRID = self.initialize_grid()
    
    def initialize_grid(self) -> list[list[int]]:
        return [[0 for _ in range(COLUMN)] for _ in range(ROW)]

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
    
    def is_row_completed(self, row: int) -> bool:
        for column in range(COLUMN):
            if self.is_empty(row, column):
                return False
        return True
    
    def pop_row(self, row: int) -> None:
        for column in range(COLUMN):
            self.GRID[row][column] = 0

    def move_row(self, row: int, n_rows: int) -> None:
        for column in range(COLUMN):
            self.GRID[row+n_rows][column] = self.GRID[row][column]
            self.GRID[row][column] = 0

    def clear_rows(self) -> int:
        completed = 0
        for row in range(ROW - 1, 0, -1):
            if self.is_row_completed(row):
                self.pop_row(row)
                completed += 1
            elif completed > 0:
                self.move_row(row, completed)
        return completed