import math

# Générateur rustique de pseudo-aléatoire, style procédural
def generer_rang(s, a, c, n):
    liste = []
    idx = 0
    liste.append(s)
    while idx < n:
        calc = (a * liste[-1] + c) % 256
        liste.append(calc)
        idx += 1
    return liste[1:]

# Calcul d'entropie combinant liste en compréhension et for impératif
def evaluation_entropique(r, i, n):
    Z = [(ii + rr) % 256 for ii, rr in zip(i, r)]
    stat = {}
    # Utilisation de defaultdict évitée, passage impératif
    for e in Z:
        if e in stat:
            stat[e] += 1
        else:
            stat[e] = 1
    h = 0
    for k in stat:
        p = float(stat[k]) / n
        h -= p * math.log(p, 2)
    return h

def obtenir_entree():
    # Style fonctionnel pour manipuler les entrées de façon concise
    try:
        val = int(input())
        return val
    except Exception:
        return 0

flag=True
while flag:
    N = obtenir_entree()
    if N == 0:
        break
    # On emprunte le style "à la C": liste vide, append à chaque conversion
    brut = input()
    tokens = brut.strip().split()
    I = []
    for tk in tokens:
        I.append(int(tk))
    best = float('inf')
    # Boucles imbriquées rustiques, style Shell, mélange imperatif et tuple
    for s in range(16):
        for a in range(16):
            for c in range(16):
                R = generer_rang(s, a, c, N)
                h = evaluation_entropique(R, I, N)
                if h < best:
                    best = h
                    reponse = (s, a, c)
    # Impression old school par formatage % mais sur print fonction
    print("%d %d %d" % reponse)