#!/usr/bin/env python

import itertools

def part1(lines):
	return sum(int(line) for line in lines)

def part2(lines):
	inputs = [int(line) for line in lines]
	seen = set([0])
	pos = 0
	for n in itertools.cycle(inputs):
		pos += n
		if pos in seen:
			return pos
		seen.add(pos)

if __name__ == '__main__':
	print(part1(open('input01.txt')))
	print(part2(open('input01.txt')))