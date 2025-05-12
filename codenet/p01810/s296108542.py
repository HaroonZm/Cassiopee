#!/usr/bin/env python3
n, k = map(int, input().split())
a = 0
for i in range(n-1):
    a = a * k // (k - 1) + 1
print(a)