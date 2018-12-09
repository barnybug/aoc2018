#!/usr/bin/env python

from collections import deque

def part1(players, marbles):
    circle = deque()
    circle.append(0)
    scores = [0] * players
    for marble in range(1, marbles+1):
        if marble % 23 == 0:
            circle.rotate(-7)
            scores[marble % players] += marble + circle.pop()
        else:
            circle.rotate(2)
            circle.append(marble)

    return max(scores)

part2 = part1

if __name__ == '__main__':
    print(part1(476, 71657))
    print(part2(476, 71657*100))
