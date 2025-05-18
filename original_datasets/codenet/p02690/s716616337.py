import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline

x = int(input())

for i in range(1,1000):
    for j in range(-1000,1000):
        if i**5 - j**5 == x:
            print(i,j)
            exit(0)