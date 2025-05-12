#!/usr/bin/env python

def main():
    k, a, b = list(map(int, input().split()))
    if b - a <= 2 or k - a < 1:
        print(k+1)
        return
    n = (k - a + 1) // 2
    print(1 + k - 2*n + (b - a) * (n))

if __name__ == '__main__':
    main()