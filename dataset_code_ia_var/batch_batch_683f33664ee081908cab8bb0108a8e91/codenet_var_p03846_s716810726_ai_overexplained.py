# Importation du module numpy sous l'alias np. Ce module fournit des fonctions performantes pour manipuler des tableaux multidimensionnels et réaliser des calculs mathématiques avancés.
import numpy as np
# Importation du module math qui offre de nombreuses fonctions et constantes mathématiques, telles que sqrt, pi, etc.
import math
# Importation du module sys qui permet d'interagir avec l'interpréteur Python, y compris d'accéder à l'entrée/sortie standard.
import sys

# Définition d'une fonction appelée sinput.
# Cette fonction n'accepte aucun argument.
# Elle lit une ligne de texte à partir de l'entrée standard (clavier ou redirection).
# sys.stdin représente l'entrée standard en flux, readline() lit jusqu'à un retour à la ligne.
# Elle retourne la ligne lue telle quelle (possiblement avec un retour à la ligne à la fin).
def sinput():
    return sys.stdin.readline()

# Définition d'une fonction appelée iinput.
# Cette fonction n'accepte aucun argument.
# Elle appelle la fonction sinput() pour lire une ligne de texte depuis l'entrée standard.
# Elle convertit ensuite la chaîne lue en un entier à l'aide de la fonction int().
# Elle retourne cet entier.
def iinput():
    return int(sinput())

# Définition d'une fonction appelée imap.
# Elle n'accepte aucun argument.
# Elle lit une ligne depuis l'entrée standard grâce à sinput().
# Elle utilise split() pour découper cette ligne en une liste de sous-chaînes, séparées par les espaces.
# Elle applique la fonction int (convertir en entier) à chaque élément de cette liste grâce à map().
# Elle retourne un objet map contenant les entiers.
def imap():
    return map(int, sinput().split())

# Définition d'une fonction appelée fmap.
# Elle ne prend pas d'arguments.
# Elle lit une ligne depuis l'entrée standard via sinput().
# Elle découpe la ligne en une liste de chaînes avec split().
# Elle applique la conversion en nombre flottant float() à chaque chaîne via map().
# Elle retourne un objet map contenant ces nombres flottants.
def fmap():
    return map(float, sinput().split())

# Définition d'une fonction appelée iarr.
# Cette fonction n'a pas d'arguments.
# Elle appelle imap() pour obtenir une séquence de valeurs entières extraites d'une ligne de l'entrée standard.
# Elle convertit l'objet map retourné par imap() en une liste à l'aide de list().
# Elle retourne la liste d'entiers.
def iarr():
    return list(imap())

# Définition d'une fonction nommée farr.
# Sans argument, elle lit et découpe la ligne obtenue comme pour fmap(), mais convertit le résultat map en liste.
# Elle retourne une liste de nombres flottants obtenue depuis l'entrée standard.
def farr():
    return list(fmap())

# Définition d'une fonction nommée sarr.
# Aucun argument attendu.
# Elle lit une ligne depuis l'entrée standard via sinput().
# Elle utilise split() pour découper cette ligne en une liste de mots (chaînes de caractères séparées par des espaces).
# Elle retourne la liste.
def sarr():
    return sinput().split()

# Lecture d'un entier depuis l'entrée standard.
# input() lit une ligne depuis l'utilisateur, int() convertit cette chaîne en entier décimal.
# Le résultat est stocké dans la variable n.
n = int(input())

# Appel de la fonction iarr() définie plus haut.
# Cette fonction lit une ligne, sépare chaque élément, convertit chacun en entier et retourne la liste complète.
# La liste obtenue est stockée dans la variable appelée A.
A = iarr()

# Création d'un ensemble (set) nommé s contenant tous les éléments distincts de la liste A.
# set() est un type de collection Python qui ne peut contenir que des éléments uniques (pas de doublons).
s = set(A)

# Calcul de la somme de tous les éléments dans A en utilisant la fonction sum().
# Calcul de la somme de tous les éléments distincts (dans l'ensemble s) aussi avec sum().
# test : On vérifie si la somme totale des éléments de A est égale au double de la somme des éléments distincts.
if sum(A) == 2 * sum(s):
    # Si la condition précédente est vraie :
    # On calcule 2 à la puissance len(A) divisé par 2 (division entière).
    # pow(x, y, m) élève x à la puissance y puis calcule le reste de la division euclidienne par m (modulo).
    # len(A) retourne le nombre total d'éléments dans A.
    # int(1e9+7) convertit la constante flottante 1e9+7 en un entier (résultant 1000000007), utilisé comme diviseur pour prendre le résultat modulo ce nombre.
    resultat = pow(2, len(A) // 2, int(1e9 + 7))
    # Affichage du résultat sur la sortie standard.
    print(resultat)
else:
    # Si la condition n'est pas vérifiée, on affiche 0.
    print(0)