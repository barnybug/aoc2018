#!/usr/bin/env python

import numpy as np

def power_grid(serial):
    gr = np.zeros((300, 300), dtype=np.int8)
    mx, my = np.mgrid[1:301, 1:301]
    rack_id = mx + 10
    power = (rack_id * my + serial) * rack_id
    gr = power // 100 % 10 - 5
    return gr

def max_power(gr, size):
    max_coord = None
    max_total = -10
    for x in range(300-size):
        for y in range(300-size):
            total = gr[x:x+size, y:y+size].sum()
            if total > max_total:
                max_total = total
                max_coord = (x+1, y+1)

    return max_coord, max_total

def part1(serial):
    gr = power_grid(serial)
    return max_power(gr, 3)[0]

def part2(serial):
    gr = power_grid(serial)
    max_size = None
    max_coord = None
    max_total = -10
    for size in range(1, 300):
        print(size)
        coord, total = max_power(gr, size)
        if total > max_total:
            max_coord = coord
            max_total = total
            max_size = size

    return max_coord[0], max_coord[1], max_size

if __name__ == '__main__':
    print(part1(1308))
    print(part2(1308))
