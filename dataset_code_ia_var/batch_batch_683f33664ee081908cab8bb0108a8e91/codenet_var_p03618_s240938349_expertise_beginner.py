import sys
from collections import defaultdict

# Réglage de la limite de récursion
sys.setrecursionlimit(10**8)

# Définition d'une constante modulo
mod = 10**9 + 7

# Fonctions utilitaires pour la lecture des entrées
def inp():
    return int(input())

def inpm():
    return map(int, input().split())

def inpl():
    return list(map(int, input().split()))

def inpls():
    return list(input().split())

def inplm(n):
    result = []
    for _ in range(n):
        result.append(int(input()))
    return result

def inplL(n):
    result = []
    for _ in range(n):
        result.append(list(input()))
    return result

def inplT(n):
    result = []
    for _ in range(n):
        result.append(tuple(input()))
    return result

def inpll(n):
    result = []
    for _ in range(n):
        line = list(map(int, input().split()))
        result.append(line)
    return result

def inplls(n):
    result = []
    for _ in range(n):
        line = list(map(int, input().split()))
        result.append(line)
    result.sort()
    return result

def graph():
    n = inp()
    g = []
    for i in range(n):
        g.append([])
    for i in range(n):
        a = inp()
        a = a - 1
        g[i].append(a)
        g[a].append(i)
    return n, g

def main():
    s = list(input())
    n = len(s)
    dic = defaultdict(int)
    for i in range(n):
        dic[s[i]] += 1
    ans = 0
    for key in dic:
        ans = ans + (n - dic[key]) * dic[key]
    print(ans // 2 + 1)

if __name__ == "__main__":
    main()