def lire_entree():
    try:
        return input()
    except EOFError:
        return None

def lire_liste():
    return raw_input().split()

def convertir_en_entier(liste_str):
    return list(map(int, liste_str))

def trier_liste(L):
    return sorted(L)

def cumul_sommes(L):
    for i in range(1, len(L)):
        L[i] += L[i-1]
    return L

def somme_liste(L):
    return sum(L)

def boucle_principale():
    while True:
        n_str = lire_entree()
        if n_str is None:
            break
        n = int(n_str)
        L_str = lire_liste()
        L_int = convertir_en_entier(L_str)
        L_triée = trier_liste(L_int)
        L_cum = cumul_sommes(L_triée)
        s = somme_liste(L_cum)
        print(s)

boucle_principale()