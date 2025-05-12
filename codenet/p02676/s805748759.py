import math
import time
from collections import defaultdict, deque
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
# t=int(input())
# for _ in range(t):
#     n,m=map(int,stdin.readline().split())
k=int(stdin.readline())
s=input()
if(len(s)<=k):
    print(s)
else:
    print(s[:k]+'...')