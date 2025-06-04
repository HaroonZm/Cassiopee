import sys
from collections import Counter

def lire_liste_entiers():
    return list(map(int, input().split()))

def lire_entier():
    return int(input())

def lire_liste_chaines():
    return input().split()

def lire_chaine():
    return input()

def verifier_possibilite_chemin_special():
    etat_possible = 'POSSIBLE'
    etat_impossible = 'IMPOSSIBLE'
    numero_premier_noeud, numero_dernier_noeud = lire_liste_entiers()
    compteur_connections_vers_extremites = Counter()
    resultat_final = etat_impossible

    for index_voie in range(numero_dernier_noeud):
        numero_noeud_debut, numero_noeud_fin = lire_liste_entiers()
        
        if numero_noeud_debut == 1:
            compteur_connections_vers_extremites[numero_noeud_fin] += 1
            
        if numero_noeud_fin == numero_premier_noeud:
            compteur_connections_vers_extremites[numero_noeud_debut] += 1
        
        if (compteur_connections_vers_extremites[numero_noeud_debut] == 2 or 
            compteur_connections_vers_extremites[numero_noeud_fin] == 2):
            resultat_final = etat_possible

    return resultat_final

def programme_principal():
    resultat_possibilite = verifier_possibilite_chemin_special()
    print(resultat_possibilite)

if __name__ == '__main__':
    programme_principal()