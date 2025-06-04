from functools import reduce

# Lecture
m, n = (int(x) for x in input().split())
plist = []
for i in range(m):
    plist.append(int(input()))
ce = []
i = 0
while i < n:
    ce.append(list(map(int, input().split())))
    i += 1

# DP init - style classique nested loop
dyn = []
for _ in range(n+1):
    dyn.append([1e100]*(m+1))
c = 0
while c < n+1:
    dyn[c][0] = 0
    c += 1

# Programmation dynamique avec un mix for/while
q = 0
while q < n:
    for w in range(1, m+1):
        if w < ce[q][0]:
            dyn[q+1][w] = min(dyn[q][w], ce[q][1])
        else:
            x = dyn[q][w-ce[q][0]] + ce[q][1]
            y = dyn[q][w]
            dyn[q+1][w] = x if x < y else y
    q += 1

plist.sort()
for i in range(m//2):
    plist[i], plist[m-1-i] = plist[m-1-i], plist[i]

sump = [0]*(m+1)
def acc(accu, val):
    return accu + val
r = 0
while r < m:
    sump[r+1] = sump[r] + plist[r]
    r += 1

# Récupération du max - mix comprehension et loop
results = []
for k in range(1, m+1):
    diff = sump[k] - dyn[n][k]
    if diff > 0:
        results.append(diff)
    else:
        results.append(0)
maximum = max(results)
print(maximum)