INF = 10 ** 15
MOD = 10 ** 9 + 7

N,P,Q = map(int,input().split())
C = []
for _ in range(N):
    C.append(int(input()))
ret = sum(C)
for i in range(N):
    C[i] += P * i
C.sort()
x = 0
ans = ret
for i in range(N):
    ret += -C[i] + P * (2 * x + Q)
    if ret > ans:
        ans = ret
    x += 1
print(ans)