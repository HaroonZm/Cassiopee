N, A, B = (int(x) for x in input().split())
c = []
for j in range(N):
    v = eval(input())
    if not (A <= v < B):
        c.append(v)
ans = 0
k = 0
while k < len(c):
    ans = ans + 1
    k += 1
print(ans)