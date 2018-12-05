import day04, day05

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
