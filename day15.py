#!/usr/bin/env python

import itertools

class Combatant(object):
    def __init__(self, hitpoints=200):
        self.hitpoints = hitpoints

    def __repr__(self):
        return '%s(%d)' % (str(self), self.hitpoints)

class Goblin(Combatant):
    def __str__(self):
        return 'G'

class Elf(Combatant):
    def __str__(self):
        return 'E'

def print_board(board):
    xs = [x for x,y in board.keys()]
    ys = [x for x,y in board.keys()]
    print('\n'.join(
        ''.join(
            str(board[x,y]) if (x,y) in board else '.'
            for x in range(min(ys), max(ys)+1)
        )
        for y in range(min(ys), max(ys)+1)
    ))


def create_board(lines):
    board = {}
    for y, line in enumerate(lines):
        line = line.strip()
        for x, c in enumerate(line):
            if c == 'G':
                c = Goblin()
            elif c == 'E':
                c = Elf()
            if c != '.':
                board[x,y] = c
    return board

def enemy(a, b):
    if isinstance(a, Goblin) and isinstance(b, Elf):
        return True
    if isinstance(a, Elf) and isinstance(b, Goblin):
        return True
    return False

def adjacent(pos):
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

def unoccupied(pos, board):
    for p in adjacent(pos):
        if p not in board:
            yield p

def neighbours(pos, board):
    for p in adjacent(pos):
        if p in board:
            yield p, board[p]

def get_targets(unit, board):
    return [p for p, c in board.items() if enemy(unit, c)]

def reading_order(p):
    return (p[1], p[0])

def choose_target(pos, targets, board):
    in_range = [i for p in targets for i in unoccupied(p, board)]
    if pos in in_range:
        return pos

    covered = {}
    work = list(unoccupied(pos, board))
    reached = []
    i = 1
    while work and not reached:
        next_work = []
        for p in work:
            if p in in_range:
                reached.append(p)
            if p not in covered:
                covered[p] = i
                next_work.extend(unoccupied(p, board))
        work = next_work
        i += 1

    reached.sort(key=reading_order)
    return reached[0] if reached else None

def run(lines, elf_power, raise_on_elf_death=False):
    board = create_board(lines)
    elf_losses = 0
    gameover = False
    rounds = 0
    while not gameover:
        # get reading order of units
        units = sorted(
            (((x, y), c) for (x, y), c in board.items() if isinstance(c, Combatant)),
            key=lambda a: reading_order(a[0]))
        for pos, unit in units:
            if unit.hitpoints <= 0:
                continue
            attack = [(p, c) for p, c in neighbours(pos, board) if enemy(unit, c)]
            if not attack:
                # movement
                targets = get_targets(unit, board)
                if not targets:
                    gameover = True
                    break

                chosen = choose_target(pos, targets, board)
                if not chosen:
                    continue # this unit cannot do anything

                step = choose_target(chosen, [pos], board)
                del board[pos]
                board[step] = unit
                pos = step

            # recheck attach
            attacks = sorted(
                ((p, c) for p, c in neighbours(pos, board) if enemy(unit, c)),
                key=lambda a: (a[1].hitpoints, reading_order(a[0])))
            if attacks:
                p, foe = attacks[0]
                # print('%r at %s attacks %r at %s' % (unit, pos, foe, p))
                power = 3 if isinstance(unit, Goblin) else elf_power
                foe.hitpoints -= power
                if foe.hitpoints <= 0:
                    # dead
                    if raise_on_elf_death and isinstance(foe, Elf):
                        raise ElfDied()
                    del board[p]

        if not gameover:
            rounds += 1

    total_hitpoints = sum(c.hitpoints for c in board.values() if isinstance(c, Combatant))
    print_board(board)
    return rounds * total_hitpoints

class ElfDied(Exception):
    pass

def part1(lines):
    return run(lines, 3)

def part2(lines):
    lines = list(lines)
    for elf_power in itertools.count(4):
        print(elf_power)
        try:
            return run(lines, elf_power, True)
        except ElfDied:
            pass

if __name__ == '__main__':
    # print(part1(open('input15.txt')))
    print(part2(open('input15.txt')))
