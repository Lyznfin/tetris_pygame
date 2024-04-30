import pygame

class Grid:
    def __init__(self) -> None:
        self.ROW = 20
        self.COLUMN = 10
        self.CELL_SIZE = 30
        self.GRID = [[0 for _ in range(self.COLUMN)] for _ in range(self.ROW)]
        self.COLORS = self.get_cell_colors()

    def get_cell_colors(self):
        DARK_GREY = (26, 31, 40)
        GREEN = (47, 230, 23)
        RED = (232, 18, 18)
        ORANGE = (226, 116, 17)
        YELLOW = (237, 234, 4)
        PURPLE = (166, 0, 247)
        CYAN = (21, 204, 209)
        BLUE = (13, 64, 216)

        return [DARK_GREY, GREEN, RED, ORANGE, YELLOW, PURPLE, CYAN, BLUE]
    
    def draw(self, screen):
        for row in range(self.ROW):
            for column in range(self.COLUMN):
                cell_value = self.GRID[row][column]

                # Rectangles | used for positioning, collision detection, and drawing
                cell_rect = pygame.Rect(column * self.CELL_SIZE + 1, row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
                
                # Draw the squares
                pygame.draw.rect(surface=screen, color=self.COLORS[cell_value], rect=cell_rect)