#!/usr/bin/env python

import collections
import re
import sys

class Point(collections.namedtuple('Point', 'x y dx dy')):
    pass

def area(pos):
    minx = min(p.x for p in pos)
    maxx = max(p.x for p in pos)
    miny = min(p.y for p in pos)
    maxy = max(p.y for p in pos)
    return (maxx-minx)*(maxy-miny)

def draw(pos):
    minx = min(p.x for p in pos)
    maxx = max(p.x for p in pos)
    miny = min(p.y for p in pos)
    maxy = max(p.y for p in pos)

    grid = ['.' * (maxx-minx) for i in range(miny, maxy+1)]
    for p in pos:
        grid[p.y-miny] = grid[p.y-miny][:p.x-minx] + '#' + grid[p.y-miny][p.x-minx+1:]
    return '\n'.join(grid)

def parts(filename):
    lines = open(filename)
    pos = [Point(*map(int, re.findall(r'(-?\d+)', line))) for line in lines]

    last_pos = None
    for j in range(0, sys.maxsize):
        last_pos = pos
        pos = [Point(x+dx, y+dy, dx, dy) for i, (x, y, dx, dy) in enumerate(pos)]
        if last_pos and area(pos) > area(last_pos):
            break
    print(draw(last_pos))
    return j

if __name__ == '__main__':
    print(parts('input10.txt'))
