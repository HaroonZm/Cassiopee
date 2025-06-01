mgr = [4, 1, 4, 1, 2, 1, 2, 1]

def lire_entree():
    return list(map(int, input().split(' ')))

def rotation_liste(liste, n):
    return liste[n:] + liste[:n]

def calculer_valeur(p, q):
    valeurs = []
    for j in range(8):
        diff = p[j] - q[j]
        valeurs.append(diff if diff >= 0 else 0)
    return valeurs

def somme_valeurs(vals):
    return sum(vals)

def calculer_somme_v(p, q):
    valeurs = calculer_valeur(p, q)
    return sum(p) - somme_valeurs(valeurs)

def calculer_v(p):
    v = []
    for i in range(8):
        q = rotation_liste(mgr, i)
        sum_v = calculer_somme_v(p, q)
        v.append(sum_v)
    return v

def trouver_max_v(v):
    return max(v)

def compte_max_v(v, mv):
    return v.count(mv)

def indices_max_v(v, mv):
    indices = []
    for i in range(8):
        if v[i] == mv:
            indices.append(i)
    return indices

def former_entiers(indices):
    nombres = []
    for i in indices:
        rotation = rotation_liste(mgr, i)
        nombre_str = "".join(map(str, rotation))
        nombres.append(int(nombre_str))
    return nombres

def afficher_solution_unique(i):
    rotation = rotation_liste(mgr, i)
    print(" ".join(map(str, rotation)))

def afficher_solution_multiple(ans):
    minimum = min(ans)
    print(" ".join(list(str(minimum))))

while True:
    try:
        p = lire_entree()
        v = calculer_v(p)
        mv = trouver_max_v(v)
        if compte_max_v(v, mv) > 1:
            indices = indices_max_v(v, mv)
            ans = former_entiers(indices)
            afficher_solution_multiple(ans)
        else:
            i = v.index(mv)
            afficher_solution_unique(i)
    except:
        break