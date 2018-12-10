#!/usr/bin/env python

import collections
import re
import sys

from grid import SparseGrid

class Point(collections.namedtuple('Point', 'x y dx dy')):
    pass

def parts(filename):
    lines = open(filename)
    pos = [Point(*map(int, re.findall(r'(-?\d+)', line))) for line in lines]

    last_grid = None
    for j in range(0, sys.maxsize):
        pos = [Point(x+dx, y+dy, dx, dy) for i, (x, y, dx, dy) in enumerate(pos)]
        grid = SparseGrid({(p.x, p.y): '#' for p in pos})
        if last_grid and grid.area() > last_grid.area():
            break
        last_grid = grid
    print(last_grid)
    return j

if __name__ == '__main__':
    print(parts('input10.txt'))
