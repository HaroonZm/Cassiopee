import sys

def get_input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000000)

M = 10**9 + 7

n = int(get_input())
p = list(map(int, get_input().split()))

# Calcul des factorielles modulo M
g1 = [1] * (n + 11)
for i in range(1, len(g1)):
    g1[i] = (g1[i-1] * i) % M

def add(bit, i, x):
    while i < len(bit):
        bit[i] += x
        i += i & -i

def query(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

# Indices où l'élément est 0 dans p (valeurs manquantes)
index = []
for i in range(n):
    if p[i] == 0:
        index.append(i)

used = [False]*n
for i in range(n):
    if p[i] > 0:
        used[p[i]-1] = True

nl = []
for i in range(n):
    if not used[i]:
        nl.append(i+1)
nl.sort()

scores = [0] * (n+1)
v = len(nl)
cur = 0
for i in range(1, n+1):
    if cur < len(nl) and nl[cur] < i:
        cur += 1
        v -= 1
    scores[i] = v

ans = 0
bit = [0] * (n+1)
s = set(index)
val = 0
pp = len(index)
ss = sum(nl)
num = 0
inv2 = pow(2, M-2, M)

for i in range(n):
    if i in s:
        if pp > 0:
            tmp1 = g1[pp-1] * (ss - pp - val - pp*num*inv2)
            ans += tmp1 * g1[n-i-1]
        num += 1
    else:
        temp2 = g1[pp] * (p[i] - query(bit, p[i]) - 1)
        temp3 = 0
        if pp > 0:
            temp3 = g1[pp-1] * num * (len(nl) - scores[p[i]])
        ans += (temp2 - temp3) * g1[n-i-1]
        add(bit, p[i], 1)
        val += scores[p[i]]
    ans %= M

print((ans + g1[pp]) % M)