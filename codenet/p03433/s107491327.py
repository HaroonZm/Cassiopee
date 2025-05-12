from sys import stdin
from itertools import combinations

n = int(stdin.readline().rstrip())
a = int(stdin.readline().rstrip())

if a >= n:
    print("Yes")

else:
    if n%500 <= a:
        print("Yes")
    else:
        print("No")