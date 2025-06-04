from sys import stdin
from functools import reduce

def get_input():
    try:
        return int(stdin.readline())
    except Exception:
        return 0

read_edges = lambda n: [list(map(int, stdin.readline().split(','))) for _ in range(n)]

def main():
    while True:
        num_nodes = get_input()
        if num_nodes == 0:
            break

        edge_count = get_input()
        edges = read_edges(edge_count)

        def cmp_key(e):
            return e[2]
        edges.sort(key=cmp_key, reverse=True)

        forests = set()
        for i in range(num_nodes):
            forests.add(frozenset([i]))
        spanning_weights = []

        def merge_and_pop():
            while len(edges) > 0:
                n1, n2, d = edges.pop()
                fA = fB = None
                i = 0
                for group in forests:
                    if n1 in group:
                        fA = group
                    if n2 in group:
                        fB = group
                    if fA and fB:
                        break
                    i += 1
                if fA != fB:
                    forests.add(fA | fB)
                    forests.discard(fA)
                    forests.discard(fB)
                    spanning_weights.append(d)
        merge_and_pop()
        result = 0
        for dist in spanning_weights:
            result += (dist // 100) - 1
        print(result)

main()