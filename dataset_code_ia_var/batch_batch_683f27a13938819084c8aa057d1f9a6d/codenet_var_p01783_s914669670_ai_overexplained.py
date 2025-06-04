# Importation de nombreux modules standards de Python, même si ils ne sont pas tous utilisés ici :
# math : fournit des fonctions mathématiques standard
# string : contient des constantes et fonctions pour manipuler des chaînes de caractères
# itertools : outils pour créer et utiliser des itérateurs performants
# fractions : permet de travailler avec des fractions rationnelles
# heapq : pour utiliser des file de priorité (tas)
# collections : contient des structures de données spécialisées comme deque ou Counter
# re : permet d'utiliser des expressions régulières
# array : pour des tableaux typés de valeurs numériques
# bisect : effectue des recherches et insertions dans des listes triées
# sys : fournit un accès à des variables et fonctions interagissant avec l'interpréteur Python
# random : permet de générer des nombres aléatoires
# time : accède au temps système, chronomètre, etc.
# copy : pour copier des objets (copie superficielle/profonde)
# functools : outils pour la programmation fonctionnelle
import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Modification de la limite de récursion autorisée par défaut en Python.
# Utile pour permettre des appels récursifs très profonds sans provoquer "RecursionError"
sys.setrecursionlimit(10**7)

# Définition de quelques constantes utiles pour le reste du programme :

# Une très grande valeur, souvent utilisée pour initialiser un minimum ou maximum dans des comparaisons
inf = 10**20

# Une petite valeur epsilon, souvent utilisée pour comparer des flottants ou pour gérer la précision
eps = 1.0 / 10**13

# Un nombre premier très utilisé en programmation compétitive pour les calculs modulo
mod = 10**9 + 7

# Une liste contenant 4 directions cardinals :
# Chaque élément est un tuple (delta_ligne, delta_colonne), représentant un déplacement haut, droite, bas, gauche
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Une liste définissant les 8 directions autour d'un point (carré dans une grille)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Fonctions abrégées pour la lecture de l'entrée standard.
# Chacune lit une ligne depuis sys.stdin et la transforme d'une certaine manière :

# Lit une ligne, sépare les mots, convertit chacun en int et renvoie la liste
def LI():
    # sys.stdin.readline() lit une ligne de l'entrée standard (y compris le \n de fin)
    # .split() découpe cette ligne en éléments séparés par des espaces/blancs
    # [int(x) for x in ...] convertit chaque élément de la liste en entier
    return [int(x) for x in sys.stdin.readline().split()]

# Même chose que LI mais retire 1 à chaque entier (très utile pour convertir indices 1-based en 0-based)
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Lit une ligne, sépare les mots, convertit en float
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne, découpe en mots (chaînes de caractères) et renvoie la liste
def LS():
    return sys.stdin.readline().split()

# Lit une ligne et convertit en entier unique
def I():
    return int(sys.stdin.readline())

# Lit une ligne et convertit en float unique
def F():
    return float(sys.stdin.readline())

# Lit une ligne et renvoie la chaîne obtenue via input() (fonction input standard)
def S():
    # input() lit une ligne depuis stdin, sans le caractère de fin de ligne (contrairement à readline)
    return input()

# Fonction pour afficher un résultat et s'assurer qu'il s'affiche tout de suite (flush=True vide le tampon de sortie)
def pf(s):
    return print(s, flush=True)

# Fonction principale du script
def main():
    # Lit une chaîne "s" depuis l'entrée standard grâce à la fonction S() définie précédemment
    s = S()
    # Calcule la longueur de la chaîne lue
    l = len(s)
    # Initialise un dictionnaire (table de hachage) pour la mémorisation (cache des résultats de la fonction récursive)
    fm = {}
    # Met dans le cache la chaîne vide "" qui mappe vers -1 (sans doute utilisée comme valeur impossible par convention)
    fm[''] = -1

    # Définition d'une fonction récursive (fonction imbriquée locale dans main()) nommée f
    # Cette fonction prend une chaîne "s" en entrée et retourne (souvent) un entier, représentatif d'une valeur maximale calculée
    def f(s):
        # Vérifie si la chaîne s est déjà stockée dans le dictionnaire "fm" (cache pour éviter des calculs redondants)
        if s in fm:
            # Si oui, retourne immédiatement la valeur déjà calculée correspondante
            return fm[s]
        # Sinon, calcule la longueur de la chaîne courante
        l = len(s)
        # Initialise une variable r à -1, qui stockera la "valeur maximale" trouvée pour cette chaîne
        r = -1
        # Cas où la chaîne semble représenter une "expression" orientée arbre binaire (fonction arithmétique, etc.)
        # On vérifie que la longueur de s > 5, que le caractère à la position 1 fait partie de '(', '?' (donc un nœud/groupe)
        # Que le dernier caractère fait partie de ')' ou '?', c'est-à-dire qu'on a probablement une structure de la forme L(expr,expr)
        if l > 5 and s[1] in '(?' and s[-1] in ')?':
            # Si le premier caractère est 'R' (ou '?'), on suppose un "noeud droit" (type R)
            if s[0] in 'R?':
                # On va maintenant chercher un séparateur ',' ou '?' entre les deux sous-expressions du nœud
                # La boucle va de i=3 à l-2, i.e. saute les premiers et derniers caractères qui ne peuvent pas être ','
                for i in range(3, l-2):
                    # Le caractère qui sépare les sous-arbres doit être ',' ou '?'
                    if s[i] not in ',?':
                        continue  # Si le caractère n'est ni ',' ni '?', passe à l'itération suivante
                    # Appel récursif sur la sous-chaîne correspondante à l'enfant gauche : de position 2 à i (exclus)
                    tl = f(s[2:i])
                    # Appel récursif sur la sous-chaîne correspondante à l'enfant droit : de position i+1 à l-1 (exclus)
                    tr = f(s[i+1:-1])
                    # Si les deux sous-arbres ont donné une valeur >= 0 (valide), on met à jour r avec la valeur de droite si elle est meilleure
                    if tl >= 0 and tr >= 0 and r < tr:
                        r = tr
            # Même chose mais pour le cas où le premier caractère est 'L' (ou '?')
            if s[0] in 'L?':
                for i in range(3, l-2):
                    if s[i] not in ',?':
                        continue
                    # On inverse la préférence : ici r est mis à jour avec tl (valeur du sous-arbre gauche), logique de "max gauche"
                    tl = f(s[2:i])
                    tr = f(s[i+1:-1])
                    if tl >= 0 and tr >= 0 and r < tl:
                        r = tl
        # Cas où la chaîne ne contient pas la structure d'un nœud (ni parenthèses, ni ',')
        # Initialement, on va supposer que la chaîne pourrait représenter juste un nombre naturel (valide)
        ff = True  # Valeur booléenne qui dit si la chaîne est un nombre "valide"
        # Si la chaîne commence par '0' et qu'elle est plus longue que 1 caractère, c'est une représentation non valide (pour éviter les zéros initiaux)
        if s[0] == '0' and l > 1:
            ff = False
        # On vérifie que la chaîne ne contient aucun des caractères spéciaux, qui seraient invalides dans un chiffre pur
        for tc in 'RL,()':
            if tc in s:
                ff = False
                break  # Dès qu'on en trouve un, ce n'est plus un nombre tout court, inutile de vérifier la suite
        # Si la chaîne passe ces tests, on remplace tous les caractères '?' (joker) par '9' pour maximiser la valeur possible,
        # puis on convertit la chaîne ainsi obtenue en entier
        if ff:
            r = int(s.replace('?', '9'))
        # Stocke le résultat pour la chaîne courante dans le cache pour optimiser les appels futurs
        fm[s] = r
        # Retourne la valeur calculée/extraite/finale pour la chaîne donnée
        return r

    # Appel initial à la fonction récursive avec la chaîne entrée
    r = f(s)
    # Si la fonction a retourné une valeur négative, cela indique un cas "invalid", donc on retourne la chaîne "invalid"
    if r < 0:
        return 'invalid'

    # Sinon, on retourne la valeur trouvée (qui sera printée plus bas)
    return r

# Exécute la fonction "main" et affiche son résultat sur la sortie standard
print(main())