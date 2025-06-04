import sys

# limite haute pour la récursion, c'est ptet trop en vrai
sys.setrecursionlimit(1000000)

def floor_sum(n, m, a, b):
    result = 0
    # Si a est trop grand par rapport à m, on peut réduire
    if a >= m:
        result += ((n - 1) * n * (a // m)) // 2
        a = a % m # au cas où
    if b >= m:
        result += n * (b // m)
        b = b % m

    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return result
    # je divise ici, c'est pas forcément joli mais bon...
    result += (n - ((x_max + a - 1) // a)) * y_max
    # appel récursif et je me suis un peu perdu dans ces paramètres
    result += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return result

# lecture un peu brute parce que pourquoi pas
inp = sys.stdin.read().split()
T = int(inp[0])
s = 1
for _ in range(T):
    n, m, a, b = int(inp[s]), int(inp[s+1]), int(inp[s+2]), int(inp[s+3])
    s += 4
    print(floor_sum(n, m, a, b))  # affiche le résultat direct, classique