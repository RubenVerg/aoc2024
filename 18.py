import heapq
from typing import Callable, TypeVar, Optional, Iterable, cast
from itertools import chain
import sys
import ray

T = TypeVar('T')

sys.setrecursionlimit(10 ** 6)

def dijkstra(start: T, neighbors: Callable[[T], list[tuple[T, int]]], is_goal: Callable[[T], bool]) -> tuple[Iterable[list[T]], Optional[int]]:
	frontier = [(0, start)]
	heapq.heapify(frontier)
	expanded: set[T] = set()
	prev: dict[T, list[T]] = dict()
	def backtrack(node: T) -> Iterable[list[T]]:
		if node == start: return [[node]]
		return (list(chain.from_iterable([path + [node] for path in backtrack(prev_node)])) for prev_node in prev[node])
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

i = [l.strip() for l in open('input/18.txt').readlines()]
'''
i = [l.strip() for l in """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".splitlines()]
'''

def neighbors(goal: tuple[int, int], marked: list[tuple[int, int]], x: int, y: int):
	ns = []
	if x != 0 and (x - 1, y) not in marked:
		ns.append(((x - 1, y), 1))
	if x != goal[0] and (x + 1, y) not in marked:
		ns.append(((x + 1, y), 1))
	if y != 0 and (x, y - 1) not in marked:
		ns.append(((x, y - 1), 1))
	if y != goal[1] and (x, y + 1) not in marked:
		ns.append(((x, y + 1), 1))
	return ns

marked = cast(list[tuple[int, int]], [tuple(map(int, line.split(','))) for line in i])

goal = (6, 6) if len(marked) == 25 else (70, 70)
fallen = 12 if len(marked) == 25 else 1024

print(dijkstra((0, 0), lambda pd: neighbors(goal, marked[:fallen], *pd), lambda pd: pd == goal)[1])

@ray.remote
def part2loop(fallen: int):
	return dijkstra((0, 0), lambda pd: neighbors(goal, marked[:fallen], *pd), lambda pd: pd == goal)[1] is None

ray.init()

print(','.join(map(str, marked[ray.get([part2loop.remote(fallen) for fallen in range(len(marked) + 1)]).index(True) - 1])))
