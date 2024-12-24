import heapq
from typing import Callable, TypeVar, Optional, cast
from itertools import chain
import sys

T = TypeVar('T')

sys.setrecursionlimit(10 ** 6)

def dijkstra(start: T, neighbors: Callable[[T], list[tuple[T, int]]], is_goal: Callable[[T], bool]) -> tuple[list[list[T]], Optional[int]]:
	frontier = [(0, start)]
	heapq.heapify(frontier)
	expanded: set[T] = set()
	prev: dict[T, list[T]] = dict()
	def backtrack(node: T) -> list[list[T]]:
		if node == start: return [[node]]
		return [list(chain.from_iterable([path + [node] for path in backtrack(prev_node)])) for prev_node in prev[node]]
	while True:
		if not len(frontier): return ([], None)
		(cost, node) = heapq.heappop(frontier)
		if is_goal(node): return (backtrack(node), cost)
		expanded.add(node)
		for (neighbor, neighbor_cost) in neighbors(node):
			if neighbor not in expanded and not any(x[1] == neighbor for x in frontier):
				heapq.heappush(frontier, (cost + neighbor_cost, neighbor))
				prev[neighbor] = [node]
			elif any(x[1] == neighbor for x in frontier):
				idx = [x[1] == neighbor for x in frontier].index(True)
				if cost + neighbor_cost < frontier[idx][0]:
					frontier[idx] = (cost + neighbor_cost, neighbor)
					prev[neighbor] = [node]
				elif cost + neighbor_cost == frontier[idx][0]:
					prev[neighbor].append(node)

i = [list(l.strip()) for l in open('input/16.txt').readlines()]
'''
i = [list(l.strip()) for l in """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()]
'''

def neighbors(grid: list[list[str]], x: int, y: int, dx: int, dy: int):
	ns = [((x, y, -dy, dx), 1000), ((x, y, dy, -dx), 1000)]
	nx, ny = x + dx, y + dy
	if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != '#':
		ns.append(((nx, ny, dx, dy), 1))
	return ns

start_y = ['S' in line for line in i].index(True)
start_x = i[start_y].index('S')
end_y = ['E' in line for line in i].index(True)
end_x = i[end_y].index('E')

paths = dijkstra((start_x, start_y, cast(int, 1), cast(int, 0)), lambda pd: neighbors(i, *pd), lambda pd: pd[0] == end_x and pd[1] == end_y)

print(paths[1])
print(len(set((point[0], point[1]) for point in chain.from_iterable(paths[0]))))
