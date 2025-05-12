import sys

readline = sys.stdin.readline

A, P = map(int, readline().split())

print((A * 3 + P) // 2)