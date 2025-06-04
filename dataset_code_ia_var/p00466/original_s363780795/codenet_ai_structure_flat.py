import sys
from sys import stdin
input = stdin.readline

while True:
    s = int(input())
    if s == 0:
        break
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    h = int(input())
    i = int(input())
    total = a + b + c + d + e + f + g + h + i
    print(s - total)