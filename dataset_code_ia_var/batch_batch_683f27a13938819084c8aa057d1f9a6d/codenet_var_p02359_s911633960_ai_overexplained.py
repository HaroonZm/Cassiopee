# Importation de la fonction setrecursionlimit depuis le module sys.
# Cette fonction permet de définir la limite maximale de profondeur de récursion.
from sys import stdin, setrecursionlimit

# Importation de la classe Counter (outil de comptage d'éléments) et deque (file à double extrémité) depuis collections.
# Ici, seul Counter et deque sont importés, mais ils ne sont pas utilisés dans ce script précis.
from collections import Counter, deque

# Définir une nouvelle limite maximale pour la profondeur de récursion à un million (10^6).
# Cela est utile lorsqu'il existe des appels récursifs profonds, pour éviter l'erreur RecursionError.
setrecursionlimit(10**6)

# Redéfinition de la fonction input pour qu'elle lise depuis l'entrée standard (stdin) plus rapidement.
# stdin.readline lit une ligne entière de l'entrée standard sous forme de chaîne de caractères (incluant le '\n' de fin).
input = stdin.readline

# Lecture de la première ligne d'entrée, qui contient deux entiers séparés par un espace.
# La fonction input() récupère la ligne, split() la découpe en une liste de chaînes représentant les nombres, 
# et map(int, ...) convertit chaque chaîne en un entier.
# La structure "n, t = ..." permet d'affecter respectivement le premier nombre à n et le second à t.
n, t = map(int, input().split())

# Création d'une liste 'ac' (abréviation probable d'accumulateur).
# Cette liste contient (t+1) éléments, initialisés à 0.
# Elle servira à stocker, pour chaque temps/durée (index), le nombre d'augmentations ou diminutions pour chaque intervalle.
# L'index 0 n'est pas réellement utilisé pour les intervalles tels qu'on les lit (qui commencent en 1).
ac = [0] * (t + 1)

# Boucle d'itération qui se répète n fois, où n est le nombre d'intervalles à traiter.
for _ in range(n):
    # À chaque itération, on lit une ligne contenant deux entiers : l (début de l'intervalle) et r (fin de l'intervalle).
    l, r = map(int, input().split())
    # On incrémente la valeur à la position l dans la liste ac de 1. 
    # Cela signale qu'à partir de l, le nombre d'éléments actifs augmente de 1.
    ac[l] += 1
    # On décrémente la valeur à la position r de 1.
    # Cela signale qu'à partir de r (exclu ou inclus selon convention, mais ici ac[r]), le nombre d'éléments actifs diminue de 1.
    ac[r] -= 1

# Boucle qui traverse tous les indices de 1 à t (inclus) dans la liste ac.
for i in range(1, t + 1):
    # Pour chaque position i, on ajoute la valeur de l'élément précédent (ac[i-1]) à ac[i].
    # Cela permet de transformer la liste ac en une accumulation de la variation précédente,
    # ce qui donne le nombre "d'intervalles actifs" à chaque instant/indice i.
    ac[i] += ac[i - 1]

# Calcul du maximum de la liste ac.
# Cela correspond au moment où le nombre maximal d'intervalles couvrent le même instant/indice.
print(max(ac))
# Affichage du résultat, qui est le recouvrement maximal d'intervalles en tout point du temps t.