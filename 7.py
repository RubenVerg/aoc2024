from math import prod

i = open("input/7.txt").readlines()

'''
i = [l.strip() for l in """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()]
'''
	
def part1(input: list[str]) -> int:
	def check(target: int, ints: list[int]) -> bool:
		if len(ints) == 0:
			return False
		if len(ints) == 1:
			return ints[0] == target
		if target % ints[-1] == 0:
			return check(target - ints[-1], ints[:-1]) or check(target // ints[-1], ints[:-1])
		else:
			return check(target - ints[-1], ints[:-1])
	result = 0
	for l in input:
		a, bs = l.split(': ')
		a = int(a)
		bs = [int(x) for x in bs.split(' ')]
		if check(a, bs):
			result += a
	return result

def part2(input: list[str]) -> int:
	def check(target: int, ints: list[int]) -> bool:
		if len(ints) == 0:
			return False
		if len(ints) == 1:
			return ints[0] == target
		check_prod = target % ints[-1] == 0
		str_last_int = str(ints[-1])
		check_catenation = str(target)[-len(str_last_int):] == str_last_int
		return (
			check(target - ints[-1], ints[:-1])
			or (check(target // ints[-1], ints[:-1]) if check_prod else 0)
			or (check(target // (10 ** len(str_last_int)), ints[:-1]) if check_catenation else 0)
		)
	result = 0
	for l in input:
		a, bs = l.split(': ')
		a = int(a)
		bs = [int(x) for x in bs.split(' ')]
		if check(a, bs):
			result += a
	return result

print(part1(i))
print(part2(i))
