i = open("input/1.txt").readlines()
cs = [[int(p) for p in l.split()] for l in i]
c1, c2 = [c[0] for c in cs], [c[1] for c in cs]
print(sum([abs(a - b) for (a, b) in zip(sorted(c1), sorted(c2))]))
print(sum([a * sum([a == b for b in c2]) for a in c1]))
