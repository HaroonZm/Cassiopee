#!/usr/bin/env python3

# Importation de la classe defaultdict depuis le module collections.
# defaultdict est une sous-classe de dict qui fournit une valeur par défaut pour les clés inexistantes.
from collections import defaultdict

# Importation de la classe deque depuis le module collections.
# deque (double-ended queue) est une structure de données permettant des insertions/suppressions rapides aux deux extrémités.
from collections import deque

# Importation des fonctions heappush et heappop depuis le module heapq.
# Ces fonctions permettent de manipuler une file de priorité (tas binaire min).
from heapq import heappush, heappop

# Importation du module sys pour accéder à des fonctionnalités dépendantes du système.
import sys

# Importation du module math pour accéder à des fonctions mathématiques standards.
import math

# Importation du module bisect pour la gestion efficace de listes triées.
import bisect

# Importation du module random pour la génération de nombres aléatoires.
import random

# Importation du module itertools pour les outils d’itération.
import itertools

# Changer la limite de récursion maximale du système pour éviter une erreur de récursion profonde.
# sys.setrecursionlimit définit le nombre maximal d'appels récursifs autorisés.
sys.setrecursionlimit(10**5)

# Raccourci pour sys.stdin (flux d’entrée standard, généralement le clavier ou un fichier redirigé).
stdin = sys.stdin

# Création de raccourcis pour la fonction bisect_left et bisect_right du module bisect.
# bisect_left : trouve l'index d'insertion à gauche dans une liste triée.
# bisect_right : trouve l'index d'insertion à droite dans une liste triée.
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right

# Déclaration de fonctions utilitaires rapides pour la lecture d'entrée

# LI() : lit une ligne d'entiers séparés par des espaces et retourne une liste d'entiers.
def LI():
    return list(map(int, stdin.readline().split()))

# LF() : lit une ligne de nombres à virgule flottante et retourne une liste de floats.
def LF():
    return list(map(float, stdin.readline().split()))

# LI_() : lit une ligne d'entiers, décrémente chaque entier de 1 (utile pour les entrées indexées à 1), retourne la liste.
def LI_():
    return list(map(lambda x: int(x)-1, stdin.readline().split()))

# II() : lit une ligne, la convertit en entier et la retourne.
def II():
    return int(stdin.readline())

# IF() : lit une ligne, la convertit en flottant et la retourne.
def IF():
    return float(stdin.readline())

# LS() : lit une ligne d'entrée, la sépare en blocs puis convertit chaque bloc en liste séparée de caractères.
def LS():
    return list(map(list, stdin.readline().split()))

# S() : lit une ligne d'entrée, supprime le retour à la ligne à droite, puis convertit cette ligne en liste de caractères.
def S():
    return list(stdin.readline().rstrip())

# IR(n) : lit n entiers (un par ligne), retourne une liste d'entiers.
def IR(n):
    return [II() for _ in range(n)]

# LIR(n) : lit n lignes, chaque ligne contient des entiers ; retourne une liste de listes d'entiers.
def LIR(n):
    return [LI() for _ in range(n)]

# FR(n) : lit n lignes, chaque ligne est convertie en flottant, retourne la liste.
def FR(n):
    return [IF() for _ in range(n)]

# LFR(n) : lit n lignes, chaque ligne est convertie via LI(), retourne une liste de listes d'entiers.
def LFR(n):
    return [LI() for _ in range(n)]

# LIR_(n) : lit n lignes, chaque ligne d'entiers est décrémentée de 1 ; retourne une liste de listes d'entiers.
def LIR_(n):
    return [LI_() for _ in range(n)]

# SR(n) : lit n lignes, chaque ligne est convertie en liste de caractères (via S()) ; retourne une liste de listes.
def SR(n):
    return [S() for _ in range(n)]

# LSR(n) : lit n lignes, chaque ligne est séparée via LS() ; retourne une liste.
def LSR(n):
    return [LS() for _ in range(n)]

# Déclaration d'une constante entière, usuellement utilisée comme modulo dans de nombreux problèmes (modulo 1e9+7)
mod = 1000000007

# Déclaration d'une constante flottante représentant l'infini (utilisée pour l'initialisation de variables de coût maximal).
inf = float('INF')

# Début de la définition des fonctions correspondant aux différents problèmes (A, B, ...)

# Fonction correspondant au problème A
def A():
    # Lecture d'un entier n depuis l'entrée standard.
    n = II()
    # Lecture d'une liste d'entiers (coûts) via LI() et assignation à p.
    p = LI()
    # Lecture d'une liste d'entiers (temps) via LI() et assignation à t.
    t = LI()
    # Initialisation du tableau dp (programming dynamique) avec la valeur 'inf' sur 100000 éléments.
    # dp[i] représentera le coût minimal pour atteindre un temps total de i.
    dp = [inf] * (10**5)
    # Initialisation du cas de base : temps total 0 coûte 0.
    dp[0] = 0
    # Premier parcours : on analyse tous les temps possibles (de 0 à 99999 inclus).
    for i in range(10**5):
        # Pour chaque tâche possible, on regarde combien de temps elle prend et son prix.
        for num, ti in enumerate(t):
            # Si on peut soustraire le temps de la tâche courante (c’est-à-dire, si on reste dans la plage 0-99999)
            if i - ti >= 0:
                # On prend le minimum entre la valeur courante de dp[i] et le coût d'atteindre i-ti + le coût pour cette tâche.
                dp[i] = min(dp[i], dp[i - ti] + p[num])
    # Second parcours : on s'assure que les coûts sont non-croissants de droite à gauche.
    # Pour tout i de 99998 à 0, on garantit que dp[i-1] <= dp[i]
    for i in range(10**5-1, 0, -1):
        dp[i - 1] = min(dp[i], dp[i - 1])
    # Affichage du coût minimal pour le temps n.
    print(dp[n])
    return

# Fonction correspondant au problème B
def B():
    # Définition (locale) de la fonction yaku(n) qui calcule le nombre de diviseurs de n.
    def yaku(n):
        # Initialisation du compteur de diviseurs à 0.
        res = 0
        # Cas particulier : si n vaut 0, on retourne 0 immédiatement car 0 n’a pas de diviseur.
        if n == 0:
            return 0
        # itération de 1 jusqu'à la racine carrée de (n-1) inclue.
        # Cela parcourt tous les candidats à diviseur jusqu'à sqrt(n-1).
        for i in range(1, int(math.sqrt(n-1)) + 1):
            # Si i est un diviseur de n, alors on sait que n % i == 0.
            if n % i == 0:
                # On ajoute 2 car i et n//i sont tous deux des diviseurs (à l’exception du carré traité après).
                res += 2
        # Si la racine carrée de n est un entier, alors on a compté le carré deux fois, on l’ajoute une fois.
        if float.is_integer(math.sqrt(n)):
            res += 1
        # Retourne le nombre total de diviseurs.
        return res
    # Lecture d’un entier q depuis l’entrée standard, c’est le nombre de requêtes.
    q = II()
    # Pré-calcul du nombre de diviseurs pour tous les entiers de 0 à 100000 inclus, via une compréhension de liste.
    ya = [yaku(i) for i in range(10 ** 5 + 1)]
    # Mettre à 0 le nombre de diviseurs de 0, cas spécial.
    ya[0] = 0
    # Pour chaque entier i de 1 à 100000 inclus
    for i in range(1,10 ** 5 + 1):
        # Si le nombre de diviseurs de i est supérieur ou égal à 5...
        if ya[i] >= 5:
            # Remplacer ya[i] par 1 (marquer ce nombre comme ayant >=5 diviseurs)
            ya[i] = 1
        else:
            # Sinon, mettre 0 (moins de 5 diviseurs)
            ya[i] = 0
        # Cumuler le résultat courant ya[i] avec le précédent ya[i-1] afin d’obtenir le préfixe cumulatif.
        ya[i] += ya[i - 1]
    # Pour chacune des q requêtes...
    for i in range(q):
        # Lire l’entier n pour la requête i.
        n = II()
        # Afficher la valeur cumulée ya[n], c’est-à-dire le nombre d'entiers ≤ n ayant au moins 5 diviseurs.
        print(ya[n])
    return

# Fonction correspondant au problème C (non encore implémentée, corps vide)
def C():
    return

# Fonction correspondant au problème D (non encore implémentée, corps vide)
def D():
    return

# Fonction correspondant au problème E (non encore implémentée, corps vide)
def E():
    return

# Fonction correspondant au problème F (non encore implémentée, corps vide)
def F():
    return

# Fonction correspondant au problème G (non encore implémentée, corps vide)
def G():
    return

# Fonction correspondant au problème H (non encore implémentée, corps vide)
def H():
    return

# Fonction principale activant la fonction de résolution choisie lors de l’exécution du script
if __name__ == '__main__':
    # Appel uniquement de la fonction B(), qui traite le problème B.
    B()