def lire_entiers():
    return map(int, input().split())

def lire_entier():
    return int(input())

def lire_liste_entiers(n):
    valeurs = []
    for _ in range(n):
        valeurs.append(lire_entier())
    return valeurs

def calculer_differences(t):
    v = []
    for i in range(len(t) - 1):
        v.append(calculer_difference(t, i))
    return v

def calculer_difference(t, i):
    return t[i + 1] - t[i] - 1

def trier_decroissant(liste):
    return sorted(liste, reverse=True)

def calculer_resultat(t, v, k):
    return calculer_intervalle(t) - calculer_somme(v, k - 1)

def calculer_intervalle(t):
    return t[-1] - t[0] + 1

def calculer_somme(liste, n):
    return sum(liste[:n])

def afficher_resultat(resultat):
    print(resultat)

def main():
    n, k = lire_entiers()
    t = lire_liste_entiers(n)
    v = calculer_differences(t)
    v = trier_decroissant(v)
    resultat = calculer_resultat(t, v, k)
    afficher_resultat(resultat)

main()