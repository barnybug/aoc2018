#!/usr/bin/env python

from collections import namedtuple
from grid import SparseGrid
from itertools import count, takewhile

move = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
}

class Alt(list):
    def __str__(self):
        return '(%s)' % '|'.join(map(str, self))

class Cat(list):
    def __str__(self):
        return ''.join(map(str, self))

def parse(it):
    it = iter(it)
    parts = Cat()
    s = ''
    term = False
    for c in it:
        if c in move:
            s += c
        elif c == '(':
            if s:
                parts.append(s)
                s = ''
            term = False
            alt = Alt()
            while not term:
                part, term = parse(it)
                alt.append(part)
            parts.append(alt)
        elif c == '|':
            term = False
            break
        elif c == ')':
            term = True
            break

    parts.append(s)
    if len(parts) == 1:
        return parts[0], term
    return parts, term

def traverse(tree, gr, pos):
    result = set()
    if isinstance(tree, Cat):
        for child in tree:
            pos = traverse(child, gr, pos)
        result = pos
    elif isinstance(tree, Alt):
        for child in tree:
            result.update(traverse(child, gr, pos))
    elif isinstance(tree, str):
        result = []
        for p in pos:
            for c in tree:
                dx, dy = move[c]
                gr[(p[0] + dx, p[1] + dy)] = '|' if c in 'EW' else '-'
                p = (p[0] + dx*2, p[1] + dy*2)
            result.append(p)
    return result

def distances(gr):
    queue = [(0, 0)]
    ret = SparseGrid()
    ret[(0, 0)] = 0
    while queue:
        pos = queue.pop()
        s = ret[pos[0]//2, pos[1]//2]
        for dx, dy in move.values():
            c = gr[pos[0] + dx, pos[1] + dy]
            if c not in '-|':
                continue

            d = pos[0]//2 + dx, pos[1]//2 + dy
            if d not in ret:
                ret[d] = s + 1
                queue.append((pos[0] + dx*2, pos[1] + dy*2))
    return ret

def parts(data):
    gr = SparseGrid()
    pos = (0, 0)
    gr[pos] = 'X'
    tree, _ = parse(data)
    traverse(tree, gr, [pos])

    # fill rest
    (minx, miny), (maxx, maxy) = gr.bounds()
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            if x < minx or y < miny or x > maxx or y > maxy:
                gr[x,y] = '#'
            elif x % 2 == 1 and y % 2 == 1:
                gr[x,y] = '#'
            elif x % 2 == 1 or y % 2 == 1:
                if (x, y) not in gr:
                    gr[x,y] = '#'
    print()
    print(gr)

    ds = distances(gr)
    part1 = max(ds.values())
    part2 = sum(1 for d in ds.values() if d >= 1000)
    return part1, part2

def part1(data):
    return parts(data)[0]

if __name__ == '__main__':
    print(parts(open('input20.txt').read()))
