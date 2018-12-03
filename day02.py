#!/usr/bin/env python

from collections import Counter

def twothrees(s):
    c = Counter(s)
    return (int(2 in c.values()), int(3 in c.values()))

def answer1():
    cs = [twothrees(line) for line in open('day02.txt')]
    twos, threes = [sum(x) for x in (zip(*cs))]
    print(twos*threes)

def answer2():
    c = Counter()
    c.update(
        line[0:i]+'_'+line[i+1:]
        for line in open('day02.txt')
        for i in range(len(line)-1)
    )
    print(c.most_common(1)[0][0].replace('_', '').strip())

answer1()
answer2()