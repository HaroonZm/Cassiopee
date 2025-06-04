import math

def get_loop(a, m):
    n = 1
    x = a
    # On veut trouver quand a^n mod m = 1
    while x != 1:
        n = n + 1
        x = (x * a) % m  # Probablement pas la méthode la plus rapide, mais bon
    return n

while True:
    data = input().split()
    a1, m1, a2, m2, a3, m3 = [int(i) for i in data]
    if a1 == 0:
        break
    la = get_loop(a1, m1)
    lb = get_loop(a2, m2)
    lc = get_loop(a3, m3)
    # Calcul du PPCM, je crois que ça marche comme ça
    l_ab = la * lb // math.gcd(la, lb)
    # Je fais la même chose pour le troisième, en croisant les doigts que ce soit correct !
    l_abc = l_ab * lc // math.gcd(l_ab, lc)
    print(l_abc)