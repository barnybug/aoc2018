#!/usr/bin/env python

import itertools
from itertools import count
import operator
from collections import namedtuple, Counter

class Bin(namedtuple('Bin', 'op a b')):
    def __str__(self):
        return '%s %s %s' % (self.a, self.op, self.b)

def translate(filename):
    lines = list(open(filename))
    r = {}
    ops = {
        'addr': lambda a, b: Bin('+', r[a], r[b]),
        'addi': lambda a, b: Bin('+', r[a], b),
        'mulr': lambda a, b: Bin('*', r[a], r[b]),
        'muli': lambda a, b: Bin('*', r[a], b),
        'banr': lambda a, b: Bin('&', r[a], r[b]),
        'bani': lambda a, b: Bin('&', r[a], b),
        'borr': lambda a, b: Bin('|', r[a], r[b]),
        'bori': lambda a, b: Bin('|', r[a], b),
        'setr': lambda a, b: r[a],
        'seti': lambda a, b: a,
        'gtir': lambda a, b: 'int(%d > %s)' % (a, r[b]),
        'gtri': lambda a, b: 'int(%s > %d)' % (r[a], b),
        'gtrr': lambda a, b: 'int(%s > %s)' % (r[a], r[b]),
        'eqir': lambda a, b: 'int(%d == %s)' % (a, r[b]),
        'eqri': lambda a, b: 'int(%s == %d)' % (r[a], b),
        'eqrr': lambda a, b: 'int(%s == %s)' % (r[a], r[b]),
    }
    ip = [int(line[4:]) for line in lines if line.startswith('#ip')][0]
    c = iter('abcde')
    for i in range(0, 6):
        if i == ip:
            r[i] = 'ip'
        else:
            r[i] = next(c)
    def parse(args):
        op, a, b, c = ops[args[0]], int(args[1]), int(args[2]), int(args[3])
        return op(a, b), r[c]
    
    def inline_pc_reads(code):
        for pc, (op, c) in enumerate(code):
            if isinstance(op, Bin):
                if op.a == 'ip':
                    op = op._replace(a=pc)
                if op.b == 'ip':
                    op = op._replace(b=pc)
                code[pc] = (op, c)
        return code

    def simplify_constants(code):
        for pc, (op, c) in enumerate(code):
            if isinstance(op, Bin) and isinstance(op.a, int) and isinstance(op.b, int):
                code[pc] = (eval(str(op)), c)
        return code

    def format_code(rhs, c):
        if c == 'ip':
            if isinstance(rhs, int):
                return 'goto %d' % (rhs+1)
            if isinstance(rhs, Bin) and rhs.op == '+' and isinstance(rhs.b, int):
                rhs = rhs._replace(b=rhs.b+1)
                return 'goto %s' % (rhs, )
            return 'goto %s + 1' % (rhs, )
        if isinstance(rhs, Bin) and rhs.a == c:
            return '%s %s= %s' % (c, rhs.op, rhs.b)
        return '%s = %s' % (c, rhs)
    parsed = [
        parse(line.split()) for line in lines if line[0] != '#'
    ]
    code = inline_pc_reads(parsed)
    code = simplify_constants(parsed)
    code = [
        format_code(*args) for args in parsed
    ]
    return code

# code = translate(filename)
# for pc, line in enumerate(code):
#     print(line + ' # %d' % pc)
# e = 123 # 0
# e &= 456 # 1
# e = int(e == 72) # 2
# goto e + 4 # 3
# goto 1 # 4
# e = 0 # 5
# c = e | 65536 # 6
# e = 9010242 # 7
# b = c & 255 # 8
# e += b # 9
# e &= 16777215 # 10
# e *= 65899 # 11
# e &= 16777215 # 12
# b = int(256 > c) # 13
# goto b + 15 # 14
# goto 17 # 15
# goto 28 # 16
# b = 0 # 17
# d = b + 1 # 18
# d *= 256 # 19
# d = int(d > c) # 20
# goto d + 22 # 21
# goto 24 # 22
# goto 26 # 23
# b += 1 # 24
# goto 18 # 25
# c = b # 26
# goto 8 # 27
# b = int(e == a) # 28
# goto b + 30 # 29
# goto 6 # 30

def seq():
    e = 0
    while True:
        c = e | 65536
        e = 9010242
        while True:
            b = c & 255
            e += b
            e &= 16777215
            e *= 65899
            e &= 16777215
            if c < 256:
                yield e
                break

            c //= 256

def part1():
    return next(seq())

def part2():
    seen = set()
    uniq = []
    for e in seq():
        if e in seen:
            break
        uniq.append(e)
        seen.add(e)
    return(uniq[-1])

if __name__ == '__main__':
    print(part1())
    print(part2())
