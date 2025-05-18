#!/usr/bin/env python3
N = int(input())
a = sorted(list(map(int, input().split())))

print(a[-1] - a[0])