N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
r = 0
for i in range(N):
    r = max(r, sum(A[:i+1])+sum(B[i:]))
print(r)