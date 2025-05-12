#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
summation = 0
for i in range(n):
    d, c = [int(item) for item in input().split()]
    ans += c
    summation += d * c
print(ans - 1 + summation // 9 - (summation % 9 == 0))