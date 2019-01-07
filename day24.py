#!/usr/bin/env python

import itertools
import logging
import re

class Group(object):
    def __init__(self, immune, n, units, hitpoints, weaknesses, immunity, initiative, attack, attack_type):
        self.immune = immune
        self.n = n
        self.units = units
        self.hitpoints = hitpoints
        self.weaknesses = weaknesses
        self.immunity = immunity
        self.initiative = initiative
        self.attack = attack
        self.attack_type = attack_type

    @property
    def effective_power(self):
        return self.units * self.attack

    def damage(self, b):
        if self.attack_type in b.immunity:
            return 0
        elif self.attack_type in b.weaknesses:
            return 2 * self.effective_power
        return self.effective_power

    @property
    def name(self):
        if self.immune:
            return 'Immune System group %d' % self.n
        return 'Infection group %d' % self.n

    @classmethod
    def parse(cls, immune, n, line):
        m = re.match(r'(\d+) units each with (\d+) hit points (\(.+\) )?with an attack that does (\d+) (\S+) damage at initiative (\d+)', line)
        units, hitpoints, details, attack, attack_type, initiative = m.groups()
        weak_to = re.findall(r'weak to ([^;)]+)', details or '')
        weaknesses = weak_to[0].split(', ') if weak_to else []
        immune_to = re.findall(r'immune to ([^;)]+)', details or '')
        immunity = immune_to[0].split(', ') if immune_to else []

        return Group(
            immune,
            n,
            int(units), 
            int(hitpoints),
            set(weaknesses),
            set(immunity),
            int(initiative),
            int(attack),
            attack_type)

    def __repr__(self):
        return str(self.__dict__)

def parse(filename):
    pairs = (list(lines) for _, lines in itertools.groupby(open(filename), lambda s: s.endswith(':\n')))
    pairs = zip(pairs, pairs)

    for header, lines in pairs:
        if header[0].startswith('Immune'):
            immune = [Group.parse(True, i+1, line) for i, line in enumerate(lines) if line != '\n']
        elif header[0].startswith('Infection'):
            infection = [Group.parse(False, i+1, line) for i, line in enumerate(lines) if line != '\n']

    return immune + infection

def select_targets(ga, gb):
    gb = gb[:]
    res = []
    for a in sorted(ga, key=lambda a: (-a.effective_power, -a.initiative)):
        if not gb:
            break
        for b in sorted(gb, key=lambda u: u.n):
            d = a.damage(b)
            logging.debug('%s would deal defending group %s %d damage' % (a.name, b.n, d))
        gb.sort(key=lambda b: (-a.damage(b), -b.effective_power, -b.initiative))
        if a.damage(gb[0]) == 0:
            # "If it cannot deal any defending groups damage, it does not choose a target"
            continue
        pick = gb.pop(0)
        # logging.debug('%s picked %s' % (a.name, pick.name))
        res.append((a, pick))
    return res

def run(filename, boost):
    units = parse(filename)
    for unit in units:
        if unit.immune:
            unit.attack += boost

    drawn = False
    while not drawn:
        drawn = True
        immune = [t for t in units if t.immune]
        logging.debug('Immune System:')
        for g in sorted(immune, key=lambda u: u.n):
            logging.debug('Group %d contains %d units' % (g.n, g.units))
        infection = [t for t in units if not t.immune]
        logging.debug('Infection:')
        for g in sorted(infection, key=lambda u: u.n):
            logging.debug('Group %d contains %d units' % (g.n, g.units))
        logging.debug('')

        if not immune or not infection:
            break

        # target selection
        targets = dict()
        t = select_targets(infection, immune)
        targets.update(t)
        t = select_targets(immune, infection)
        targets.update(t)
        logging.debug('')

        # attacking in increasing order of initiative
        units.sort(key=lambda u: -u.initiative)
        for unit in units:
            if unit.units == 0:
                continue
            target = targets.get(unit)
            if not target:
                continue

            killed = min(unit.damage(target) // target.hitpoints, target.units)
            if killed:
                drawn = False
            logging.debug('%s attacks defending group %d, killing %d units' % (unit.name, target.n, killed))
            target.units -= killed

        units = [u for u in units if u.units > 0]
        logging.debug('')

    return sum(u.units for u in infection), sum(u.units for u in immune)

def part1(filename):
    score, _ = run(filename, 0)
    return score

def part2(filename):
    for boost in itertools.count(1):
        infection, immune = run(filename, boost)
        if infection == 0:
            break
    return immune

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    print(part1('input24.txt'))
    print(part2('input24.txt'))
