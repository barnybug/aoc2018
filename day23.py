#!/usr/bin/env python

import re
from collections import namedtuple, deque

import numpy as np

class Bot(namedtuple('Bot', 'x y z r')):
    def distance(self, a):
        return abs(self.x - a[0]) + abs(self.y - a[1]) + abs(self.z - a[2])

def parse(filename):
    return [
        Bot(*map(int, re.findall(r'-?\d+', line)))
        for line in open(filename)
    ]

def part1(filename):
    bots = parse(filename)
    strongest = max(bots, key=lambda bot: bot.r)
    in_range = sum(1 for bot in bots if strongest.distance(bot) <= strongest.r)
    return in_range

def part2(filename):
    bots = parse(filename)
    octs = np.array([bot[:3] for bot in bots])
    rs = np.array([bot[3] for bot in bots])

    # work out bounds and set cube in centre, radius extending to bounds
    mi, mx = octs.min(axis=0), octs.max(axis=0)
    p = ((mi + mx) / 2).astype(int)
    r = np.ceil((octs.max(axis=0) - octs.min(axis=0)).max() / 2).astype(int)

    cubes = deque([(p, r, 0)])
    results = []

    pbest = -1
    while cubes:
        p, r, ir = cubes.popleft()
        if ir <= pbest:
            continue # cull anything already beaten
        if r == 1:
            r = 0
            xr, yr, zr = zip(p - 1, p) # slice 2x2x2 into 8 unit-cubes
        else:
            r = np.ceil(r / 2).astype(int)
            xr, yr, zr = zip(p - r, p + r) # slice in 8 half cubes

        cands = []
        best = pbest
        for x in xr:
            for y in yr:
                for z in zr:
                    pn = np.array([x, y, z])
                    # calculate intersection of the octahedra with the cube pn, radius r
                    n = np.clip(octs, pn - r, pn + r - 1)
                    # clip octahedra to cube faces
                    mh = np.abs(n - octs).sum(axis=1)
                    # calculate manhattan distance to octahedra
                    ir = (mh <= rs).sum()
                    # if less than of equal to range, this intersects with the cube
                    if ir > best:
                        if r == 0:
                            pbest = ir
                        cands = [(pn, r, ir)]
                        best = ir
                    elif ir == best:
                        # when tied, all cubes should be searched
                        cands.append((pn, r, ir))
        if r == 0:
            # only need the lowest by manhattan (which is our search order, depth first)
            best = cands[0]
        else:
            cubes.extendleft(cands)

    return np.abs(best[0]).sum()

if __name__ == '__main__':
    print(part1('input23.txt'))
    print(part2('input23.txt'))
