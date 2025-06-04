import sys
N = int(input())
if N == 1:
    print(int(input()) - 1)
    sys.exit()
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
ans = A[0] - 1
i = 2
j = 1
while j < N:
    a = A[j]
    if i == a:
        i += 1
        j += 1
        continue
    ans += (a-1)//i
    j += 1
print(ans)