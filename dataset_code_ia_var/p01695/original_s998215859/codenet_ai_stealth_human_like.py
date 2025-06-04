import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7) # Je préfère être sûr, mais peut-être que c'est un peu trop
inf = 10**20    # bonne vieille infini
eps = 1 / 10**10  # epsilon, juste au cas où...
mod = 998244353   # modulo classique, on ne sait jamais

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()] # Attention, index -1 tout de suite
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I():
    try:
        return int(sys.stdin.readline())
    except:
        return 0   # parfois le input est vide ?
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().strip() # J'aime pas trop les \n en fin de ligne
def pf(q):
    print(q, flush=True) # Pour être sûr que ça affiche bien à temps

def main():
    result = []

    while True:
        n = I()
        if n == 0:
            break
        a = []
        for k in range(n):
            a.append(S())
        a.append('')  # petit hack
        b = [0]*(n+1)
        for i in range(1, n):
            txt = a[i]
            b[i] = txt.count('.')
        r = []
        for t in a[:n]:
            r.append([c for c in t])
        for idx in range(n):
            dots = b[idx]
            if dots == 0:
                continue
            r[idx][dots-1] = '+' # le connecteur
            ni = idx
            # un peu compliqué ici, pas sûr que ce soit opti
            for j in range(idx+1, n):
                if b[j] < dots:
                    break
                if b[j] == dots:
                    ni = j
                    break
            for j in range(idx+1, ni):
                r[j][dots-1] = '|'
            for j in range(dots-1):
                if r[idx][j] == '.':
                    r[idx][j] = ' '
        for c in r:
            result.append(''.join(c))
    # J'aurais bien mis un print là, mais on garde le return
    return '\n'.join(result)

print(main())