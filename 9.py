from typing import Optional
from itertools import chain

i = open('input/9.txt').read().strip()
# i = "2333133121414131402"

def part1(s: str) -> int:
	xs = list(chain.from_iterable([i // 2 if i % 2 == 0 else None] * int(x) for (i, x) in enumerate(s)))
	while None in xs:
		xs[xs.index(None)] = xs.pop()
	return sum(x * i for (i, x) in enumerate(xs))

def part2(s: str) -> int:
	lens = [int(c) for c in s]
	vals = [i // 2 if i % 2 == 0 else None for i in range(len(s))]
	result = 0
	index = 0
	while len(vals):
		l = lens.pop(0)
		v = vals.pop(0)
		if v is not None:
			result += sum(v * i for i in range(index, index + l))
			index += l
		else:
			possible = [ni for (ni, (nl, nv)) in enumerate(zip(lens, vals)) if nl <= l and nv is not None]
			if len(possible):
				selected = possible[-1]
				result += sum(vals[selected] * i for i in range(index, index + lens[selected]))
				index += lens[selected]
				vals[selected] = None
				if lens[selected] < l:
					vals.insert(0, None)
					lens.insert(0, l - lens[selected])
			else:
				index += l
	return result

print(part1(i))
print(part2(i))
