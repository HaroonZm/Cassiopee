def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def calculer_max(liste):
    return max(liste)

def calculer_min(liste):
    return min(liste)

def calculer_difference_max_min(max_val, min_val):
    return max_val - min_val

def est_difference_pair(diff):
    return diff % 2 == 0

def calculer_resultat(diff):
    if est_difference_pair(diff):
        return diff // 2
    else:
        return (diff // 2) + 1

def afficher_resultat(resultat):
    print(resultat)

def main():
    N = lire_entier()
    a = lire_liste_entiers()
    max_val = calculer_max(a)
    min_val = calculer_min(a)
    diff = calculer_difference_max_min(max_val, min_val)
    resultat = calculer_resultat(diff)
    afficher_resultat(resultat)

main()