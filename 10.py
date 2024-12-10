from collections import deque
from typing import TypeVar, Callable

T = TypeVar('T')
U = TypeVar('U')

i = [l.strip() for l in open('input/10.txt').readlines()]
'''
i = [l.strip() for l in """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()]
'''

def unique_on(l: list[T], f: Callable[[T], U]) -> list[T]:
	seen = []
	result = []
	for e in l:
		fe = f(e)
		if fe not in seen:
			seen.append(fe)
			result.append(e)
	return result

def parts(grid: list[list[int]]) -> tuple[int, int]:
	height = len(grid)
	width = len(grid[0])
	def neighbors(x: int, y: int) -> list[tuple[tuple[int, int], int]]:
		return (
			([((x - 1, y), grid[y][x - 1])] if x != 0 else []) +
			([((x + 1, y), grid[y][x + 1])] if x != width - 1 else []) +
			([((x, y - 1), grid[y - 1][x])] if y != 0 else []) +
			([((x, y + 1), grid[y + 1][x])] if y != height - 1 else [])
		)
	paths: list[list[tuple[int, int]]] = []
	queue: deque[tuple[list[tuple[int, int]], int]] = deque()
	for y, row in enumerate(grid):
		for x, cell in enumerate(row):
			if cell == 0:
				queue.append(([(x, y)], 0))
	while queue:
		positions, depth = queue.popleft()
		x, y = positions[-1]
		if depth == 9:
			paths.append(positions)
			continue
		for (nx, ny), ndepth in neighbors(x, y):
			if ndepth == depth + 1:
				queue.append((positions + [(nx, ny)], ndepth))
	return len(unique_on(paths, lambda xs: (xs[0], xs[-1]))), len(paths)

part1, part2 = parts([[int(ch) for ch in row] for row in i])

print(part1)
print(part2)
