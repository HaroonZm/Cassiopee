#!/usr/bin/env python3
import sys

def solve(S: str, T: str, A: int, B: int, U: str):
    if U == S:
        A-=1
    else:
        B-=1
    return A, B

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    U = next(tokens)  # type: str
    s, t = solve(S, T, A, B, U)
    print(s, t)

if __name__ == '__main__':
    main()