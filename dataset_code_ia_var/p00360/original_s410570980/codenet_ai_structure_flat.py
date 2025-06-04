import sys

NI = lambda : int(sys.stdin.readline())
SI = lambda : sys.stdin.readline().rstrip()

s = SI()
n = len(s)
k = NI()

bit = [0] * (n+1)
z = [0] * n
top = [-1] * 26
nxt = [-1] * n
bef = [-1] * 26

for i in range(n):
    cv = ord(s[i]) - ord('a')
    if bef[cv] >= 0:
        nxt[bef[cv]] = i
    bef[cv] = i
    if top[cv] < 0:
        top[cv] = i

ans = []
while k > 0:
    found = False
    for i in range(26):
        if top[i] < 0:
            continue
        p = top[i]
        idx = p + 1
        cost = 0
        j = idx
        while j > 0:
            cost += bit[j]
            j -= j & -j
        cost = p - cost
        if cost <= k:
            ans.append(chr(ord('a')+i))
            z[top[i]] = 1
            k -= cost
            t = p + 1
            while t <= n:
                bit[t] += 1
                t += t & -t
            top[i] = nxt[top[i]]
            found = True
            break
    if not found:
        break

for i in range(n):
    if z[i] == 0:
        ans.append(s[i])
print(*ans, sep='')