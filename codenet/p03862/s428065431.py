#!/usr/bin/env python3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split())) + [0]

    result = 0
    for i in range(N):
        tmp = max(0, A[i] + A[i - 1] - X)
        result += tmp
        A[i] -= tmp
    print(result)

if __name__ == "__main__":
    main()