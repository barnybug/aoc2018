#!/usr/bin/env python

from collections import Counter

from grid import SparseGrid

def part1(filename, runs):
    orig = SparseGrid.parse(open(filename))
    grid = orig

    t = 0
    period = 0
    while t < runs:
        ngrid = SparseGrid()
        for xy in orig.range():
            co = Counter(grid.adjacent(xy))
            c = grid[xy]
            if c == '.':
                if co['|'] >= 3:
                    ngrid[xy] = '|'
            elif c == '|':
                ngrid[xy] = '#' if co['#'] >= 3 else '|'
            elif c == '#':
                if co['#'] >= 1 and co['|'] >= 1:
                    ngrid[xy] = '#'

        grid = ngrid
        co = grid.count()
        val = co['|'] * co['#']
        if val == 210000:
            if period:
                t += ((runs - t) // period) * period
            else:
                period += 1
        elif period:
            period += 1

        t += 1

    return val

if __name__ == '__main__':
    print(part1('input18.txt', 10))
    print(part1('input18.txt', 1000000000))
