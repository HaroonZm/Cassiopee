N = int(input())

from itertools import accumulate

A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.reverse()

A = list(accumulate(A))
B = list(accumulate(B))
B.reverse()

m = max(a+b for a,b in zip(A,B))
print(m)