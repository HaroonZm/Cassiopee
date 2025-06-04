import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

i = 0
seq = 0
ans = 0
while i < N:
    A[i] -= i + 1
    if A[i] == 0:
        seq += 1
    else:
        ans += (seq + 1) // 2
        seq = 0
    i += 1
ans += (seq + 1) // 2
print(ans)