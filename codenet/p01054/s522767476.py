#!/usr/bin/env python3

from collections import defaultdict

N = int(input())
s1 = input()
s2 = input()

def make_appears(s):
    chars = list(map(ord, s))
    hist = defaultdict(int)
    for ch in chars:
        hist[ch] += 1
    appears = list(hist.values())
    appears.sort()
    appears.reverse()
    return appears
    
appears1 = make_appears(s1)
appears2 = make_appears(s2)

ans = 0
for i, j in zip(appears1, appears2):
    ans += abs(i - j)

shorter = min(len(appears1), len(appears2))
ans += sum(appears1[shorter:]) + sum(appears2[shorter:])

print(ans//2)