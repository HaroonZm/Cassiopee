#!/usr/bin/env python3

# Importation de la classe defaultdict du module collections.
# defaultdict est une sous-classe de dict qui fournit une valeur par défaut pour une clé inexistante.
from collections import defaultdict

# Lecture de la première entrée utilisateur, qui doit être un entier, et conversion à un int.
N = int(input())  # Stocke la longueur des chaînes d'entrée, mais inutile dans le code

# Lecture de la deuxième entrée utilisateur, qui est supposée être une chaîne de caractères (string).
s1 = input()  # La première chaîne à comparer

# Lecture de la troisième entrée utilisateur, également une chaîne de caractères.
s2 = input()  # La deuxième chaîne à comparer

# Définition d'une fonction pour compter les occurrences de chaque caractère dans une chaîne de caractères.
def make_appears(s):
    # Conversion de la chaîne 's' en une liste d'entiers représentant le code ASCII de chaque caractère.
    # La fonction ord(c) retourne le code Unicode (habituellement ASCII) du caractère c.
    chars = list(map(ord, s))
    # Création d'un dictionnaire avec des valeurs entières par défaut pour compter les occurrences de chaque caractère.
    hist = defaultdict(int)
    # Parcours de la liste des entiers représentant les caractères.
    for ch in chars:
        # Incrémente le compteur pour chaque code de caractère observé
        hist[ch] += 1
    # Extrait uniquement les valeurs du dictionnaire, c'est-à-dire le nombre d'occurrences pour chaque caractère distinct.
    appears = list(hist.values())
    # Trie la liste des occurrences en ordre croissant.
    appears.sort()
    # Inverse la liste pour obtenir un ordre décroissant.
    appears.reverse()
    # Retourne la liste ordonnée des fréquences d'apparition des caractères.
    return appears

# Appel de la fonction sur la première chaîne, stocke la liste des occurrences pour s1.
appears1 = make_appears(s1)
# Appel de la fonction sur la deuxième chaîne, stocke la liste pour s2.
appears2 = make_appears(s2)

# Initialise une variable pour accumuler la somme totale de la différence des fréquences.
ans = 0

# zip(appears1, appears2) crée des paires d'éléments correspondants à la même position dans les deux listes.
# i et j représentent les nombres d'occurrences pour chaque caractère (dans l'ordre décroissant des fréquences).
for i, j in zip(appears1, appears2):
    # Calcule la valeur absolue de la différence entre i et j (différence des comptages pour la même position)
    ans += abs(i - j)  # Ajoute le résultat à la variable d'accumulation

# Calcule la longueur minimale des deux listes de fréquences.
shorter = min(len(appears1), len(appears2))

# Si les listes de fréquences n'ont pas la même longueur, il peut rester des éléments non appariés
# Appears1[shorter:] donne la sous-liste restante de appears1 (si elle est plus longue)
# Sommation de toutes ces fréquences restantes pour les éléments non correspondants
ans += sum(appears1[shorter:]) + sum(appears2[shorter:])

# La réponse finale doit être divisée par 2 (car chaque différence a été comptée deux fois lors de la transformation de l'un vers l'autre)
# L'opérateur // effectue une division entière, retournant la partie entière du quotient
print(ans // 2)  # Affiche la réponse finale à l'utilisateur