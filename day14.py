#!/usr/bin/env python

def part1(recipes):
    seq = '37'
    a, b = 0, 1
    while len(seq) < recipes+10:
        s = int(seq[a]) + int(seq[b])
        seq += str(s)
        a = (a + int(seq[a])+1) % len(seq)
        b = (b + int(seq[b])+1) % len(seq)
    return seq[recipes:recipes+10]

def part2(recipes):
    seq = '37'
    a, b = 0, 1
    i = -1
    l = len(recipes)
    while i == -1:
        s = int(seq[a]) + int(seq[b])
        seq += str(s)
        a = (a + int(seq[a])+1) % len(seq)
        b = (b + int(seq[b])+1) % len(seq)
        if seq[-l:] == recipes:
            i = len(seq)-l
            break
        if seq[-l-1:-1] == recipes:
            i = len(seq)-l-1
            break

        if len(seq) % 1000000 == 0:
            print(len(seq))

    return i

if __name__ == '__main__':
    print(part1(580741))
    print(part2('580741'))
