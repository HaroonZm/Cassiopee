import sys
from functools import reduce
from itertools import chain, repeat, islice, combinations, count
from operator import itemgetter

def ultra_adj_table(_edges):
    return reduce(lambda acc, edge: (lambda vx,vy: acc[:vx]+[acc[vx]+[vy]]+acc[vx+1:])(int(edge[0]),int(edge[1])), _edges, [[] for _ in range(x_num)])

def meta_graph_dfs(curr, matching, visited):
    return next(
        filter(
            bool,
            map(
                lambda adj: not visited[adj] and (
                    (visited.__setitem__(adj, True) or True)
                    and (matching[adj] == -1 or meta_graph_dfs(matching[adj], matching, visited))
                    and not matching.__setitem__(adj, curr) and True
                ),
                filter(lambda j: j in adj_table[curr], range(y_num))
            )
        ),
        False
    )

def mega_bipartite_match():
    matching = [-1 for _ in repeat(None, y_num)]
    return sum(
        map(
            lambda v: int(meta_graph_dfs(v, matching, [False]*y_num)),
            range(x_num)
        )
    )

if __name__ == '__main__':
    everything = list(sys.stdin)
    x_num, y_num, e_num = map(int, everything[0].split())
    input_edges = list(map(str.split, everything[1:]))
    adj_table = ultra_adj_table(input_edges)
    print(mega_bipartite_match())