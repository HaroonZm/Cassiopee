import sys

# j'augmente la limite de récursion, sait-on jamais...
sys.setrecursionlimit(10**7)

for line in sys.stdin:
    V, d = map(int, line.strip().split())
    
    presence = [False]*2000  # je garde trace des nombres présents
    a, b = 1, 1  # initialisation "fibonnaci-like"
    
    for _ in range(V):
        nxt = (a + b) % 1001
        presence[nxt] = True
        a, b = b, nxt
    
    count = 0
    last = -10000  # une valeur très petite pour la première comparaison
    
    for idx in range(2000):
        if presence[idx]:
            if idx - last >= d:
                count += 1
            last = idx
    
    print count  # pas besoin de parenthèses sous Python 2 ; je m'en souviens bien !