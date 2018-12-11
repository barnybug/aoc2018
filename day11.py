#!/usr/bin/env python

import numpy as np

def power_grid(serial):
    gr = np.zeros((300, 300), dtype=np.int8)
    mx, my = np.mgrid[1:301, 1:301]
    rack_id = mx + 10
    power = (rack_id * my + serial) * rack_id
    gr = power // 100 % 10 - 5
    return gr

def part1(serial):
    gr = power_grid(serial)
    cs = gr.cumsum(0).cumsum(1)
    size = 3
    totals = cs[size:,size:] + cs[:-size,:-size] - cs[size:,:-size] - cs[:-size,size:]
    x, y = np.unravel_index(
        totals.argmax(), totals.shape)
    return (x+2, y+2)

def part2(serial):
    gr = power_grid(serial)
    cs = gr.cumsum(0).cumsum(1)

    answer = None
    max_total = 0
    for size in range(1, 300):
        totals = cs[size:,size:] + cs[:-size,:-size] - cs[size:,:-size] - cs[:-size,size:]
        if totals.max() > max_total:
            x, y = np.unravel_index(
                totals.argmax(), totals.shape)
            answer = (x+2, y+2, size)
            max_total = totals.max()

    return answer

if __name__ == '__main__':
    print(part1(1308))
    print(part2(1308))
