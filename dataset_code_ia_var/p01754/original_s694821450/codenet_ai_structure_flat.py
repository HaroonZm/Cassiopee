n,p,q = map(int, input().split())
cn = []
for _ in range(n):
    cn.append(int(input()))
difs = []
for i in range(n):
    difs.append(p * (q - i) - cn[i])
difs.sort(reverse=True)
ans = [sum(cn)]
for i in range(n):
    ans.append(ans[-1] + 2 * i * p + difs[i])
m = ans[0]
for a in ans:
    if a > m:
        m = a
print(m)