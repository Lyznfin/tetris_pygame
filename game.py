from grid import Grid
from blocks import *
from const import CELL_OFFSET

import random
from pygame import Surface

class Game:
    def __init__(self) -> None:
        self.grid: Grid = Grid()
        self.blocks: list[Block] = self.get_all_blocks()
        self.cur_block: Block = self.get_random_block()
        self.next_block: Block = self.get_random_block()
        self.game_over: bool = False
        self.score: int = 0

    def update_score(self, lines_cleared: int, move_down: int) -> None:
        match lines_cleared:
            case 1:
                self.score += 100
            case 2:
                self.score += 300
            case 3:
                self.score += 500
        self.score += move_down
        
    def get_random_block(self) -> Block:
        if len(self.blocks) == 0:
            self.blocks = self.get_all_blocks()

        block: Block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def get_all_blocks(self) -> list[Block]:
        return [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    
    def move_block(self, direction: str) -> None:
        match direction:
            case "left":
                self.cur_block.move(0, -1)
                self.cur_block.move(0, 1) if not self.block_inside() or not self.block_fits() else None
            case "down":
                self.cur_block.move(1, 0)
                if not self.block_inside() or not self.block_fits():
                    self.cur_block.move(-1, 0)
                    self.lock_block()
            case "right":
                self.cur_block.move(0, 1)
                self.cur_block.move(0, -1) if not self.block_inside() or not self.block_fits() else None

    def lock_block(self) -> None:
        tiles = self.cur_block.get_cell_positions()
        for position in tiles:
            self.grid.GRID[position.row][position.column] = self.cur_block.id
        self.cur_block = self.next_block
        self.next_block = self.get_random_block()
        lines_cleared = self.grid.clear_rows()
        self.update_score(lines_cleared, 0)
        if not self.block_fits():
            self.game_over = True

    def block_fits(self) -> bool:
        tiles = self.cur_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):
                return False
        return True

    def rotate_block(self, rotation: str) -> None:
        match rotation:
            case "right":
                self.cur_block.rotate(1)
                self.cur_block.rotate(-1) if not self.block_inside() or not self.block_fits() else None
            case "left":
                self.cur_block.rotate(-1)
                self.cur_block.rotate(1) if not self.block_inside() or not self.block_fits() else None

    def block_inside(self) -> bool:
        tiles = self.cur_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen: Surface) -> None:
        self.grid.draw(screen)
        self.cur_block.draw(screen, CELL_OFFSET)
        self.next_block.draw(screen, 275)

    def reset(self) -> None:
        self.grid.set_grid()
        self.blocks = self.get_all_blocks()
        self.game_over = False
        self.score = 0