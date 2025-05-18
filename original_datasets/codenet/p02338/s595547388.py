import sys
sys.setrecursionlimit(10**7)

n,k = map(int, input().split())
if n <= k:
    print(1)
else:
    print(0)