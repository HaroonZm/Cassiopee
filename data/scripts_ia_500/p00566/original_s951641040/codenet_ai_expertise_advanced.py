#!/usr/bin/env python3
import sys

def main():
    H, W = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    # Pré-calculer pour accélérer les distances
    best = float('inf')
    for ay in range(H):
        for ax in range(W):
            s = 0
            for y, row in enumerate(A):
                for x, val in enumerate(row):
                    d = min(abs(y - ay), abs(x - ax))
                    s += val * d
                    if s >= best:
                        break  # early stop
                if s >= best:
                    break
            if s < best:
                best = s
    print(best)

if __name__ == '__main__':
    main()