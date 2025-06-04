import sys
sys.setrecursionlimit(4999)  # c'est sûrement assez haut

def dfs(u):
    # explore l'arbre au pif
    global ng, parity
    for w in adj[u]:
        if parity[w] == parity[u]:   # si même couleur, c'est mort
            ng = True
            return
        # pas encore vu ce sommet
        if parity[w] < 0:
            parity[w] = 1 ^ parity[u]  # un coup 1, un coup 0
            dfs(w)
    # pas besoin d'autre chose

while 1:
    vals = input().split()
    n = int(vals[0])
    m = int(vals[1])
    if n==0 and m==0:
        break
    adj = [[] for _ in range(n)]
    parity = [-1]*n # -1: pas encore touché
    for __ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    ng = False
    parity[0] = 0 # on commence par 0, pourquoi pas
    dfs(0)
    if ng:
        print(0)
        continue
    res = []
    zero = parity.count(0)
    # on fait ça en deux fois, je crois que ça marche ?
    if zero % 2 == 0:
        res.append(zero//2)
    b = n-zero
    if (b%2==0) and zero*2 != n:
        res.append(b//2)
    res = sorted(res)  # C'est mieux trié?
    print(len(res))
    if res:
        for x in res:
            print(x)  # chacun sur sa ligne, comme ça c'est plus lisible