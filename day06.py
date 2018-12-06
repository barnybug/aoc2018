#!/usr/bin/env python

import numpy as np
from collections import Counter
import re
import string

symbols = '.'+string.ascii_lowercase

def symbol(i):
    return symbols[i+1]

def part1(filename):
    coords = np.loadtxt(filename, delimiter=', ').astype(int)
    # coords = [tuple(map(int, re.findall(r'\d+', line))) for line in open(filename)]
    mx = max(x for x, _ in coords)+1
    my = max(y for _, y in coords)+1
    grid = np.full((my, mx), -1)

    for x in range(mx):
        for y in range(my):
            ds = np.absolute(coords - (x, y)).sum(1)
            m = ds.min()
            if (ds == m).sum() == 1:
                grid[y][x] = np.argmin(ds)

    # for row in grid:
    #     print(''.join(symbol(r) for r in row))

    # remove borders
    border = set()
    border.update(grid[0][x] for x in range(mx))
    border.update(grid[my-1][x] for x in range(mx))
    border.update(grid[y][0] for y in range(my))
    border.update(grid[y][mx-1] for y in range(my))

    counts = Counter(c for row in grid for c in row if c != -1)
    for b in border:
        del counts[b]
    return counts.most_common(1)[0][1]

def part2(filename, below):
    coords = [tuple(map(int, re.findall(r'\d+', line))) for line in open(filename)]
    mx = max(x for x, _ in coords)+1
    my = max(y for _, y in coords)+1
    grid = [[0 for x in range(mx)] for y in range(my)]

    for x in range(mx):
        for y in range(my):
            for ci, (cx, cy) in enumerate(coords):
                d = abs(cx-x) + abs(cy-y)
                grid[y][x] += d

    return sum(1 for x in range(mx) for y in range(my) if grid[y][x] < below)

if __name__ == '__main__':
    print(part1('input06.txt'))
    print(part2('input06.txt', 10000))
