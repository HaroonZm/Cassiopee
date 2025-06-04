import itertools  # Importe le module 'itertools', qui fournit des fonctions créant des itérateurs pour un traitement efficace des boucles.
import math       # Importe le module 'math', qui offre des fonctions mathématiques comme sqrt, log, etc.
import sys        # Importe le module 'sys', qui permet d'interagir avec l'interpréteur Python et de manipuler des aspects système.
import heapq      # Importe le module 'heapq', qui fournit des fonctions pour créer et manipuler des tas binaires (heaps).
from collections import Counter  # Importe la classe 'Counter' du module 'collections', qui compte les éléments dans des objets itérables.
from collections import deque    # Importe la classe 'deque' pour créer des files d'attente à accès rapide en FIFO/LIFO.
from fractions import gcd        # Importe la fonction gcd (greatest common divisor) pour calculer le plus grand commun diviseur de deux nombres.
INF = 1 << 60  # Définit une grande valeur constante, utilisée généralement pour représenter l'infini. Ici, c'est 2^60.
sys.setrecursionlimit(10 ** 6)  # Définit la limite de récursion de Python à un million pour éviter les erreurs de récursion dans des cas profonds.

# Début du corps principal du programme (section où résoudre le problème principal).
# Récupère deux entiers n et k à partir de l'entrée standard.
n, k = map(int, input().split())  # split() sépare la ligne d'entrée sur les espaces, map applique int() à chaque partie.

# Récupère trois entiers r, s, p. Ces variables représentent les points attribués pour jouer 'rock', 'scissors', 'paper'.
r, s, p = map(int, input().split())  # Lecture et affectation simultanées des trois valeurs depuis l'entrée.

# Récupère une chaîne t depuis l'entrée standard, représentant la séquence des actions adverses ('r','s','p').
t = input()  # Le contenu de t sera itéré plus loin pour déterminer les actions à choisir.

a = ""  # Initialise la chaîne a, qui contiendra la séquence de nos actions optimalement choisies.
# Pour chaque caractère (chaque coup de l'adversaire) dans la chaîne t (boucle sur l'adversaire).
for i in t:
    if i == "r":        # Si l'adversaire a joué 'rock' ("r"),
        a += "p"        # alors on joue 'paper' ("p"), car paper bat rock.
    elif i == "s":      # Sinon si l'adversaire a joué 'scissors' ("s"),
        a += "r"        # alors on joue 'rock' ("r"), car rock bat scissors.
    else:               # Sinon, l'adversaire a joué 'paper' ("p")
        a += "s"        # alors on joue 'scissors' ("s"), car scissors bat paper.

ans = 0  # Initialise la variable 'ans', qui contiendra le score total obtenu.

# Pour chaque caractère (coup choisi) dans 'a' (la liste de nos coups optimaux sans contrainte sur les doublons espacés de k).
for i in a:
    if i == "r":        # Si on a joué 'rock' ("r")
        ans += r        # On ajoute le score attribué à 'rock' à la réponse totale.
    elif i == "s":      # Sinon si on a joué 'scissors' ("s")
        ans += s        # On ajoute le score de 'scissors'.
    else:               # Sinon, on a joué 'paper' ("p")
        ans += p        # On ajoute le score de 'paper'.
# Note : À ce stade, tous les coups sont traités comme indépendants. On va compenser ensuite si la contrainte de non-répétition k s'applique.

# Pour gérer la contrainte : on ne peut pas gagner en utilisant le même coup que k coups avant.
# On parcourt l'indexi des coups, en commençant à k (ici, on commence après les k premiers coups car on ne peut pas vérifier pour les premiers).
for i in range(k, n):       # Pour chaque index i allant de k jusqu'à n-1 (noter que range s'arrête avant n).
    if a[i] == a[i - k]:    # Si le coup à l'index i est le même que celui à l'index i-k (le coup précédent dans la même sous-séquence de modulo k)
        # On a donc utilisé le même coup qu'il y a k coups, ce qui n'est pas permis pour scorer.
        if a[i] == "r":     # Si le coup interdit est 'rock', 
            ans -= r        # On soustrait le score r car ce point ne doit pas être compté.
        elif a[i] == "s":   # Si c'est 'scissors',
            ans -= s        # On soustrait le score s.
        else:               # Si c'est 'paper',
            ans -= p        # On soustrait le score p.
        # On modifie le coup à l'index i dans la chaîne a pour ne pas compter ce coup plusieurs fois à l'avenir.
        # Comme les chaînes sont immuables en Python, on crée une nouvelle chaîne identique, sauf à l'index i où on met un caractère arbitraire ("a" ici).
        a = a[:i] + "a" + a[i + 1:]  # Ceci empêche de décompter deux fois sur des séquences à distance k multiples.
        
print(ans)  # Affiche enfin le score total obtenu après avoir appliqué la contrainte de non-répétition à distance k.