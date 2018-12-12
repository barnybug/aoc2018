#!/usr/bin/env python

from itertools import count

def str_to_bits(s):
    return sum(2**i for i, v in enumerate(s) if v == '#')

def bits_to_str(b):
    return ''.join('#' if c & 1 else '.' for c in bit_iter(b))

def bit_iter(b, mask=1):
    while b:
        yield b & mask
        b >>= 1

def bit_sum(state, offset):
    return sum(b * i for b, i in zip(bit_iter(state), count(-offset)))

def bit_count(b):
    return sum(bit_iter(b))

def part1(filename, n):
    lines = open(filename)
    initial = next(lines).strip().replace('initial state: ', '')
    initial = str_to_bits(initial)
    offset = 10
    initial <<= offset

    next(lines) # blank line

    masks = [0]*32
    for line in lines:
        rule, result = line.strip().split(' => ')
        masks[str_to_bits(rule)] = 1 if result == '#' else 0

    state = initial
    for i in range(n):
        previous = state
        state = sum(
            masks[p] << (j+2)
            for j, p in enumerate(bit_iter(previous, 31))
        )
        if state == previous*2:
            # doubling cycle detected - shortcut
            return bit_sum(state, offset) + bit_count(state) * (n-i-1)

    return bit_sum(state, offset)

if __name__ == '__main__':
    print(part1('input12.txt', 20))
    print(part1('input12.txt', 50000000000))
