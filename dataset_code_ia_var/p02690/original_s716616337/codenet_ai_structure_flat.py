import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline

x = int(input())

i = 1
found = False
while i < 1000 and not found:
    j = -1000
    while j < 1000 and not found:
        if i**5 - j**5 == x:
            print(i, j)
            found = True
            sys.exit(0)
        j += 1
    i += 1