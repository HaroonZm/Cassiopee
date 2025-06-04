# Importation de la fonction setrecursionlimit depuis le module sys
# Cela permet de modifier la limite maximale de profondeur de la récursion, c'est-à-dire combien de fois une fonction peut s'appeler elle-même avant de provoquer une erreur.
from sys import setrecursionlimit

# On augmente la limite de récursion à un million (10^6)
# Ceci est important spécialement si la fonction récursive va s'appeler très profondément pour de grandes entrées
setrecursionlimit(10 ** 6)

# Définition de la fonction floor_sum avec quatre paramètres :
# n : nombre d'entiers
# m : modulateur
# a, b : coefficients de la fonction de somme
def floor_sum(n, m, a, b):
    # Initialisation de la variable de résultat ans à zéro.
    ans = 0

    # Si a est supérieur ou égal à m, on peut simplifier une partie du calcul en utilisant la division entière.
    # En effet, chaque a entier apporte (a // m) à chaque term de la somme.
    if a >= m:
        # Additionne à ans la somme arithmétique résultante due à la partie entière de la division de a par m
        # (n-1) * n // 2 est la somme des entiers de 0 à n-1 (formule de la somme d'une suite arithmétique)
        # Cette quantité est multipliée par (a // m), puis ajoutée à ans
        ans += (n - 1) * n * (a // m) // 2
        # Mise à jour de a en le remplaçant par le reste de sa division par m
        # Cela permet de réduire le problème pour qu'a soit strictement inférieur à m
        a %= m

    # Si b est supérieur ou égal à m, on peut également simplifier une partie du calcul
    if b >= m:
        # Chaque unité de b entier (b // m) est ajoutée n fois, car il apparaît dans chaque terme
        ans += n * (b // m)
        # Mise à jour de b en gardant seulement le reste de la division de b par m
        b %= m

    # Calculer la valeur maximale de y = (a * x + b) // m pour x allant de 0 à n-1.
    # Ceci donne le plus grand entier y qui peut apparaître dans la somme.
    y_max = (a * n + b) // m

    # Calculer x_max, qui représente le plus grand x pour lequel (a * x + b) // m est encore égal à y_max
    # On trouve le x correspondant à y_max et on soustrait b pour ajuster la borne
    x_max = y_max * m - b

    # Si y_max est égal à 0, il ne reste rien à ajouter, donc on retourne la valeur de ans
    if y_max == 0:
        return ans

    # Ajout à ans de la contribution des termes où (a * x + b) // m == y_max
    # On calcule combien de tels termes existent et multiplie par y_max.
    # (n - (x_max + a - 1) // a) donne le nombre d'x restants
    ans += (n - (x_max + a - 1) // a) * y_max

    # Appel récursif pour gérer la suite du problème, mais avec des paramètres adaptés :
    # - Le nouveau n devient y_max
    # - Le nouveau m devient a
    # - Le nouveau a devient m (échange des rôles)
    # - Le nouveau b est ajusté avec ((a - x_max % a) % a) pour décaler correctement la récurrence
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    # Retour de la variable ans, qui contient la valeur finale du calcul
    return ans

# Lecture des données d'entrée :
# La fonction open(0) ouvre le 'stdin' (entrée standard) pour la lecture.
# read() lit tout le contenu d'un coup, split() sépare les éléments selon les espaces/blancs
# map(int, ...) convertit chaque chaîne de texte en entier
T, *queries = map(int, open(0).read().split())

# La variable T contient le nombre de cas de test.
# La variable queries contient la liste plate de tous les entiers des requêtes restantes.

# On traite chaque cas de test. Chaque requête contient 4 éléments (n, m, a, b).
# [iter(queries)] * 4 crée un itérateur multiple, permettant de regrouper les entiers 4 par 4.
# zip(...) regroupe chaque ensemble de 4 entiers pour former une requête complète.
for q in zip(*[iter(queries)] * 4):
    # On appelle la fonction floor_sum avec les paramètres de la requête, et on affiche le résultat.
    print(floor_sum(*q))