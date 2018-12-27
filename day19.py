#!/usr/bin/env python

import itertools
import operator
from collections import namedtuple, Counter

class Op(namedtuple('Op', 'op a b')):
    def __call__(self, va, vb):
        return self.op(self.a(va), self.b(vb))

def translate(filename):
    lines = list(open(filename))
    ops = {
        'addr': lambda a, b: 'r%d + r%d' % (a, b),
        'addi': lambda a, b: 'r%d + %d' % (a, b),
        'mulr': lambda a, b: 'r%d * r%d' % (a, b),
        'muli': lambda a, b: 'r%d * %d' % (a, b),
        'banr': lambda a, b: 'r%d & r%d' % (a, b),
        'bani': lambda a, b: 'r%d & %d' % (a, b),
        'borr': lambda a, b: 'r%d | r%d' % (a, b),
        'bori': lambda a, b: 'r%d | %d' % (a, b),
        'setr': lambda a, b: 'r%d' % a,
        'seti': lambda a, b: a,
        'gtir': lambda a, b: 'int(%d > r%d)' % (a, b),
        'gtri': lambda a, b: 'int(r%d > %d)' % (a, b),
        'gtrr': lambda a, b: 'int(r%d > r%d)' % (a, b),
        'eqir': lambda a, b: 'int(%d == r%d)' % (a, b),
        'eqri': lambda a, b: 'int(r%d == %d)' % (a, b),
        'eqrr': lambda a, b: 'int(r%d == r%d)' % (a, b),
    }
    ip = [int(line[4:]) for line in lines if line.startswith('#ip')][0]
    def parse(args):
        op, a, b, c = ops[args[0]], int(args[1]), int(args[2]), int(args[3])
        return 'r%d = %s' % (c, op(a, b))
    code = [
        parse(line.split()) for line in lines if line[0] != '#'
    ]
    return code

def parts(filename, r0):
    # code = translate(filename)
    # for pc, c in enumerate(code):
    #     print(c.replace('r2', 'pc') + ' # %d' % pc)
    r1, pc, r3, r4, r5 = 0, 0, 0, 0, 0
    hot = Counter()

    while True:
        hot[pc] += 1
        if pc == 0:
            pc = 16 # 0
        elif pc == 1:
            r1 = 1 # 1
            r3 = 1 # 2
            r4 = r1 * r3 # 3
            r4 = int(r4 == r5) # 4
            pc = r4 + 5 # 5
        elif pc == 3:
            while r1 <= r5:
                if r5 % r1 == 0:
                    r0 += r1
                r1 += 1 # 12
            print(pc, hot)
            return r0
        elif pc == 6:
            r3 += 1 # 8
            r4 = int(r3 > r5) # 9
            pc = 10 + r4 # 10
        elif pc == 7:
            r0 = r1 + r0 # 7
            r3 = r3 + 1 # 8
            r4 = int(r3 > r5) # 9
            pc = pc + r4 # 10
        elif pc == 8:
            r3 = r3 + 1 # 8
            r4 = int(r3 > r5) # 9
            pc += r4 + 2 # 10
        elif pc == 11:
            pc = 2 # 11
        elif pc == 12:
            r1 = r1 + 1 # 12
            r4 = int(r1 > r5) # 13
            pc += 2 + r4 # 14
        elif pc == 13:
            r4 = int(r1 > r5) # 13
        elif pc == 14:
            pc += r4 # 14
        elif pc == 17:
            r5 += 2 # 17
            r5 = r5 * r5 # 18
            r5 = 19 * r5 # 19
            pc += 2
        elif pc == 20:
            r5 = r5 * 11 # 20
            r4 += 5 # 21
            r4 = r4 * 22 + 9 # 22
            r5 = r5 + r4 # 24
            pc += r0 + 5 # 25
        elif pc == 26:
            pc = 0 # 26
        elif pc == 27:
            r4 = 32 * 14 * 30 * (29 +  27 * 28) # 29
            r5 += r4 # 33
            r0 = 0 # 34
            pc = 0
        pc += 1

def part1(filename):
    return parts(filename, 0)

def part2(filename):
    return parts(filename, 1)

if __name__ == '__main__':
    print(part1('input19.txt'))
    print(part2('input19.txt'))
