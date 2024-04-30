import pygame
from pygame import Surface

from const import ROW, COLUMN, CELL_SIZE, COLORS

class Grid:
    def __init__(self) -> None:
        self.ROW = ROW
        self.COLUMN = COLUMN
        self.CELL_SIZE = CELL_SIZE
        self.GRID = [[0 for _ in range(self.COLUMN)] for _ in range(self.ROW)]
        self.COLORS = COLORS
    
    def draw(self, screen: Surface):
        for row in range(self.ROW):
            for column in range(self.COLUMN):
                cell_value = self.GRID[row][column]

                # Rectangles | used for positioning, collision detection, and drawing
                cell_rect = pygame.Rect(column * self.CELL_SIZE + 1, row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
                
                # Draw the squares
                pygame.draw.rect(surface=screen, color=self.COLORS[cell_value], rect=cell_rect)