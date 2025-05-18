#!/usr/bin/env python3
import os
from sys import stdin, stdout
    
    
def solve(tc):
    d, t, s = map(int, stdin.readline().split())

    if d/t<=s:
        print("Yes")
    else:
        print("No")

    
tcs = 1
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1