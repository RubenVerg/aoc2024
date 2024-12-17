import re
from functools import reduce

i = open('input/17.txt').read().strip()
'''
i = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
'''

def parse(i: str) -> tuple[int, int, int, list[int]]:
	a = int(re.search(r"Register A: (\d+)", i).group(1))
	b = int(re.search(r"Register B: (\d+)", i).group(1))
	c = int(re.search(r"Register C: (\d+)", i).group(1))
	program = [int(l) for l in re.search(r"Program: ([\d,]+)", i).group(1).split(",")]
	return a, b, c, program

def run(a: int, b: int, c: int, program: list[int]) -> int:
	ip = 0
	output: list[int] = []
	def combo(arg: int) -> int:
		if arg in [0, 1, 2, 3]: return arg
		if arg == 4: return a
		if arg == 5: return b
		if arg == 6: return c
		return 0
	while ip < len(program):
		op = program[ip]
		arg = program[ip + 1]
		ip += 2
		if op == 0:
			a = a // (2 ** combo(arg))
		elif op == 1:
			b = b ^ arg
		elif op == 2:
			b = combo(arg) % 8
		elif op == 3:
			if a != 0: ip = arg
		elif op == 4:
			b = b ^ c
		elif op == 5:
			output.append(combo(arg) % 8)
		elif op == 6:
			b = a // (2 ** combo(arg))
		elif op == 7:
			c = a // (2 ** combo(arg))
		else:
			raise RuntimeError(f"Unknown op {op}")
	return output

def part1(i: str) -> str:
	return ','.join(str(o) for o in run(*parse(i)))

# not working!
def part2(i: str) -> str:
	_, b, c, program = parse(i)
	digits = [0 for _ in program]
	digits[-1] = 1
	for i in range(len(digits)):
		for dig in range(8):
			digits[i] = dig
			output = run(reduce(lambda a, b: a * 8 + b, digits, 0), b, c, program)
			print(output)
			if (output[-i] if i < len(output) else 0) == dig: break
	return reduce(lambda a, b: a * 8 + b, digits, 0)

print(part1(i))
# print(part2(i))
