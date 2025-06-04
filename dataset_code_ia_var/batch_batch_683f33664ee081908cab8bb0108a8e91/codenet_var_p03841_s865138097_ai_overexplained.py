#!usr/bin/env python3

# Importation de modules nécessaires

# 'defaultdict' permet de créer un dictionnaire avec une valeur par défaut si la clé n'existe pas.
# 'deque' est une file à double extrémité utile pour des opérations rapides d'ajout/suppression aux deux bouts.
from collections import defaultdict, deque

# 'heappush' et 'heappop' implémentent une file de priorité (tas binaire).
from heapq import heappush, heappop

# 'sys' donne accès aux objets utilisés ou maintenus par l'interpréteur.
import sys

# 'math' donne accès à des fonctions mathématiques comme sqrt, sin, etc.
import math

# 'bisect' permet de manipuler des listes triées efficacement, comme l'insertion ou la recherche d'indices.
import bisect

# 'random' permet de générer des nombres aléatoires ou de mélanger des listes.
import random

# ---------- Définition de fonctions utilitaires pour lire l'entrée rapidement ----------

def LI():
    """
    Lit une ligne de l'entrée standard, la découpe en éléments par rapport à l'espace,
    convertit chaque élément en entier, et retourne une liste de ces entiers.
    Exemple d'utilisation : si l'entrée est "5 8 13", LI() retournera [5, 8, 13].
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Lit une ligne de l'entrée standard, la convertit en entier, puis la retourne.
    Par exemple, si la saisie est "42", I() retourne 42.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne de l'entrée standard, la découpe par espaces,
    puis convertit chaque élément en une liste de caractères.
    Retourne une liste de listes.
    Exemple : "abc def" -> [['a','b','c'], ['d','e','f']]
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Lit une ligne de texte à l'entrée, la convertit en liste de caractères.
    Si le dernier caractère est un saut de ligne '\n', il est retiré pour ne garder que la donnée utile.
    Retourne la liste de caractères de la ligne lue.
    """
    res = list(sys.stdin.readline())
    if res[-1] == "\n":    # Vérifie et supprime le saut de ligne s'il est présent
        return res[:-1]
    return res

def IR(n):
    """
    Lit n lignes, chacune étant convertie en un entier via la fonction I(), et retourne la liste de ces entiers.
    """
    return [I() for i in range(n)]

def LIR(n):
    """
    Lit n lignes, chacune étant convertie en une liste d'entiers via la fonction LI(), puis retourne la liste de ces listes.
    """
    return [LI() for i in range(n)]

def SR(n):
    """
    Lit n lignes, chacune étant convertie en une liste de caractères via la fonction S(), puis retourne la liste de ces listes.
    """
    return [S() for i in range(n)]

def LSR(n):
    """
    Lit n lignes, chacune étant convertie en une liste de listes de caractères via la fonction LS(), puis retourne une liste de listes de listes.
    """
    return [LS() for i in range(n)]

# ---------- Paramètres globaux ----------

# Augmente la limite de récursivité maximale.
# Utile en cas d'appels récursifs profonds pour éviter l'erreur RecursionError.
sys.setrecursionlimit(1000000)  # Définit la profondeur maximale de récursion à 1 000 000.

# Définition d'une constante très utilisée en programmation compétitive, particulièrement pour les opérations modulo.
mod = 1000000007  # Ce nombre est un nombre premier grand, utilisé pour éviter les débordements.

# ---------- Définition des différentes fonctions de résolution de problèmes ----------

# Fonction A (exemple de résolution d'un problème sur deux entiers x et y)
def A():
    # La fonction commence par lire deux entiers sur une seule ligne de saisie.
    x, y = LI()
    # On considère tous les cas possibles de signes pour x et y et on génère un résultat en fonction de leurs signes et valeurs.
    if x < 0:        
        if y < 0:    # Les deux sont négatifs
            if x < y:
                print(y - x)  # Cas où x est "plus petit" (plus négatif)
            else:
                print(x - y + 2)  # Cas opposé, l'opération implique un 'retour' par 0 (donc +2)
        else:         # x est négatif, y est positif ou nul
            if abs(x) < y:
                print(y - abs(x) + 1)
            else:
                print(-y - x + (y > 0))  # On ajoute 1 si y est strictement positif
    else:
        if y < 0:    # x positif ou nul, y négatif
            if x < abs(y):
                print(abs(y) - x + 1)
            else:
                print(x + y + 1)
        else:        # x et y positifs
            if x < y:
                print(y - x)  # y plus grand que x, donc simplement y-x opérations suffisantes
            else:
                print(x - y + (x > 0) + (y > 0))  # Ajout de 1 ou 2 selon si x ou y sont>0

    return

# Fonction B (modèle vide pour un problème 'B')
def B():
    return

# Fonction C : Problème utilisant des listes et des opérations sur les éléments
def C():
    # Lit une ligne d'entrée et la convertit en tableau d'entiers.
    a = LI()
    # Vérifie que certains indices de la liste a contiennent des valeurs strictement positives
    if a[0] > 0 and a[3] > 0 and a[4] > 0:
        # Si c'est le cas, calcule deux expressions candidates et affiche la plus grande.
        # Utilise la division entière pour compter des paires et ajoute une correction selon le second cas
        print(max(
            2 * (a[0] // 2) + a[1] + 2 * (a[3] // 2) + 2 * (a[4] // 2),
            2 * ((a[0] - 1) // 2) + a[1] + 2 * ((a[3] - 1) // 2) + 2 * ((a[4] - 1) // 2) + 3
        ))
    else:
        # Si la condition n'est pas vérifiée, affiche simplement l'expression de base sans correction
        print(
            2 * (a[0] // 2) + a[1] + 2 * (a[3] // 2) + 2 * (a[4] // 2)
        )
    return

# Fonction D : Cette fonction effectue une opération algorithmique complexe sur une liste d'entiers.
def D():
    # Lit un entier à l'entrée, qui définit la taille de la suite à traiter.
    n = I()
    
    # Lit une ligne de n entiers.
    x = LI()
    
    # Construction d'une liste de tuples (valeur, index) pour trier selon les valeurs tout en gardant l'index original.
    f = [(x[i], i) for i in range(n)]
    
    # Trie la liste de tuples par ordre croissant selon le premier élément (la valeur de x[i])
    f.sort()
    
    # Initialise une liste vide b, qui sera remplie selon une règle détaillée ci-dessous.
    b = []
    
    # Première boucle pour remplir b avec (i+1) répété i fois pour chaque élément trié.
    for xi, i in f:
        # Ajoute dans b la valeur (i+1), répété i fois. Cela utilise la multiplication de listes en Python.
        b += [i + 1] * i
    
    # Deuxième boucle pour remplir b avec (i+1) répété (n-i-1) fois pour chaque élément.
    for xi, i in f:
        b += [i + 1] * (n - i - 1)
    
    # ans sera la variable résultat qui va contenir la séquence générée au final.
    ans = []
    
    # l servira comme pointeur sur la liste b pour suivre l'état de construction de ans.
    l = 0

    # Pour chaque élément dans la liste triée, ajoute des éléments à ans pour atteindre la contrainte xi.
    for xi, i in f:
        # Tant que la taille actuelle de ans (+1 car on s'apprête à rajouter) est inférieure à xi (but à atteindre)
        while len(ans) + 1 < xi:
            # Si on a déjà utilisé tous les éléments de b, on arrête.
            if l == len(b):
                break
            # Ajoute le l-ième élément de b à ans et incrémente l.
            ans.append(b[l])
            l += 1
        # Ajoute toujours (i+1) à ans (rappel : i = index d'origine dans x)
        ans.append(i + 1)

    # Ajoute à ans tous les éléments de b restants après l (si il en reste)
    for i in range(l, len(b)):
        ans.append(b[i])

    # f sera utilisée ici comme un compteur pour valider la séquence générée.
    f = [0] * n

    # Cette boucle va vérifier que la position à laquelle chaque 'index' apparaît dans ans est conforme à la valeur d'origine.
    for i in range(len(ans)):
        ai = ans[i] - 1   # On obtient l'indice associé en décrémentant de 1 (car on ajoutait +1 plus haut)
        if f[ai] == ai:
            # Pour valider, on vérifie que la position dans ans plus 1 est égale à x[ai]
            if i + 1 != x[ai]:
                # Si ce n'est pas le cas, on affiche 'No' et on sort immédiatement.
                print("No")
                return
        # On incrémente le compteur pour l'indice courant.
        f[ai] += 1

    # Si la séquence générée respecte les contraintes, on affiche 'Yes'
    print("Yes")
    # Affiche tous les éléments de ans séparés par un espace.
    print(*ans)
    return

# Fonction E (modèle vide pour un problème 'E')
def E():
    return

# Fonction F (modèle vide pour un problème 'F')
def F():
    return

# ---------- Exécution principale du programme ----------

# Si ce script est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    # Appelle la fonction D. C'est donc ce problème qui sera résolu avec l'entrée donnée.
    D()