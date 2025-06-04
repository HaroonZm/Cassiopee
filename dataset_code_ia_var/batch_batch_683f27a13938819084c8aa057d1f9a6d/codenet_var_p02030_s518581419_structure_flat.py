from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random

mod = 1000000007

#A
n_m = sys.stdin.readline()
while n_m.strip() == '':
    n_m = sys.stdin.readline()
n, m = map(int, n_m.strip().split())

a_line = sys.stdin.readline()
while a_line.strip() == '':
    a_line = sys.stdin.readline()
a = list(map(int, a_line.strip().split()))

b_line = sys.stdin.readline()
while b_line.strip() == '':
    b_line = sys.stdin.readline()
b = list(map(int, b_line.strip().split()))

li = list(set(a) | set(b))
li2 = list(set(a) & set(b))
li.sort()
li2.sort()
print(len(li2), len(li))
for i in li2:
    print(i)
for i in li:
    print(i)
#B

#C

#D

#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T