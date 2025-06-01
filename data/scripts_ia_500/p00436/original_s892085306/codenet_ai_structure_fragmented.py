def lire_entier():
    return int(input())

def lire_liste_entiers(n):
    result = []
    for _ in range(n):
        result.append(int(input()))
    return result

def initialiser_paquet(n):
    return [i for i in range(1, n * 2 + 1)]

def separer_cartes(n, cartes):
    c1 = cartes[:n]
    c2 = cartes[n:]
    return c1, c2

def entrelacer_cartes(c1, c2, n):
    tmp = []
    for i in range(n):
        tmp.append(c1[i])
        tmp.append(c2[i])
    return tmp

def deplacer_cartes(cartes, k):
    return cartes[k:] + cartes[:k]

def traiter_ks(n, ks, cartes):
    for k in ks:
        if k == 0:
            c1, c2 = separer_cartes(n, cartes)
            cartes = entrelacer_cartes(c1, c2, n)
        else:
            cartes = deplacer_cartes(cartes, k)
    return cartes

def afficher_cartes(cartes):
    for v in cartes:
        print v

def main():
    n = lire_entier()
    m = lire_entier()
    ks = lire_liste_entiers(m)
    cartes = initialiser_paquet(n)
    cartes = traiter_ks(n, ks, cartes)
    afficher_cartes(cartes)

main()