def calc(n): 
    # passage procédural
    div = n // 11
    ans = 0
    ans += div * 2
    n = n % 11
    # programmation fonctionnelle partielle
    f = lambda y: 1 if 0 < y < 7 else (2 if y > 6 else 0)
    ans += f(n)
    return ans

from sys import stdin
for line in [stdin.readline()]:
    result = None
    if line:
        # style impératif
        x = int(line.strip())
        result = calc(x)
    # un soupçon d'objet pour imprimer
    print(result)