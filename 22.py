from more_itertools import windowed

i = [int(l.strip()) for l in open('input/22.txt').readlines()]
'''
i = [int(l.strip()) for l in """1
10
100
2024""".splitlines()]
'''
'''
i = [int(l.strip()) for l in """1
2
3
2024""".splitlines()]
'''

def next_secret_number(previous: int):
	next = previous
	def mix_and_prune(x: int):
		nonlocal next
		next ^= x
		next %= 16777216
	mix_and_prune(next * 64)
	mix_and_prune(next // 32)
	mix_and_prune(next * 2048)
	return next

def part1(input: list[int]):
	result = 0
	for i in input:
		for _ in range(2000):
			i = next_secret_number(i)
		result += i
	return result

def part2(input: list[int]):
	costs: list[list[int]] = []
	cost_deltas: list[list[int]] = []
	possible_deltas: set[tuple[int, int, int, int]] = set()
	for i in input:
		c = [i % 10]
		for _ in range(2000):
			i = next_secret_number(i)
			c.append(i % 10)
		cd = [c1 - c0 for c0, c1 in zip(c, c[1:])]
		costs.append(c)
		cost_deltas.append(cd)
		for d in windowed(cd, 4): possible_deltas.add(d)
	max_bananas = 0
	for i, (d0, d1, d2, d3) in enumerate(possible_deltas):
		if i % 10 == 0: print(i, "/", len(possible_deltas))
		run_bananas = 0
		for (c, cd) in zip(costs, cost_deltas):
			for index in range(len(cd) - 3):
				if cd[index] == d0 and cd[index + 1] == d1 and cd[index + 2] == d2 and cd[index + 3] == d3:
					run_bananas += c[index + 4]
					break
		max_bananas = max(max_bananas, run_bananas)
	return max_bananas

print(part1(i))
print(part2(i))

