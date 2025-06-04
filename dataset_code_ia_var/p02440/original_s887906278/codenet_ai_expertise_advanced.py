from sys import stdin
from functools import partial

def process_queries(N, A, queries):
    funcs = {0: min, 1: max}
    return (funcs[qtype](A[b:e]) for qtype, b, e in queries)

if __name__ == "__main__":
    it = map(int, stdin.read().split())
    N = next(it)
    A = [next(it) for _ in range(N)]
    Q = next(it)
    queries = [tuple(next(it) for _ in range(3)) for _ in range(Q)]
    print('\n'.join(map(str, process_queries(N, A, queries))))