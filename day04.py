
import numpy as np
import re
from utils import get_input

class Board:
    def __init__(self, grid):
        self.array = np.array(grid).astype('int')
        self.drawn = np.zeros((5,5))
        self.bingo = False
    
    def update(self, draw):
        hits = self.array == draw
        self.drawn[hits] = 1
        if (self.drawn.sum(axis=0) == 5).any() or (self.drawn.sum(axis=1) == 5).any():
            self.bingo = True

    def score(self):
        return (self.array[self.drawn == 0]).sum().item()

    def reset(self):
        self.drawn == 0

def play_bingo(nums, grids):
    boards = [Board(grid) for grid in grids]
    
    bingo = False
    for num in nums:
        for board in boards:
            board.update(num)
            if board.bingo:
                bingo = board.bingo
                break
        if bingo: break

    return num * board.score()

def parse_input(input):
    lines = [line.lstrip() for line in input.splitlines()]
    nums = [int(o) for o in lines[0].split(',')]
    boards = [
        [
            re.split('\D+', row) for row in lines[i:i+5]]
            for i in range(2, len(lines), 6)
        ]
    boards = np.stack([np.array(board, dtype=np.uint8) for board in boards])
    return nums, boards

if __name__ == '__main__':
    example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19

    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7"""
    
    nums, grids = parse_input(example)
    print(play_bingo(nums, grids))
    input = get_input('day04.txt')
    nums, grids = parse_input(input)
    print(play_bingo(nums, grids))