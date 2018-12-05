#!/usr/bin/env python

from collections import Counter
import re

fabric = Counter()

def parse(lines):
    return [
        [int(x) for x in re.findall(r'(\d+)', line)]
        for line in lines
    ]

def part1(lines):
    bits = parse(lines)
    for cid, x, y, w, h in bits:
        fabric.update((i, j) for i in range(x, x+w) for j in range(y, y+h))

    return sum(1 for _, c in fabric.items() if c > 1)

def part2(lines):
    bits = parse(lines)
    for cid, x, y, w, h in bits:
        counts = [fabric[(i, j)] for i in range(x, x+w) for j in range(y, y+h)]
        if all(count == 1 for count in counts):
            return cid

if __name__ == '__main__':
    lines = list(open('input03.txt'))
    print(part1(lines))
    print(part2(lines))
    