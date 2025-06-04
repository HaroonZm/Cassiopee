#!/usr/bin/env python3

# Importation du module sys pour lire l'entrée standard (stdin)
import sys

# Importation de la fonction accumulate du module itertools
# Cette fonction permet de calculer les sommes cumulées facilement
from itertools import accumulate

# Importation du module math pour utiliser la fonction log2
# log2 permet de récupérer la position du bit le plus élevé à 1 (c'est-à-dire l'ordre de grandeur d'un nombre en base 2)
import math

# Définition de la fonction principale "solve" qui contient la logique du problème
# N : Nombre d'éléments dans la liste a
# K : Nombre de sous-sommes à sélectionner pour maximiser la valeur trouvée
# a : Liste des entiers sur lesquels on travaille
def solve(N: int, K: int, a: "List[int]"):
    # Création d'une liste des sommes préfixes (somme cumulative jusqu'à chaque index)
    # accumulate(a) retourne les sommes cumulées, mais on ajoute 0 au début pour faciliter le calcul des sous-sommes
    accum = [0] + list(accumulate(a))

    # Initialisation d'une liste vide pour stocker toutes les sous-sommes possibles
    sum_list = []

    # Deux boucles imbriquées pour générer toutes les sous-sommes possibles de la liste a
    # La première boucle parcourt les points de départ (i) des sous-tableaux
    for i in range(0, N):
        # La deuxième boucle parcourt les points d'arrivée (j) des sous-tableaux
        # En partant de i+1 pour éviter des sous-tableaux vides
        for j in range(i + 1, N + 1):
            # Calcul de la somme du sous-tableau de a[i] jusqu'à a[j-1] en utilisant les sommes cumulées
            # accum[j] - accum[i] donne la somme du sous-tableau a[i:j]
            sum_list.append(accum[j] - accum[i])

    # Tri de toutes les sous-sommes possibles par ordre décroissant
    sum_list.sort(reverse=True)

    # Recherche du nombre maximal de bits utilisés dans le plus grand élément de sum_list
    # math.log2(x) donne le logarithme en base 2, int(...) donne la partie entière (la position du bit de poids fort)
    # On utilise sum_list[0] après tri décroissant car c'est la sous-somme maximale possible
    max_bit = int(math.log2(sum_list[0]))

    # Initialisation de la variable qui contiendra la réponse finale (le résultat maximisé)
    answer = 0

    # Parcours de tous les bits possibles de l'entier (du bit de poids fort vers le poids faible)
    # On commence par max_bit et on décroit jusqu'à 0 (inclus)
    for i in range(max_bit, -1, -1):

        # Initialisation d'un compteur pour compter combien de sous-sommes ont ce bit activé(=1) en position i
        count = 0

        # Création d'une liste temporaire pour stocker les sous-sommes ayant ce bit à 1
        tmp = []

        # Boucle pour examiner toutes les sous-sommes du tableau current
        for j in range(len(sum_list)):
            # Utilisation d'une opération binaire "AND" entre la sous-somme et 1 décalé de i positions (1 << i)
            # Ceci permet de vérifier si le i-ème bit est activé (=1)
            if sum_list[j] & (1 << i):
                # S'il l'est, on augmente le compteur
                count += 1
                # On ajoute la sous-somme à la liste temporaire tmp
                tmp.append(sum_list[j])

        # Si on a au moins K sous-sommes qui ont le i-ème bit activé,
        # cela signifie qu'on peut maximiser answer en mettant ce bit à 1
        if count >= K:
            # On active (ajoute) ce bit à la réponse finale (answer)
            answer += 2 ** i
            # On remplace la liste sum_list par tmp, réduisant ainsi la suite des sous-sommes considérées
            # Ceci garantit que les bits déjà sélectionnés restent activés dans les prochaines étapes
            sum_list = tmp

    # Affichage du résultat sur la sortie standard (interpreteur ou console)
    print(answer)

    # La fonction ne retourne rien explicitement
    return

# Définition de la fonction main()
# C'est le point d'entrée du programme si exécuté directement
def main():
    # Définition d'une fonction interne "iterate_tokens" qui permet de lire les entrées séparées par espace ou par ligne
    def iterate_tokens():
        # Pour chaque ligne reçue depuis l'entrée standard
        for line in sys.stdin:
            # On parcourt chaque mot (ou nombre) de la ligne, séparé par un espace
            for word in line.split():
                # On "yield" (retourne) chaque entier au fur et à mesure, un à un
                yield word

    # Instanciation de l'itérateur pour consommer l'entrée, c'est une sorte de flux de tokens
    tokens = iterate_tokens()

    # On lit les deux premiers nombres reçus (N et K), en les convertissant en entiers via int()
    N = int(next(tokens))  # Nombre d'éléments du tableau a
    K = int(next(tokens))  # Nombre de sous-tableaux à prendre en compte

    # On lit les N éléments suivants et on les place dans la liste 'a'
    a = [int(next(tokens)) for _ in range(N)]  # Liste de N entiers

    # Appel de la fonction de résolution du problème avec les paramètres lus
    solve(N, K, a)

# Condition qui vérifie si ce script est exécuté comme programme principal (et non importé comme module)
if __name__ == '__main__':
    main()