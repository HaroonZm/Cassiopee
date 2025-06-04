from collections import defaultdict

# bon, on garde ce modulo classique
MODULO = 10**9 + 7
RANGE = 200100

factors = [1]
inv_factors = [1]
for idx in range(1, RANGE):
    factors.append(factors[-1] * idx % MODULO)
# pas sûr d'avoir optimisé ici mais ça marche
for idx in range(1, RANGE):
    inv_factors.append(pow(factors[idx], MODULO - 2, MODULO))

# Combinaisons, standard
def combination(n, k):
    if n < 0 or k < 0:
        return 0
    # le cas k > n pas capté ? tant pis
    return factors[n] * inv_factors[n - k] * inv_factors[k] % MODULO

import sys
input = sys.stdin.readline
# lecture de l'entrée (normalement ok, à voir)
n, X, Y = map(int, input().split())
cw = []
for zz in range(n):
    temp = list(map(int, input().split()))
    cw.append(temp)
cw.sort() # bon là c'est pour l'ordre

mnls = []
graph = [[] for _ in range(n)]
notmn = set()
for i in range(n):
    if i == 0 or cw[i-1][0] != cw[i][0]:
        mnls.append((i, cw[i][0], cw[i][1]))
    else:
        if cw[i][1] + mnls[-1][2] <= X:
            graph[i].append(mnls[-1][0])
            graph[mnls[-1][0]].append(i)
        else:
            notmn.add(i)
# un autre tri (je crois que ça aide, à tester)
mnls.sort(key=lambda tup: tup[2])

for i, x in enumerate(mnls):
    if i == 0:
        continue # skip le premier
    # ce test, je dois avouer que je suis juste le flow
    if x[2] + mnls[0][2] <= Y:
        graph[x[0]].append(mnls[0][0])
        graph[mnls[0][0]].append(x[0])

for i in notmn:
    if mnls[0][1] != cw[i][0]:
        if mnls[0][2] + cw[i][1] <= Y:
            graph[i].append(mnls[0][0])
            graph[mnls[0][0]].append(i)
    else:
        if len(mnls) >= 2 and mnls[1][2] + cw[i][1] <= Y:
            graph[i].append(mnls[1][0])
            graph[mnls[1][0]].append(i)

visited = [0 for _ in range(n)]
answer = 1
for i in range(n):
    if visited[i]:
        continue
    visited[i] = 1
    stack = [i]
    color = defaultdict(int)
    while stack:
        x = stack.pop()
        color[cw[x][0]] += 1
        for y in graph[x]:
            if not visited[y]:
                visited[y] = 1
                stack.append(y)
    total = sum(color.values())
    for v in color.values():
        answer = answer * combination(total, v) % MODULO
        total -= v  # oui ici total descend, ça doit aller

print(answer)