#!/usr/bin/env python

import re
from collections import defaultdict, Counter

def parse(filename):
    lines = sorted(open(filename))
    guard_id = None
    fell_asleep = None
    for line in lines:
        m = re.search(r'#(\d+) begins shift', line)
        if m:
            guard_id = int(m.group(1))
        elif 'falls asleep' in line:
            fell_asleep = int(line[15:17])
        elif 'wakes up' in line:
            wake_up = int(line[15:17])
            yield (guard_id, fell_asleep, wake_up)

def part1(filename):
    total_sleep = Counter()
    by_minute = defaultdict(Counter)
    for guard_id, fell_asleep, wake_up in parse(filename):
        total_sleep[guard_id] += wake_up - fell_asleep
        by_minute[guard_id].update(range(fell_asleep, wake_up))

    sleepiest, _ = total_sleep.most_common(1)[0]
    best_minute = by_minute[sleepiest].most_common(1)[0][0]
    return sleepiest * best_minute 

def part2(filename):
    guard_minute = Counter()
    for guard_id, fell_asleep, wake_up in parse(filename):
        guard_minute.update((guard_id, m) for m in range(fell_asleep, wake_up))

    a, b = guard_minute.most_common(1)[0][0]
    return a * b

if __name__ == '__main__':
    print(part1('input04.txt'))
    print(part2('input04.txt'))
