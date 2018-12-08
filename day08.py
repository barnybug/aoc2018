#!/usr/bin/env python

import itertools

class Node(object):
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def __repr__(self):
        return '[%s %s]' % (self.metadata, self.children)

    def all_meta(self):
        return self.metadata + [x for c in self.children for x in c.all_meta()]

    def value(self):
        if not self.children:
            return sum(self.metadata)
        return sum(
            self.children[m-1].value()
            for m in self.metadata
            if m >= 1 and m <= len(self.children))

def parse(it):
    nc = next(it)
    nm = next(it)
    children = [parse(it) for c in range(nc)]
    metadata = list(itertools.islice(it, nm))
    return Node(children, metadata)

def parse_file(filename):
    ins = map(int, open(filename).read().split())
    return parse(ins)

def part1(filename):
    tree = parse_file(filename)
    return sum(tree.all_meta())

def part2(filename):
    tree = parse_file(filename)
    return tree.value()

if __name__ == '__main__':
    print(part1('input08.txt'))
    print(part2('input08.txt'))
