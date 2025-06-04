#!/usr/bin/env python

# Importation du module deque depuis collections. 'deque' est une structure de données de type file (queue) ou pile (stack).
from collections import deque

# Importation du module itertools dans le namespace court 'it', permettant l'utilisation de fonctions avancées pour les itérables.
import itertools as it

# Importation du module sys pour accéder à des fonctions spécifiques telles que l'accès à la limite de récursion ou aux entrées/sorties système.
import sys

# Importation du module math pour utiliser des fonctions mathématiques, bien que dans ce script il n'est pas utilisé explicitement.
import math

# Modification de la limite de récursion du système afin d'éviter qu'une éventuelle récursion profonde ne provoque une erreur.
# 10 000 000 est un nombre beaucoup plus élevé que la limite par défaut, à utiliser avec prudence.
sys.setrecursionlimit(10000000)

# Python 2 : Lecture d'une entrée utilisateur définissant le nombre de cas de test à traiter.
T = input()  # 'input()' évalue l'entrée comme du code, donc il faut entrer un entier par exemple 2.

# Boucle principale pour traiter chaque cas de test individuellement. 
# 'loop' est utilisé comme variable d'itération, variant de 0 à T-1.
for loop in range(T):

    # Lecture de la valeur N qui représente probablement une taille ou un paramètre du problème.
    N = input()  # N doit être entré comme un entier.

    # Lecture de la chaîne S. 'raw_input()' lit la ligne de texte exactement comme elle est saisie (sans évaluation).
    S = raw_input()

    # Création d'une nouvelle chaîne S1 :
    # - Ajoute un caractère 'N' au début.
    # - Prend les 2*N premiers caractères de S avec la notation de slicing S[:N * 2].
    # - Ajoute un caractère 'N' à la fin.
    # Cela crée une chaîne qui contient les N paires de deux caractères de S, encadrées par 'N'.
    S1 = 'N' + S[:N * 2] + 'N'

    # Création d'une seconde chaîne S2 :
    # - Ajoute un caractère 'N' au début.
    # - Prend la portion de S commençant à l'index 2*N jusqu'à la fin avec S[N * 2:].
    # - Ajoute un caractère 'N' à la fin.
    # Cela correspond à une seconde partie de S, également encadrée.
    S2 = 'N' + S[N * 2:] + 'N'

    # Initialisation de sx1 et sx2 avec une valeur très grande (100000).
    # Ces variables représentent probablement les indices minimums (par exemple, des plus petits indices trouvés).
    sx1 = sx2 = 100000

    # Initialisation de gx1 et gx2 à -1.
    # Ces variables représentent probablement les indices maximums (derniers indices trouvés).
    gx1 = gx2 = -1

    # Initialisation du compteur d'une valeur nommée 'ans' à 0.
    # Celui-ci est utilisé pour stocker des incréments basés sur des conditions rencontrées dans la boucle suivante.
    ans = 0

    # Une boucle for qui va de 0 à N inclus, donc (N + 1) itérations.
    # L'indice 'i' sert à parcourir les différents points ou groupes de caractères, indexés par les transformations des chaînes S1 et S2.
    for i in range(N + 1):

        # Vérifie si, dans S1, soit la position 2*i soit la position 2*i + 1 (donc, la paire d'indices pour i) contient le caractère 'Y'.
        # Si c'est le cas, on effectue plusieurs opérations :
        if S1[i * 2] == 'Y' or S1[i * 2 + 1] == 'Y':

            # On incrémente la réponse de 1, car une condition spéciale est remplie.
            ans += 1

            # On met à jour sx1 afin de retenir le plus petit indice i où la condition précédente est remplie.
            sx1 = min(sx1, i)

            # On stocke le dernier indice i où la condition est remplie, grimpant à chaque fois que le test est vrai.
            gx1 = i

        # Même logique, mais cette fois pour la chaîne S2.
        # On vérifie la paire S2[2*i] et S2[2*i+1].
        if S2[i * 2] == 'Y' or S2[i * 2 + 1] == 'Y':

            # Incrémentation de la variable réponse.
            ans += 1

            # Mémorisation du plus petit indice satisfaisant la condition.
            sx2 = min(sx2, i)

            # Mémorisation du plus grand indice testé (à chaque réussite, l'indice courant écrase l'ancien).
            gx2 = i

    # Après la boucle, on compare les indices minimums : si le minimum de la première séquence est plus grand que celui de la seconde,
    # on incrémente 'ans' de 1.
    if sx1 > sx2:
        ans += 1

    # Ensuite, on vérifie si le maximum de la première séquence est inférieur au maximum de la seconde. Si oui, on augmente également 'ans'.
    if gx1 < gx2:
        ans += 1

    # Affichage du résultat final pour ce cas de test, qui est N additionné à la valeur de 'ans'.
    # En Python 2, la syntaxe 'print' n'exige pas de parenthèses.
    print N + ans