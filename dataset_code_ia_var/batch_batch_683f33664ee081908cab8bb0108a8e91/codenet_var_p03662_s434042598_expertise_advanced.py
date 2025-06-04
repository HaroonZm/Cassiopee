from sys import stdin
import networkx as nx
from operator import itemgetter

N, *edges = next(stdin).split(), [line.split() for line in stdin]
N = N[0]
edges = edges or []

G = nx.Graph()
G.add_edges_from(edges)

sp_1 = nx.single_source_shortest_path_length(G, '1')
sp_N = nx.single_source_shortest_path_length(G, N)

cnt = sum(sp_1.get(k, float('inf')) > sp_N.get(k, float('inf')) for k in sp_1)
res = 'Fsennunkeec'
print(res[::2] if cnt * 2 >= int(N) else res[1::2])