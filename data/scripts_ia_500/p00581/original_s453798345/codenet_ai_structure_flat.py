#!/usr/bin/python3

import os
import sys

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

H, W = [int(e) for e in inp().split()]
S = [inp() for _ in range(H)]

o_table = [[0]*W for _ in range(H)]
for y in range(H):
    c = 0
    for x in range(W-1, -1, -1):
        if S[y][x] == 'O':
            c += 1
        o_table[y][x] = c

i_table = [[0]*W for _ in range(H)]
for x in range(W):
    c = 0
    for y in range(H-1, -1, -1):
        if S[y][x] == 'I':
            c += 1
        i_table[y][x] = c

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == 'J':
            ans += o_table[y][x] * i_table[y][x]

print(ans)