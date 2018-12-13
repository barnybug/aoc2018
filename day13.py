#!/usr/bin/env python

import re

def draw(track, carts):
    out = [list(row) for row in track]
    for cart in carts:
        out[cart.y][cart.x] = cart.d
    return '\n'.join(''.join(row) for row in out)

dirs = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}

turn_forward = {
    '^': '>',
    '>': '^',
    '<': 'v',
    'v': '<',
}

turn_backward = {
    '^': '<',
    '<': '^',
    '>': 'v',
    'v': '>',
}

turn_intersect = {
    '^': '<^>',
    'v': '>v<',
    '<': 'v<^',
    '>': '^>v',
}

class Cart(object):
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.intersects = 0

    def next(self):
        dx, dy = dirs[self.d]
        return self.x+dx, self.y+dy

    def move(self):
        self.x, self.y = self.next()

    def turn_forward(self):
        self.d = turn_forward[self.d]

    def turn_backward(self):
        self.d = turn_backward[self.d]

    def intersection(self):
        self.d = turn_intersect[self.d][self.intersects]
        self.intersects = (self.intersects + 1) % 3

    def __str__(self):
        return '(%d, %d, %s)' % (self.x, self.y, self.d)


def run(filename, stop):
    track = [line.strip('\n') for line in open(filename)]
    mx = max(map(len, track))
    my = len(track)

    carts = []
    for y, row in enumerate(track):
        for x, d in enumerate(row):
            if d not in '^v<>':
                continue
            carts.append(Cart(x, y, d))
    track = [row.replace('>', '-').replace('v', '|').replace('^', '|').replace('<', '-') for row in track]
    # print()
    # print(draw(track, carts))

    while True:
        carts.sort(key=lambda cart: (cart.y, cart.x))
        positions = set((cart.x, cart.y) for cart in carts)
        dead = []
        for cart in carts:
            if cart in dead:
                continue

            positions.remove((cart.x, cart.y))
            nx, ny = cart.next()
            if (nx, ny) in positions:
                if stop:
                    return '%d,%d' % (nx, ny) # crash!
                else:
                    # eliminate and continue
                    other = next(cart for cart in carts if cart.x == nx and cart.y == ny)
                    dead.extend([cart, other])
                    positions.remove((nx, ny))
                    continue

            # move
            cart.move()
            positions.add((cart.x, cart.y))

            # calculate new direction
            t = track[ny][nx]
            if t == '/':
                cart.turn_forward()
            elif t == '\\':
                cart.turn_backward()
            elif t == '+':
                cart.intersection()

        if not stop and dead:
            carts = [cart for cart in carts if cart not in dead]
            if len(carts) == 1:
                return '%d,%d' % (carts[0].x, carts[0].y)

        # print()
        # print(draw(track, carts))

def part1(filename):
    return run(filename, stop=True)

def part2(filename):
    return run(filename, stop=False)

if __name__ == '__main__':
    print(part1('input13.txt'))
    print(part2('input13.txt'))
