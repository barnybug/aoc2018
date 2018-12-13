import day01, day02, day03, day04, day05
import day06, day07, day08, day09, day10
import day11, day12, day13

def test_day01_part1():
    assert day01.part1('+1, -2, +3, +1'.split(', ')) == 3

def test_day01_part2():
    assert day01.part2('+1, -2, +3, +1'.split(', ')) == 2
    assert day01.part2('+1, -1'.split(', ')) == 0
    assert day01.part2('+3, +3, +4, -2, -4'.split(', ')) == 10
    assert day01.part2('-6, +3, +8, +5, -6'.split(', ')) == 5
    assert day01.part2('+7, +7, -2, -7, -4'.split(', ')) == 14

def test_day02_part1():
    assert day02.part1('bcdef bababc abbcde abcccd aabcdd abcdee ababab'.split()) == 12

def test_day02_part2():
    assert day02.part2('abcde fghij klmno pqrst fguij axcye wvxyz'.split()) == 'fgij'

def test_day03_part1():
    assert day03.part1('#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'.split('\n')) == 4

def test_day03_part2():
    assert day03.part2('#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2'.split('\n')) == 3

def test_day04():
    assert day04.part1('test04.txt') == 240
    assert day04.part2('test04.txt') == 4455

def test_day05_part1():
    assert day05.part1('aA') == 0
    assert day05.part1('abBA') == 0
    assert day05.part1('abAB') == 4
    assert day05.part1('aabAAB') == 6
    assert day05.part1('dabAcCaCBAcCcaDA') == 10

def test_day05_part2():
    assert day05.part2('dabAcCaCBAcCcaDA') == 4

def test_day06_part1():
    assert day06.part1('test06.txt') == 17

def test_day06_part2():
    assert day06.part2('test06.txt', 32) == 16

def test_day07_part1():
    assert day07.part1('test07.txt') == 'CABDFE'

def test_day07_part2():
    assert day07.part2('test07.txt', day07.test_cost, 2) == 15

def test_day08_part1():
    assert day08.part1('test08.txt') == 138

def test_day08_part2():
    assert day08.part2('test08.txt') == 66

def test_day09_part1():
    assert day09.part1(9, 25) == 32
    assert day09.part1(10, 1618) == 8317
    assert day09.part1(13, 7999) == 146373
    assert day09.part1(17, 1104) == 2764
    assert day09.part1(21, 6111) == 54718
    assert day09.part1(30, 5807) == 37305

def test_day09_part2():
    assert day09.part2(9, 25) == 32
    assert day09.part2(10, 1618) == 8317
    assert day09.part2(13, 7999) == 146373
    assert day09.part2(17, 1104) == 2764
    assert day09.part2(21, 6111) == 54718
    assert day09.part2(30, 5807) == 37305

def test_day10_part2():
    assert day10.parts('test10.txt') == 3

def test_day11_part1():
    assert day11.part1(18) == (33, 45)
    assert day11.part1(42) == (21, 61)

def test_day11_part2():
    assert day11.part2(18) == (90, 269, 16)
    assert day11.part2(42) == (232, 251, 12)

def test_day12_part1():
    assert day12.part1('test12.txt', 20) == 325
    assert day12.part1('test12.txt', 200) == 3374
    assert day12.part1('test12.txt', 220) == 3774
    assert day12.part1('test12.txt', 221) == 3794

def test_day13_part1():
    assert day13.part1('test13.txt') == '7,3'

def test_day13_part2():
    assert day13.part2('test13_2.txt') == '6,4'
