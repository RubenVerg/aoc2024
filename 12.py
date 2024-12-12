from collections import deque

i = [l.strip() for l in open('input/12.txt').readlines()]
'''
i = [l.strip() for l in """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()]
'''

def region(g: list[str], x: int, y: int) -> tuple[int, int, set[tuple[int, int]]]:
	area = 0
	perimeter = 0
	visited: set[tuple[int, int]] = set()
	queue: deque[tuple[int, int]] = deque()
	queue.append((x, y))

	while queue:
		x, y = queue.popleft()
		if (x, y) in visited:
			continue
		visited.add((x, y))
		area += 1
		perimeter += sum([
			x == 0 or g[y][x - 1] != g[y][x],
			x == len(g[0]) - 1 or g[y][x + 1] != g[y][x],
			y == 0 or g[y - 1][x] != g[y][x],
			y == len(g) - 1 or g[y + 1][x] != g[y][x],
		])
		for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			if (x + dx, y + dy) not in visited and 0 <= x + dx < len(g[0]) and 0 <= y + dy < len(g) and g[y + dy][x + dx] == g[y][x]:
				queue.append((x + dx, y + dy))
	return area, perimeter, visited

def sides(points: set[tuple[int, int]]) -> int:
	fences: set[tuple[int, int, int, int]] = set()
	sides = 0
	for (x, y) in sorted(points):
		for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
			if (x + dx, y + dy) not in points:
				if (x - (dx == 0), y - (dy == 0), dx, dy) not in fences:
					sides += 1
				fences.add((x, y, dx, dy))
	return sides

def parts(g: list[str]) -> tuple[int, int]:
	part1 = 0
	part2 = 0
	visited: set[tuple[int, int]] = set()
	for y in range(len(g)):
		for x in range(len(g[0])):
			if (x, y) not in visited:
				area, perimeter, points = region(g, x, y)
				part1 += area * perimeter
				part2 += area * sides(points)
				visited |= points
	return part1, part2


print(parts(i))
