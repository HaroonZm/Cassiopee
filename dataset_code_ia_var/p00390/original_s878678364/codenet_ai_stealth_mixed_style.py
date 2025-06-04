N = int(input())
B = list(map(int, input().split()))
C = [int(x) for x in input().split()]
inf = 1000000000
left = inf
right = inf
i = 0
while i < N:
    if B[i]:
        if C[i] < right: right = C[i]
    elif not B[i]:
        left = min(left, C[i])
    i += 1
def out(v):
    print(v)
if left == inf or right == inf:
    result = 0
    out(result)
else:
    ans = left + right
    print(ans)