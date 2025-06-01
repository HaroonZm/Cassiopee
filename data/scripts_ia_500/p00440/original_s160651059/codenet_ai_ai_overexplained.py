from bisect import bisect_left, bisect_right  # Importation des fonctions bisect_left et bisect_right qui permettent de faire des recherches binaires dans des listes triées
from collections import Counter, defaultdict, deque, OrderedDict  # Importation de différentes structures de données comme Counter (compteur d'éléments), defaultdict (dictionnaire avec valeur par défaut), deque (file doublement terminée), OrderedDict (dictionnaire ordonné)
from copy import deepcopy  # Importation de la fonction deepcopy qui permet de copier un objet récursivement pour avoir une copie indépendante
from fractions import gcd  # Importation de la fonction gcd qui calcule le plus grand commun diviseur entre deux entiers (à noter que gcd est déplacé dans math à partir de Python 3.9)
from functools import lru_cache, reduce  # Importation de lru_cache (mémorisation de résultats de fonctions) et reduce (application répétée d'une fonction binaire sur une séquence)
from math import ceil, floor  # Importation des fonctions ceil (arrondi supérieur) et floor (arrondi inférieur)
from sys import setrecursionlimit  # Importation de la fonction setrecursionlimit qui modifie la limite maximale de la profondeur de récursion autorisée

import heapq  # Importation du module heapq permettant de manipuler des tas/binary heaps
import itertools  # Importation du module itertools fournissant des fonctions pour créer des itérateurs efficaces
import operator  # Importation du module operator qui fournit des fonctions d'opérations courantes (add, mul, etc.)

# Déclaration d'une constante 'inf' qui représente l'infini en virgule flottante
inf = float('inf')

# Initialisation de trois variables globales sous forme de listes vides
N, K = [], []  # Listes pour stocker des entiers n et k lus depuis l'entrée
C = []         # Liste pour stocker des listes C, chaque C contenant des entiers

def set_inputs():
    '''
    Définition d'une fonction qui remplit les listes globales N, K et C avec les données en entrée.
    On utilise l'instruction global pour modifier les variables globales.
    La fonction lit successivement des lignes d'entrée tant que la paire (n, k) n'est pas (0, 0).
    Ensuite, pour chaque (n, k), elle lit k entiers correspondants à une liste c et les ajoute à C.
    '''
    global N, K, C  # Permet d'utiliser/modifier les variables externes globales N, K, C
    while True:
        n, k = get_li()  # Lecture d'une ligne d'entrée : liste d'entiers, on récupère n et k
        if n == k == 0:  # Condition d'arrêt de la lecture : si les deux valeurs sont 0, on arrête la boucle
            break
        N.append(n)  # Ajout de n à la liste globale N
        K.append(k)  # Ajout de k à la liste globale K
        c = get_data(k, [int])  # Lecture de k éléments d'entrée convertis en entiers, sous forme de liste c
        C.append(c)  # Ajout de la liste c à C
    return  # Fin de la fonction, retourne None implicitement

def sgn(n):
    '''
    Fonction qui calcule le signe d'un nombre entier n.
    Retourne 0 si n = 0, 1 si n est positif, -1 si n est négatif.
    Cela permet de connaître la direction ou la nature du nombre.
    '''
    if n == 0:    # Test si n est nul
        return 0  # Retourne 0
    if n > 0:     # Test si n est strictement positif
        return 1  # Retourne 1
    return -1     # Sinon, n est négatif, on retourne -1

def main():
    '''
    Fonction principale du programme qui coordonne la lecture des données, le traitement principal,
    puis affiche les résultats.
    '''
    setrecursionlimit(100000)  # Augmente la limite maximale de récursion pour éviter un dépassement de pile éventuel
    set_inputs()  # Appel de la fonction qui remplit N, K et C à partir des entrées
    
    # ---------- TRAITEMENT PRINCIPAL ----------
    # On va traiter chaque triplet (n,k,c) extrait des listes globales simultanément
    for n, k, c in zip(N, K, C):
        c.sort()  # Trie la liste c par ordre croissant : indispensable pour la logique qui suit
        
        ans = 0  # Initialisation d'une variable 'ans' pour stocker le résultat maximal trouvé pour ce cas
        
        if c[0] == 0:  # Cas où le premier élément de c est égal à 0
            tmp = 1  # Variable temporaire tmp initialisée à 1, va servir à compter ou suivre une séquence
            
            # On boucle simultanément sur les couples consécutifs dans la liste c sauf le dernier élément
            for v1, v2 in zip(c[1:], c[2:]):
                # Si les deux valeurs consécutives diffèrent de 1 (sont adjacentes)
                if v2 - v1 == 1:
                    tmp += 1 * sgn(tmp)  # On incrémente tmp de 1 multiplié par le signe de tmp (assure que tmp garde son signe)
                    
                    # On met à jour ans si la valeur absolue de tmp dépasse celle actuelle d'ans
                    if abs(tmp) > abs(ans):
                        ans = tmp
                        
                elif v2 - v1 == 2:  # Si la différence est exactement égale à 2
                    if tmp > 0:
                        tmp = -tmp - 2  # On inverse le signe de tmp et on décrémente de 2 si tmp est positif
                    else:
                        tmp = -3       # Sinon, on met tmp à -3
                    
                else:
                    tmp = 1  # Réinitialisation de tmp à 1 si la différence n'est ni 1 ni 2
                    
            if ans > 0:
                ans += 1  # Si ans est positif, on l'incrémente de 1 (post-traitement)
            ans = abs(ans)  # Transformation finale de ans en sa valeur absolue pour la sortie
            
        else:  # Cas où le premier élément de c n'est pas égal à 0
            tmp = 1  # Initialisation de tmp à 1 pour le comptage des éléments consécutifs
            
            # Boucle sur les couples consécutifs dans c (de v1 à v2)
            for v1, v2 in zip(c, c[1:]):
                if v2 - v1 == 1:  # Si la différence est égale à 1 (éléments consécutifs)
                    tmp += 1      # Incrémentation du compteur tmp
                    ans = max(ans, tmp)  # Mise à jour de ans si tmp est supérieur à ans
                else:
                    tmp = 1       # Sinon réinitialisation du compteur tmp à 1
                    
        print(ans)  # Affichage du résultat calculé ans pour ce cas particulier
        
    return  # Fin de la fonction main, retour implicite None

def get_int():
    '''
    Fonction utilitaire pour lire une seule entrée entière depuis l'entrée standard.
    '''
    return int(input())  # Lecture d'une ligne, conversion en entier puis renvoi

def get_float():
    '''
    Fonction utilitaire pour lire une seule entrée flottante depuis l'entrée standard.
    '''
    return float(input())  # Lecture d'une ligne, conversion en float puis renvoi

def get_str():
    '''
    Fonction utilitaire pour lire une chaîne de caractères, en ôtant les espaces en début et fin.
    '''
    return input().strip()  # Lecture d'une ligne, suppression des espaces inutiles puis renvoi

def get_li():
    '''
    Fonction utilitaire qui lit une ligne contenant plusieurs entiers séparés par des espaces.
    Retourne la liste des entiers correspondants.
    '''
    return [int(i) for i in input().split()]  # Split la ligne en sous-chaînes, conversion en int, création d'une liste

def get_lf():
    '''
    Fonction utilitaire qui lit une ligne contenant plusieurs flottants séparés par des espaces.
    Retourne la liste des flottants correspondants.
    '''
    return [float(f) for f in input().split()]  # Split la ligne en sous-chaînes, conversion en float, création d'une liste

def get_lc():
    '''
    Fonction utilitaire qui lit une ligne de texte et retourne la liste de ses caractères.
    '''
    return list(input().strip())  # Lecture de la ligne, suppression espaces non significatifs, conversion en liste de caractères

def get_data(n, types, sep=None):
    '''
    Fonction utilitaire qui lit n lignes d'entrée.
    Chaque ligne est convertie selon une liste de types passés en paramètre.
    Si un seul type est fourni, retourne simplement une liste contenant n éléments convertis.
    Si plusieurs types sont fournis, retourne un tuple d'itérables avec chaque élément converti selon son type.
    L'argument sep permet de définir le séparateur pour split.
    '''
    if len(types) == 1:
        # Cas particulier où une seule colonne avec un type unique est lu : on lit n fois la valeur convertie
        return [types[0](input()) for _ in range(n)]
    # Sinon, on lit n lignes, on split chaque ligne avec sep, et on convertit chaque élément avec son type respectif
    return list(zip(*(
        [t(x) for t, x in zip(types, input().split(sep=sep))]
        for _ in range(n)
    )))

if __name__ == '__main__':
    '''
    Point d'entrée du script.
    Lorsque le script est exécuté directement, on appelle la fonction main.
    '''
    main()