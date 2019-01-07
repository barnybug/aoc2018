import day01, day02, day03, day04, day05
import day06, day07, day08, day09, day10
import day11, day12, day13, day14, day15
import day16, day17, day18, day19, day20
import day21, day22, day23, day24

import itertools

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

def test_day14_part1():
    assert day14.part1(9) == '5158916779'
    assert day14.part1(5) == '0124515891'
    assert day14.part1(18) == '9251071085'
    assert day14.part1(2018) == '5941429882'

def test_day14_part2():
    assert day14.part2('51589') == 9
    assert day14.part2('01245') == 5
    assert day14.part2('92510') == 18
    assert day14.part2('59414') == 2018

def test_day15_choose_target():
    lines = '#######\n#E..G.#\n#...#.#\n#.G.#G#\n#######'.split()
    board = day15.create_board(lines)
    unit = board[1,1]
    targets = day15.get_targets(unit, board)
    target = day15.choose_target((1,1), targets, board)
    assert target == (3, 1)

def test_day15_example():
    lines = '#########\n#G..G..G#\n#.......#\n#.......#\n#G..E..G#\n#.......#\n#.......#\n#G..G..G#\n#########'.split()
    day15.part1(lines)

def test_day15_part1():
    tests = open('test15.txt')
    games = [list(group) for k, group in itertools.groupby(tests, lambda s: s != '\n') if k]

    assert day15.part1(games[0]) == 27730
    assert day15.part1(games[1]) == 36334
    assert day15.part1(games[2]) == 39514
    assert day15.part1(games[3]) == 27755
    assert day15.part1(games[4]) == 28944
    assert day15.part1(games[5]) == 18740

def test_day15_part2():
    tests = open('test15.txt')
    games = [list(group) for k, group in itertools.groupby(tests, lambda s: s != '\n') if k]

    assert day15.part2(games[0]) == 4988
    assert day15.part2(games[2]) == 31284
    assert day15.part2(games[3]) == 3478
    assert day15.part2(games[4]) == 6474
    assert day15.part2(games[5]) == 1140

def test_day16_part1():
    assert day16.parts('test16.txt', part2=False) == 1

def test_day17_part1():
    assert day17.part1('test17.txt') == 57
    assert day17.part1('test17_2.txt') == 66

def test_day17_part2():
    assert day17.part2('test17.txt') == 29

def test_day18_part1():
    assert day18.part1('test18.txt', 10) == 1147

def test_day19_part1():
    assert day19.part1('input19.txt') == 1152

def test_day19_part2():
    assert day19.part2('input19.txt') == 12690000

def test_day20_part1():
    assert day20.part1('^WNE$') == 3
    assert day20.part1('^ENWWW(NEEE|SSE(EE|N))$') == 10
    assert day20.part1('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)') == 18
    assert day20.part1('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$') == 23
    assert day20.part1('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$') == 31

def test_day21():
    assert list(itertools.islice(day21.seq(), 10)) == [6619857, 7435730, 9149508, 14415175, 5500417, 9362280, 12034598, 8811079, 7737914, 2475507]

def test_day22_part1():
    assert day22.part1(510, (10, 10)) == 114

def test_day22_part2():
    assert day22.part2(510, (10, 10)) == 45

def test_day23_part1():
    assert day23.part1('test23.txt') == 7

def test_day23_part2():
    assert day23.part2('test23_2.txt') == 36

def test_day24_part1():
    assert day24.part1('test24.txt') == 5216

def test_day24_part2():
    assert day24.part2('test24.txt') == 51
