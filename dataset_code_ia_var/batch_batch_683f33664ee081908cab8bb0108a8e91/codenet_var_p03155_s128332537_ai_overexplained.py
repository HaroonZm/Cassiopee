# Importation de divers modules utiles dans de nombreux scénarios.
# 'collections' fournit des structures de données alternatives (deque, Counter, etc.)
# 'atexit' permet d’enregistrer des fonctions à exécuter à la sortie du programme.
# 'math' offre de nombreuses fonctions mathématiques standards.
# 'sys' permet d’interagir directement avec l’interpréteur Python (comme la redirection d'entrée/sortie, les paramètres système, etc.)
# 'bisect' fournit des algorithmes pour insérer et rechercher efficacement dans des listes triées.
import collections
import atexit
import math
import sys
import bisect

# Modification de la limite de récursion pour permettre des appels récursifs très profonds.
# La valeur 1000000 est très élevée et dépasser cette limite conduira à une erreur de dépassement de pile (stack overflow).
sys.setrecursionlimit(1000000)

# Définition d’une fonction utilitaire pour lire une ligne de l’entrée,
# séparer cette ligne selon les espaces, convertir ces morceaux en entiers
# et retourner une liste d’entiers.
def getIntList():
    # 'input()' lit une ligne depuis l'entrée standard, comme le clavier ou un fichier redirigé.
    # 'split()' découpe la ligne selon les espaces (par défaut).
    # 'map(int, ...)' convertit chaque morceau en un entier.
    # 'list(...)' convertit le résultat en une liste Python.
    return list(map(int, input().split()))

# Bloc 'try/except' pour détecter si le module 'numpy' est installé dans l'environnement.
# Si l'import de NumPy réussit, on définit la fonction 'dprint' qui sert à afficher des messages de debug.
# Si l'import échoue (ModuleNotFoundError ou toute autre erreur), on définit une 'dprint' factice qui ne fait rien.
try:
    # On essaie d'importer 'numpy'. Si cela fonctionne, nous sommes en "mode debug".
    import numpy

    # Définition de la fonction de debug. Elle imprime ce qu’on lui passe en arguments, vers stderr,
    # c'est-à-dire la sortie d’erreurs, pas la sortie standard.
    # Cela signifie que les messages de debug ne rentreront pas en conflit avec le 'print' standard.
    def dprint(*args, **kwargs):
        # On utilise un print commenté qui montre qu'on pourrait accepter des kwargs,
        # mais ici on utilise seulement l'impression des arguments vers sys.stderr.
        # sys.stderr est habituellement utilisé pour des messages d’erreur et de debug.
        print(*args, file=sys.stderr)
    # On affiche un message de debug pour signaler que le mode de debug (avec numpy) est actif.
    dprint('debug mode')
except Exception:
    # Si une erreur survient (par exemple, si numpy n’est pas installé), on définit dprint comme une fonction qui ne fait rien.
    def dprint(*args, **kwargs):
        pass

# Déclaration et initialisation de deux variables entières :
# Ces variables sont utilisées pour déterminer si l’entrée et/ou la sortie doivent être redirigées vers des fichiers.
inId = 0
outId = 0

# Si 'inId' est strictement supérieur à 0, on redirige l’entrée standard (sys.stdin)
# vers un fichier d’entrée nommé "input#.txt", où # est la valeur de inId.
if inId > 0:
    # Affichage optionnel en debug pour signaler la redirection de l’entrée.
    dprint('use input', inId)
    # 'open' ouvre le fichier en mode lecture ('r').
    # sys.stdin est alors remplacé : toutes les prochaines lectures via input() iront chercher dans ce fichier.
    sys.stdin = open('input' + str(inId) + '.txt', 'r')

# Si 'outId' est strictement supérieur à 0, on redirige la sortie standard (sys.stdout)
# vers un fichier de sortie nommé "stdout#.txt", où # est la valeur de outId.
if outId > 0:
    # Affichage optionnel en debug pour signaler la redirection de la sortie.
    dprint('use output', outId)
    # 'open' ouvre le fichier en mode écriture ('w') et remplace sys.stdout :
    # les instructions print écriront ainsi dans ce fichier.
    sys.stdout = open('stdout' + str(outId) + '.txt', 'w')
    # On enregistre une fonction à exécuter automatiquement à la fin du programme (via atexit)
    # qui fermera proprement le fichier de sortie.
    atexit.register(lambda: sys.stdout.close())

# Lecture de N depuis l’entrée : la taille d’un grand carré, ou d’une grille.
# 'getIntList()' renvoie une liste, le ',' après N force le déballage du premier (et unique) élément.
N, = getIntList()  # Par exemple, si la ligne est "10", alors N vaudra 10.

# Lecture de H depuis l’entrée : la hauteur d’un sous-rectangle/rectangle plus petit à placer dans la grille.
H, = getIntList()  # Ex : si la ligne entrée vaut "2", H prendra la valeur 2.

# Lecture de W depuis l’entrée : la largeur d’un sous-rectangle/rectangle plus petit.
W, = getIntList()

# Initialisation d’une variable de résultat à 0. Ce sera typiquement le compteur demandé par l’énoncé.
r = 0

# Calcul du nombre de manières de placer un rectangle HxW dans un carré N×N sans sortir du bord.
# - (N-H+1) : nombre de positions verticales possibles (pour la première ligne du sous-rectangle).
# - (N-W+1) : nombre de positions horizontales possibles.
# L’expression donne donc le nombre total d’encastrements possibles.
r += (N - H + 1) * (N - W + 1)

# On affiche finalement la valeur calculée de r. C’est la sortie principale du programme.
print(r)