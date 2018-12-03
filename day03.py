#!/usr/bin/env python

from collections import Counter
import re

fabric = Counter()

bits = [
    [int(x) for x in re.findall(r'(\d+)', line)]
    for line in open('input03.txt')
]

for cid, x, y, w, h in bits:
    fabric.update((i, j) for i in range(x, x+w) for j in range(y, y+h))

print(sum(1 for _, c in fabric.items() if c > 1))

for cid, x, y, w, h in bits:
    counts = [fabric[(i, j)] for i in range(x, x+w) for j in range(y, y+h)]
    if all(count == 1 for count in counts):
        print(cid)
