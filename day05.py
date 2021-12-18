from itertools import chain
import numpy as np
from numpy.lib.shape_base import row_stack
from utils import get_input

class VentLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def positions(self):
        
        if self.is_vertical():
            col = self.x1
            row = sorted([self.y1, self.y2])
            row = list(range(row[0], row[1] + 1))
            return row, col
        
        if self.is_horizontal():
            col = sorted([self.x1, self.x2])
            row = self.y1
            col = list(range(col[0], col[1] + 1))
            return row, col
        
        else:
            if self.x1 > self.x2:
                col = list(range(self.x1, self.x2 - 1, -1))
            else:
                col = list(range(self.x1, self.x2 + 1))
            if self.y1 > self.y2:
                row = list(range(self.y1, self.y2 - 1, -1))
            else:
                row = list(range(self.y1, self.y2 + 1))
            return row, col

    @staticmethod
    def parse(raw):
        start, end = raw.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        coords = [int(o) for o in (x1, y1, x2, y2)]
        return VentLine(*coords)

class SeaBed:
    def __init__(self, map, ventlines):
        self.map = map
        self.ventlines = ventlines

    def update_map(self, ventline):
        row, col = ventline.positions()
        self.map[row, col] += 1

    def count_overlaps(self):
        return (self.map >= 2).sum()

    def map_seabed(self, ignore_diags = True):

        self.reset()

        if ignore_diags:
            for vl in self.ventlines:
                if vl.is_horizontal() or vl.is_vertical():
                    self.update_map(vl)
        
        else:
            for vl in self.ventlines:
                self.update_map(vl)

    def danger_spots(self):
        if self.map.sum() == 0:
            raise AssertionError ('Seabed unmapped')

        return (self.map >= 2).sum()
    
    def reset(self):
        self.map[:] = 0

    @staticmethod
    def parse(ventlines):
        
        xs = chain.from_iterable([
            [vl.x1 for vl in ventlines],
            [vl.x2 for vl in ventlines]
        ])
        
        ys = chain.from_iterable([
            [vl.y1 for vl in ventlines],
            [vl.y2 for vl in ventlines]
        ])

        xmax = max(xs)
        ymax = max(ys)

        map = np.zeros((xmax+2, ymax+2))
        return SeaBed(map, ventlines)
        
if __name__ == '__main__':
    example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    ventlines = [VentLine.parse(line) for line in example.splitlines()]
    assert ventlines[0].x1 == 0, 'ventline error'
    seabed = SeaBed.parse(ventlines)
    seabed.map_seabed()
    assert seabed.danger_spots() == 5
    seabed.map_seabed(ignore_diags=False)
    assert seabed.danger_spots() == 12
    raw = get_input('day05.txt')
    ventlines = [VentLine.parse(line) for line in raw.splitlines()]
    seabed = SeaBed.parse(ventlines)
    print(seabed.map.shape)
    seabed.map_seabed(ignore_diags=False)
    print(seabed.danger_spots())
