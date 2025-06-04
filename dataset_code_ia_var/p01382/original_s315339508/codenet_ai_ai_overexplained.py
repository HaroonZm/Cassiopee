#!/usr/bin/env python3

# Importation du module itertools afin de profiter de fonctions utilitaires,
# en particulier pour générer toutes les combinaisons possibles d'éléments dans une liste.
import itertools

# Définition de la fonction "greedy" qui prend en paramètre une liste 'a'.
def greedy(a):
    # Exécution d'une boucle tant que le nombre d'éléments dans la liste 'a' est supérieur ou égal à 3.
    # Cela signifie qu'il doit rester au moins 3 éléments pour effectuer l'opération suivante.
    while len(a) >= 3:
        # Vérifie si la somme des avant-derniers éléments de la liste (a[-3] + a[-2])
        # est strictement supérieure au dernier élément de la liste (a[-1]).
        # Les indices négatifs parcourent la liste depuis la fin : -1 est le dernier élément,
        # -2 l'avant-dernier, -3 l'antépénultième.
        if a[-3] + a[-2] > a[-1]:
            # Si la condition précédente est vraie, alors on retire (pop) les trois derniers éléments de la liste 'a'
            # et on les additionne. La méthode 'pop()' retire l'élément à la fin de la liste et le renvoie.
            # L'addition est faite entre les trois valeurs retirées. L'ordre d'évaluation est de droite à gauche.
            return a.pop() + a.pop() + a.pop()
        else:
            # Si la condition n'est pas remplie, on supprime (pop) seulement le dernier élément de la liste 'a'.
            # Ceci permet de réduire la taille de la liste pour réévaluer à la prochaine itération.
            a.pop()

# Définition de la fonction "bruteforce" qui prend une liste 'a' comme paramètre.
def bruteforce(a):
    # Début d'une boucle qui continue tant qu'il y a au moins 3 éléments dans la liste,
    # et que la somme des deux avant-derniers ('a[-3]' et 'a[-2]') est inférieure ou égale au dernier élément ('a[-1]').
    while len(a) >= 3 and a[-3] + a[-2] <= a[-1]:
        # Suppression du dernier élément de la liste, ce qui modifie la liste en place.
        a.pop()
    # Initialisation d'une variable 'result' à zéro pour stocker le meilleur résultat trouvé.
    result = 0
    # Utilisation de itertools.combinations pour générer toutes les combinaisons uniques de 6 éléments
    # (sans répétition, peu importe l'ordre) à partir des 10 derniers éléments de la liste 'a'.
    for b in itertools.combinations(a[-10:], 6):
        # Pour chaque combinaison de 6 éléments, on génère toutes les répartitions possibles de 3 positions (sur 6).
        # Cela donne toutes les manières de diviser 6 éléments en deux groupes de 3.
        for partition in itertools.combinations(range(6), 3):
            # Initialisation de deux listes vides : 'c' et 'd'.
            c, d = [], []
            # Boucle sur tous les indices de la combinaison (0 à 5 inclus car 6 éléments).
            for i in range(6):
                # Si l'indice 'i' fait partie de la 'partition' sélectionnée, on ajoute l'élément correspondant à la liste 'c'.
                if i in partition:
                    c += [b[i]]
                else:
                    # Sinon, on ajoute l'élément à la liste 'd'.
                    d += [b[i]]
            # Après la répartition, on vérifie la condition suivante sur les deux groupes (c et d):
            # Pour chaque groupe, la somme des deux premiers éléments doit être strictement supérieure au 3ème.
            # L'accès c[0], c[1], c[2] suppose que chaque groupe contient exactement 3 éléments.
            if c[0] + c[1] > c[2] and d[0] + d[1] > d[2]:
                # Si les deux sous-ensembles satisfont la condition, on met à jour 'result'
                # par la valeur maximale entre sa valeur actuelle et la somme totale des 6 éléments sélectionnés.
                result = max(result, sum(b))
    # La fonction retourne 'result', qui est le meilleur (maximal) score trouvé par la méthode brute force.
    return result

# Définition de la fonction principale 'solve' qui prend en paramètre la liste 'preserved_a'.
def solve(preserved_a):
    # Initialisation de la variable 'result' à zéro.
    result = 0

    # ------ Approche gloutonne (greedy algorithm) ------
    # On crée une copie de la liste d'origine afin de ne pas la modifier.
    a = list(preserved_a)
    # Application de la fonction 'greedy' sur la liste copiée 'a' pour obtenir la première solution partielle 'x'.
    x = greedy(a)
    # Application de la fonction 'greedy' à nouveau sur la liste 'a' qui a été modifiée par la première opération,
    # afin d'obtenir une seconde solution partielle 'y'.
    y = greedy(a)
    # Si aucune des deux valeurs 'x' ou 'y' n'est nulle (None), 
    # on met à jour 'result' avec la somme de x et y si cette somme est supérieure à la valeur actuelle de 'result'.
    if x is not None and y is not None:
        result = max(result, x + y)

    # ------ Approche exhaustive (brute force) ------
    # On crée une nouvelle copie de la liste d'origine.
    a = list(preserved_a)
    # On applique la fonction 'bruteforce' pour obtenir une solution par recherche exhaustive.
    x = bruteforce(a)
    # On met à jour la valeur du résultat si la nouvelle solution est meilleure.
    result = max(result, x)

    # Retour de la meilleure solution trouvée entre les deux approches.
    return result

# Lecture en entrée du nombre d'éléments dans la séquence.
# La fonction 'input' attend que l'utilisateur saisisse une valeur au clavier (sous forme de chaîne de caractères).
# La fonction 'int' convertit cette chaîne en un entier.
n = int(input())

# Lecture et création de la liste des éléments.
# Pour chaque nombre de 0 à n-1 (grâce à la construction [ ... for _ in range(n) ]),
# on lit une entrée (input), on la convertit en entier, puis on ajoute ce nombre dans la liste.
# On trie ensuite la liste entière par ordre croissant grâce à la fonction 'sorted'.
a = sorted([int(input()) for _ in range(n)])

# On appelle la fonction solve avec la liste ordonnée 'a'.
result = solve(a)

# Affichage du résultat à l'écran. La fonction 'print' affiche la valeur sur la sortie standard.
print(result)