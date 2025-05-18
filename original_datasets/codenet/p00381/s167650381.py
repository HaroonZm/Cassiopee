N = int(input())
s = input()
t = input()
D = {t[-1]: 1}
for i in range(N-2, 0, -1):
    si = s[i]; ti = t[i]
    v = D.get(si, 0)
    D[ti] = (D.get(ti, 0) + v) % (10**9+7)
print(D.get(s[0], 0))