i = open("input/6.txt").readlines()

'''
i = [l.strip() for l in """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()]
'''

def traverse(map1: list[str]) -> tuple[set[str], bool]:
	pos_y = [i for (i, l) in enumerate(map1) if '^' in l][0]
	pos_x = map1[pos_y].index('^')
	visited1: set[tuple[int, int]] = set()
	visited2: set[tuple[int, int, int, int]] = set()
	pos = (pos_x, pos_y)
	map = map1.copy()
	direction = (0, -1)
	visited1.add(pos)
	visited2.add((pos[0], pos[1], direction[0], direction[1]))
	while True:
		if pos[0] + direction[0] < 0 or pos[0] + direction[0] >= len(map[0]) or pos[1] + direction[1] < 0 or pos[1] + direction[1] >= len(map):
			return (visited1, False)
		if map[pos[1] + direction[1]][pos[0] + direction[0]] == '#':
			direction = (-direction[1], direction[0])
		else:
			pos = (pos[0] + direction[0], pos[1] + direction[1])
			if ((pos[0], pos[1], direction[0], direction[1]) in visited2):
				return (visited1, True)
		visited1.add(pos)
		visited2.add((pos[0], pos[1], direction[0], direction[1]))

def part1(map: list[str]) -> int:
	return len(traverse(map)[0])

def part2(map: list[str]) -> int:
	(visited, _) = traverse(map)
	loops = 0
	checked: set[tuple[int, int]] = set()
	for pos in visited:
		for d in [(0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)]:
			if (pos[0] + d[0], pos[1] + d[1]) not in checked:
				new_map = [''.join(['#' if x == pos[0] + d[0] and c != '^' else c for (x, c) in enumerate(l)]) if y == pos[1] + d[1] else l for (y, l) in enumerate(map)]
				loops += traverse(new_map)[1]
				checked.add((pos[0] + d[0], pos[1] + d[1]))
	return loops

print(part1(i))
print(part2(i))
