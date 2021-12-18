from itertools import chain
import numpy as np
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
            x = self.x1
            if self.y2 > self.y1:
                y = list(range(self.y1, self.y2 + 1))
            else:
                y = list(range(self.y2, self.y1 + 1))
            return x, y
        
        elif self.is_horizontal():
            y = self.y1
            if self.x2 > self.x1:
                x = list(range(self.x1, self.x2 + 1))
            else:
                x = list(range(self.x2, self.x1 + 1))
            return x, y
        
        else:
            raise ValueError('diagonal line')

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
        x, y = ventline.positions()
        self.map[x, y] += 1

    def count_overlaps(self):
        return (self.map >= 2).sum()

    def map_seabed(self):
        for vl in self.ventlines:
            if vl.is_horizontal() or vl.is_vertical():
                self.update_map(vl)
        return (self.map >= 2).sum()

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

        map = np.zeros((xmax+1, ymax+1))
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
    assert ventlines[5].y1 == 4, 'ventline error'
    seabed = SeaBed.parse(ventlines)
    seabed.map_seabed()
    assert (seabed.map >= 2).sum() == 5
    raw = get_input('day05.txt')
    ventlines = [VentLine.parse(line) for line in raw.splitlines()]
    seabed = SeaBed.parse(ventlines)
    print(seabed.map_seabed())
