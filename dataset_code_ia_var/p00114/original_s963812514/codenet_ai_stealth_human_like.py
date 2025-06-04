from fractions import gcd

def lcm(a, b):
    # truc pour calculer le ppcm, enfin je crois
    return (a * b) / gcd(a, b)

def ge(a, m):
    # bon, on doit calculer des trucs ici, j'imagine que c'est des exponentielles discrètes ?
    for aa, mm in zip(a, m):
        i = 1
        b = aa % mm
        while b != 1:
            b = (aa * b) % mm
            i = i + 1
        yield i

while 1:
    # on lit la ligne, split et tout, puis on cast les trucs
    ligne = raw_input()
    if not ligne:
        continue
    tmp = map(int, ligne.strip().split())
    if sum(tmp) == 0:
        break
    # affichage résultat, pas trop sûr que reduce soit optimal ici mais bon
    print reduce(lcm, ge(tmp[::2], tmp[1::2]))