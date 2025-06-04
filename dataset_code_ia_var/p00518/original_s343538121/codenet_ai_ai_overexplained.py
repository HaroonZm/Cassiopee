import sys  # Importe le module sys pour gérer les arguments du script et d'autres fonctionnalités système

from collections import Counter  # Importe Counter pour compter facilement les objets dans une collection
from itertools import product  # Importe product pour créer les combinaisons de produits cartésiens

def solve(n, data):
    # Initialisation de l'état possible avec un dictionnaire Counter
    # La clé (1, 0, 0) indique qu'uniquement 'J' (le patron) est présent au début, aucun 'O' ni 'I'
    # Le Counter agit comme un dictionnaire pour compter combien de façons chaque état peut être atteint
    status = Counter({(1, 0, 0): 1})

    # Parcourir chaque caractère du planning (data)
    for ch in data:
        # Crée un nouveau Counter pour l'état suivant
        u = Counter()
        # Pour chaque combinaison possible de présence de 'J', 'O', et 'I' (0 = absent, 1 = présent)
        # Ceci produit 8 combinaisons possibles: (0,0,0), (0,0,1), ..., (1,1,1)
        for j, o, i in product((0, 1), repeat=3):
            # On vérifie si la personne correspondant au jour est présente dans cette combinaison
            # On utilise un dictionnaire temporaire pour accéder à la présence selon le caractère du jour
            # { 'J': j, 'O': o, 'I': i }[ch] retourne True (1) si la personne ch (du jour) est dans la team pour cette combinaison
            if {'J': j, 'O': o, 'I': i}[ch]:
                # Pour chaque état précédent (clé k, valeur v) qui peut conduire au nouvel état
                for k, v in status.items():
                    # Décompose l'état précédent, où pj, po, pi sont la présence de chacun ('J','O','I') la veille
                    pj, po, pi = k
                    # Vérifier s'il y a au moins une personne en commun avec la veille
                    # C'est-à-dire, on vérifie que la composition d'aujourd'hui (j,o,i) et la veille (pj,po,pi)
                    # ont au moins un 1 à la même position (pour garantir que l'équipe est "liée" d'un jour au suivant)
                    if any([(j and pj), (o and po), (i and pi)]):
                        # Si oui, alors on ajoute le nombre de façons d'arriver à ce nouvel état
                        # à celui déjà possible dans u pour cette combinaison
                        u[(j, o, i)] += v
        # Après avoir examiné toutes les combinaisons possibles, on met à jour le status
        # Aussi, on applique l'opération modulo 10007 comme spécifié nécessaire pour garder les nombres petits
        status = Counter({k: v % 10007 for k, v in u.items()})
    # À la fin, le nombre total de manières possibles est la somme des valeurs de status
    # On applique encore modulo 10007 selon les exigences du problème
    return sum(status.values()) % 10007

def main(args):
    # Lis la première ligne en tant qu'entier : nombre de jours (n)
    n = int(input())
    # Lis la seconde ligne comme une string : le planning des jours (data)
    data = input()
    # Appelle la fonction 'solve' pour trouver la solution au problème
    ans = solve(n, data)
    # Affiche la réponse (nombre de façons modulo 10007)
    print(ans)

# Point d'entrée standard d'un script Python
if __name__ == '__main__':
    # Appelle la fonction main avec les arguments de la ligne de commande sauf le nom du script
    main(sys.argv[1:])