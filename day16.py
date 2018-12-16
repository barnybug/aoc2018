#!/usr/bin/env python

import itertools
import operator
from collections import namedtuple, Counter

class Op(namedtuple('Op', 'op a b')):
    def __call__(self, va, vb):
        return self.op(self.a(va), self.b(vb))

def parts(filename, part2=True):
    regs = [0, 0, 0, 0]
    def reg(i):
        return regs[i]
    def value(i):
        return i
    ops = [
        Op(operator.add, reg, reg),
        Op(operator.add, reg, value),
        Op(operator.mul, reg, reg),
        Op(operator.mul, reg, value),
        Op(operator.and_, reg, reg),
        Op(operator.and_, reg, value),
        Op(operator.or_, reg, reg),
        Op(operator.or_, reg, value),
        Op(lambda a, b: a, reg, value),
        Op(lambda a, b: a, value, value),
        Op(lambda a, b: int(a > b), value, reg),
        Op(lambda a, b: int(a > b), reg, value),
        Op(lambda a, b: int(a > b), reg, reg),
        Op(lambda a, b: int(a == b), value, reg),
        Op(lambda a, b: int(a == b), reg, value),
        Op(lambda a, b: int(a == b), reg, reg),
    ]

    samples = [list(group) for k, group in itertools.groupby(open(filename), lambda s: s != '\n') if k]
    c = Counter()

    op_guesses = {
        i: list(ops)
        for i in range(16)
    }
    op_mapping = {}
    for sample in samples:
        if not sample[0].startswith('Before'):
            continue

        before = list(map(int, sample[0][9:19].split(', ')))
        args = list(map(int, sample[1].split(' ')))
        after = list(map(int, sample[2][9:19].split(', ')))

        regs.clear()
        regs.extend(before)
        opcode, arga, argb, outc = args

        candidates = set()
        for op in op_guesses[opcode]:
            result = op(arga, argb)
            if after[outc] == result:
                candidates.add(op)
        op_guesses[opcode] = candidates
        c[len(candidates)] += 1

    part1 = sum(i for n, i in c.items() if n >= 3)
    if not part2:
        return part1
    while op_guesses:
        decided = [code for code, s in op_guesses.items() if len(s) == 1]
        for code in decided:
            op = list(op_guesses.pop(code))[0]
            op_mapping[code] = op
            for c, s in op_guesses.items():
                if op in s:
                    s.remove(op)

    program = samples[-1]
    regs.clear()
    regs.extend([0, 0, 0, 0])
    for line in program:
        code, a, b, c = map(int, line.split())
        regs[c] = op_mapping[code](a, b)

    part2 = regs[0]
    return part1, part2

if __name__ == '__main__':
    print(parts('input16.txt'))
