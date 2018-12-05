#!/usr/bin/env python

from collections import Counter

def twothrees(s):
    c = Counter(s)
    return (int(2 in c.values()), int(3 in c.values()))

def part1(lines):
    cs = [twothrees(line) for line in lines]
    twos, threes = [sum(x) for x in (zip(*cs))]
    return twos*threes

def part2(lines):
    c = Counter()
    c.update(
        line[0:i]+'_'+line[i+1:]
        for line in lines
        for i in range(len(line)-1)
    )
    return c.most_common(1)[0][0].replace('_', '').strip()

if __name__ == '__main__':
    lines = open('input02.txt')
    print(part1(lines))
    print(part2(lines))
