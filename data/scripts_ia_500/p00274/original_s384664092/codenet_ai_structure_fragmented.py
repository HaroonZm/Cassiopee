def lire_nombre():
    return int(input())

def lire_liste(n):
    return list(map(int, input().split()))

def contient_valeur_superieure_ou_egale_a_2(liste):
    return max(liste) >= 2

def compter_zero(liste):
    return liste.count(0)

def afficher_resultat_ou_na(n, liste):
    if not contient_valeur_superieure_ou_egale_a_2(liste):
        afficher_na()
    else:
        t = compter_zero(liste)
        afficher_resultat(n, t)

def afficher_na():
    print('NA')

def afficher_resultat(n, t):
    print(n - t + 1)

def boucle_principale():
    while True:
        n = lire_nombre()
        if condition_arret(n):
            break
        s = lire_liste(n)
        afficher_resultat_ou_na(n, s)

def condition_arret(n):
    return n == 0

boucle_principale()