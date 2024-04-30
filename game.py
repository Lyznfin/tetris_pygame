from grid import Grid
from blocks import *

import random
from pygame import Surface

class Game:
    def __init__(self) -> None:
        self.grid: Grid = Grid()
        self.blocks: list[Block] = self.get_all_blocks()
        self.cur_block: Block = self.get_random_block()
        self.next_block: Block = self.get_random_block()
        
    def get_random_block(self) -> Block:
        if len(self.blocks) == 0:
            self.blocks = self.get_all_blocks()

        block: Block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def get_all_blocks(self) -> list[Block]:
        return [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
    
    def move_block(self, direction: str):
        match direction:
            case "left":
                self.cur_block.move(0, -1)
            case "right":
                self.cur_block.move(0, 1)
            case "down":
                self.cur_block.move(1, 0)

    def draw(self, screen: Surface):
        self.grid.draw(screen)
        self.cur_block.draw(screen)