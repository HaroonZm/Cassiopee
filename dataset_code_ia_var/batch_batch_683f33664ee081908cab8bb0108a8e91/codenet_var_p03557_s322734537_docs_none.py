from bisect import bisect_left
from bisect import bisect_right
N = int(input())
A = sorted(list(map(int, input().split()))) 
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ab = bisect_left(A,B[i])
    bc = N-bisect_right(C,B[i])
    ans += ab*bc
print(ans)