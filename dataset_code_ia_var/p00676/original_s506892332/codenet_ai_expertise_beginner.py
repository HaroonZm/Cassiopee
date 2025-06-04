import sys

for ligne in sys.stdin:
    a, l, x = ligne.split()
    a = int(a)
    l = int(l)
    x = int(x)
    import math
    part1 = a * math.sqrt(4 * l * l - a * a)
    part2 = 2 * l * math.sqrt((l + x) ** 2 - l * l)
    resultat = (part1 + part2) / 4
    print(resultat)