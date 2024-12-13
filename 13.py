import re
from typing import Optional

i = open('input/13.txt').read()
'''
i = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
'''

def parse(s: str) -> list[tuple[int, int, int, int, int, int]]:
	return [tuple([int(n) for n in match]) for match in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", s)]

def solve(xa: int, xb: int, xg: int, ya: int, yb: int, yg: int) -> Optional[tuple[int, int]]:
	det = xa * yb - xb * ya
	if det == 0:
		return None
	asc = yb * xg - xb * yg
	bsc = xa * yg - ya * xg
	a = asc / det
	b = bsc / det
	if a != int(a) or b != int(b):
		return None
	return int(a), int(b)

def part1(i: str) -> int:
	buttons = parse(i)
	cost = 0
	for xa, ya, xb, yb, xg, yg in buttons:
		res = solve(xa=xa, ya=ya, xb=xb, yb=yb, xg=xg, yg=yg)
		if res is not None:
			cost += res[0] * 3 + res[1] * 1
	return cost

def part2(i: str) -> int:
	buttons = parse(i)
	cost = 0
	for xa, ya, xb, yb, xg, yg in buttons:
		res = solve(xa=xa, ya=ya, xb=xb, yb=yb, xg=xg + 10000000000000, yg=yg + 10000000000000)
		if res is not None:
			cost += res[0] * 3 + res[1] * 1
	return cost

print(part1(i))
print(part2(i))
