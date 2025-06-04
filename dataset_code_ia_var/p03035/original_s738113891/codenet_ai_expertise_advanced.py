from sys import stdin

A, B = map(int, stdin.readline().split())
print(B if A >= 13 else B // 2 if 6 <= A <= 12 else 0)