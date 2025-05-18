#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

def solve(N: int, A: int, B: int, X: "List[int]"):
    print(sum(
        min((xj - xi) * A, B)
        for xi, xj in zip(X, X[1:])
    ))

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, X)

if __name__ == '__main__':
    main()