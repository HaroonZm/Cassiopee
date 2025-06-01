def lire_entier():
    return int(input())

def calculer_nouvelle_valeur(a):
    return a * 1.05

def est_multiple_de_mille(n):
    return n % 1000 == 0

def ajuster_au_mille_superieur(n):
    return (n + 1000) - (n % 1000)

def traiter_valeur(a):
    a = calculer_nouvelle_valeur(a)
    if not est_multiple_de_mille(int(a)):
        a = ajuster_au_mille_superieur(int(a))
    return a

def boucle_principale(a, j):
    for _ in range(j):
        a = traiter_valeur(a)
    return a

def afficher_resultat(a):
    print(int(a))

def main():
    a = 100000
    j = lire_entier()
    a = boucle_principale(a, j)
    afficher_resultat(a)

main()