#!/usr/bin/env python

import itertools

def answer1():
	return sum(int(line) for line in open('input1.txt'))
print(answer1())

def answer2():
	inputs = [int(line) for line in open('input1.txt')]
	seen = set([0])
	pos = 0
	for n in itertools.cycle(inputs):
		pos += n
		if pos in seen:
			return pos
		seen.add(pos)

print(answer2())