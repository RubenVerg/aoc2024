import networkx as nx
from networkx.drawing.nx_pylab import draw
import matplotlib.pyplot as plt

i = [l.strip() for l in open('input/23.txt').readlines()]
'''
i = [l.strip() for l in """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".splitlines()]
'''

g = nx.Graph()
for line in i:
	[a, b] = line.split('-')
	g.add_edge(a, b)

def part1(g: nx.Graph):
	return sum(any(x[0] == 't' for x in cycle) for cycle in list(nx.simple_cycles(g, length_bound=3)))

def part2(g: nx.Graph):
	return ','.join(sorted(sorted(nx.find_cliques(g), key=lambda x: len(x))[-1]))

print(part1(g))
print(part2(g))

# draw(g, with_labels=True)
# plt.show()

