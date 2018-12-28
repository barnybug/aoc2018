#!/usr/bin/env python

import numpy as np
from collections import namedtuple, deque
import sys

ROCKY = 0
WET = 1
NARROW = 2

EMPTY = 0
TORCH = 1
CLIMB = 2

ALLOWED = [
    [CLIMB, TORCH],
    [EMPTY, CLIMB],
    [EMPTY, TORCH],
]

SWITCHES = {
    (ROCKY, TORCH): CLIMB,
    (ROCKY, CLIMB): TORCH,
    (WET, CLIMB): EMPTY,
    (WET, EMPTY): CLIMB,
    (NARROW, TORCH): EMPTY,
    (NARROW, EMPTY): TORCH,
}

class State(namedtuple('State', 'x y tool time')):
    pass

def generate(depth, target, size):
    geologic = np.zeros(size, int)
    erosion = np.zeros(size, int)
    for (x,y), _ in np.ndenumerate(geologic):
        if x == 0 or y == 0:
            geologic[x, y] = x * 16807 + y * 48271
        elif (x, y) != target:
            geologic[x, y] = erosion[x-1, y] * erosion[x, y-1]
        erosion[x, y] = (geologic[x, y] + depth) % 20183

    cave = erosion % 3
    return cave

def part1(depth, target):
    size = (target[0]+1, target[1]+1)
    cave = generate(depth, target, size)
    return cave.sum()

def part2(depth, target):
    size = (target[0]+10, target[1]+10)
    cave = generate(depth, target, size)

    s = State(0, 0, TORCH, 0)
    quickest = {}
    states = deque([s])
    best = sys.maxsize

    while states:
        s = states.popleft()
        if s.time >= best:
            continue
        if (s.x, s.y) == target and s.tool == TORCH:
            best = s.time
            continue

        # moves
        for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx = s.x + x
            ny = s.y + y
            if nx < 0 or ny < 0 or nx >= size[0] or ny >= size[1]:
                continue
            if s.tool not in ALLOWED[cave[nx, ny]]:
                continue

            key = (nx, ny, s.tool)
            if key not in quickest or quickest[key] > s.time+1:
                quickest[key] = s.time+1
                states.append(s._replace(x=nx, y=ny, time=s.time+1))

        # switch tool
        ntool = SWITCHES[cave[s.x, s.y], s.tool]
        key = (s.x, s.y, ntool)
        if key not in quickest or quickest[key] > s.time+7:
            quickest[key] = s.time+7
            states.append(s._replace(tool=ntool, time=s.time+7))

    return best

if __name__ == '__main__':
    depth = 7305
    target = (13,734)
    print(part1(depth, target))
    print(part2(depth, target))
