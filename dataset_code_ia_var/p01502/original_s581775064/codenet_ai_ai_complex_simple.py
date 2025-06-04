from functools import reduce
from operator import add
import sys

def main():
    n = int(input())
    edge_lines = list(map(lambda _: sys.stdin.readline(), range(n)))
    edges = list(map(lambda line: list(map(int, line.split())), edge_lines))
    coordinate_pairs = filter(lambda tpl: tpl[0] < tpl[1], ((i, j) for i in range(n) for j in range(n)))
    answer_sum = reduce(
        add,
        map(
            lambda pair: min(edges[pair[0]][pair[1]], edges[pair[1]][pair[0]]),
            coordinate_pairs
        ),
        0
    )
    print(answer_sum)

if __name__ == '__main__':
    main()