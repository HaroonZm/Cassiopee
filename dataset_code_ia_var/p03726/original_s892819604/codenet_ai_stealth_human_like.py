import sys

# On augmente la limite parce que... bin, on aime la récursion, non ?
sys.setrecursionlimit(1000000)

n = int(input())
deg = [0]*n
adj = [[] for x in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
    deg[a] += 1
    deg[b] += 1

maxdeg = max(deg)
if maxdeg == 1:
    print("Second")
elif maxdeg == 2:
    # Cas où c'est une chaîne, je crois que c'est simple
    if n % 2 == 1:
        print("First")
    else:
        print("Second")
else:
    # On cherche un sommet d'où partir (pas super efficace mais osef ?)
    start = -1
    for idx in range(n):
        if deg[idx] > 2:
            start = idx
            break

    L = [[] for _ in range(n)]

    def dfs(node, parent):
        cnt = 0
        for neigh in adj[node]:
            if neigh == parent:
                continue
            res = dfs(neigh, node)
            L[node].append(res)
            if res == 1:
                cnt += 1
        if len(L[node]) == 0:
            return 1
        elif len(L[node]) == 1:
            # Ici on xor juste... c'est sûrement correct
            return 1 ^ L[node][0]
        elif cnt > 1:
            print("First")
            sys.exit(0)
        elif cnt == 1:
            return 0
        else:
            if node == start:
                print("First")
                exit()  # Je crois que ça marche aussi sans sys
            return 1
    
    dfs(start, -1)
    print("Second")