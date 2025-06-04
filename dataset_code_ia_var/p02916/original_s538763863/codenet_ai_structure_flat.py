N = int(input())
As = list(map(int, input().split()))
for i in range(len(As)):
    As[i] -= 1
Bs = list(map(int, input().split()))
Cs = list(map(int, input().split()))
ans = 0
APrev = -100
i = 0
while i < N:
    A = As[i]
    ans += Bs[A]
    if APrev == A - 1:
        ans += Cs[APrev]
    APrev = A
    i += 1
print(ans)