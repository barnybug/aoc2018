#!/usr/bin/env python

import numpy as np

def part1(data):
    lines = data.split('\n')
    pts = [np.array(list(map(int, line.split(',')))) for line in lines]
    groups = []
    for pt in pts:
        matches = []
        not_matches = []
        for group in groups:
            ds = np.abs(group - pt).sum(axis=1)
            if np.sum(ds <= 3):
                matches.append(group)
            else:
                not_matches.append(group)

        if matches:
            supergroup = [p for group in matches for p in group] + [pt]
            matches = [np.array(supergroup)]
        else:
            matches = [np.array([pt])]
        groups = matches + not_matches
    return len(groups)

def part2(filename):
    pass

if __name__ == '__main__':
    print(part1(open('input25.txt').read()))
    # print(part2('input_.txt'))
