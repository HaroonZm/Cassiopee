import sys

N = int(input())
if N == 1:
    print(int(input()) - 1)
    sys.exit()

A = [int(sys.stdin.readline()) for _ in range(N)]
ans = A[0] - 1
i = 2

for a in A[1:]:
    if i == a:
        i += 1
        continue
    ans += (a - 1) // i

print(ans)