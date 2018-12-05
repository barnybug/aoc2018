#!/usr/bin/env python

import re
import string

def calc(inp):
	pair = '|'.join(c + c.upper() + '|' + c.upper() + c for c in string.ascii_lowercase)

	n = re.sub(pair, '', inp)
	while n != inp:
		inp = n
		n = re.sub(pair, '', inp)
	return inp

def part1(inp):
	return len(calc(inp))

def part2(inp):
	lens = []
	for c in string.ascii_lowercase:
		ainp = inp.replace(c, '').replace(c.upper(), '')
		lens.append(part1(ainp))

	return min(lens)

if __name__ == '__main__':
	inp = open('input05.txt').read()
	# this cannot alter the calculation, but avoids duplicate work
	inp = calc(inp)
	print(part1(inp))
	print(part2(inp))