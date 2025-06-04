def lire_entree():
    return input()

def extraire_nk(entree):
    return map(int, entree.split())

def obtenir_n(entree):
    n, _ = extraire_nk(entree)
    return n

def obtenir_k(entree):
    _, k = extraire_nk(entree)
    return k

def k_est_un(k):
    return k == 1

def calculer_resultat(n, k):
    return n - k - 1 + 1

def afficher_resultat(resultat):
    print(resultat)

def traiter_cas_k_un():
    afficher_resultat(0)

def traiter_cas_general(n, k):
    res = calculer_resultat(n, k)
    afficher_resultat(res)

def main():
    entree = lire_entree()
    n = obtenir_n(entree)
    k = obtenir_k(entree)
    if k_est_un(k):
        traiter_cas_k_un()
    else:
        traiter_cas_general(n, k)

main()