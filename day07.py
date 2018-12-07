#!/usr/bin/env python

from collections import defaultdict
import re
import string

def part1(filename):
    rules = [re.findall(' ([A-Z]) ', line) for line in open(filename)]
    remain = set(a for p in rules for a in p)
    order = ''

    while remain:
        ready = set(remain) - set(b for _, b in rules)
        now = sorted(ready)[0]
        order += now
        remain.remove(now)
        rules = [(a, b) for a, b in rules if a != now]

    return order

def test_cost(c):
    return ord(c)-ord('A')+1

def input_cost(c):
    return ord(c)-ord('A')+61

def part2(filename, cost, max_workers):
    rules = [re.findall(' ([A-Z]) ', line) for line in open(filename)]
    remain = set(a for p in rules for a in p)
    t = 0
    work = []
    started = set()

    while remain:
        done = set(c for c, td in work if t == td)
        if done:
            remain -= done
            rules = [(a, b) for a, b in rules if a not in done]
            work = [(c, td) for c, td in work if c not in done]

        ready = set(remain) - set(b for _, b in rules) - started
        idle = max_workers - len(work)
        for _, start in zip(range(idle), ready):
            started.update(start)
            work.append((start, t+cost(start)))

        if remain:
            t += 1

    return t

if __name__ == '__main__':
    print(part1('input07.txt'))
    print(part2('input07.txt', input_cost, 5))
