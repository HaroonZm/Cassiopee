# Importation de modules standards Python (sys pour la gestion des flux d'entrée/sortie, math pour les fonctions mathématiques, os pour l'accès aux variables d'environnement)
import sys  # Module intégré pour accéder à certains paramètres et fonctions système
import math  # Module mathématique (non utilisé ici mais souvent importé pour les fonctions math utiles)
import os  # Module pour interagir avec le système d'exploitation, par exemple accéder aux variables d'environnement

# Lecture de l'entrée selon l'environnement : si la variable d'environnement 'PYDEV' vaut "True",
# redirige sys.stdin vers un fichier texte pour l'entrée simulée (utilisé lors du développement/du débogage)
PYDEV = os.environ.get('PYDEV')  # Tente de récupérer la valeur associée à la variable d'environnement 'PYDEV' (renvoie None si absente)
if PYDEV == "True":  # Vérifie si la variable PYDEV est présente et vaut exactement la chaîne "True"
    sys.stdin = open("sample-input2.txt", "rt")  # Ouvre le fichier 'sample-input2.txt' en mode texte pour lecture et utilise son contenu comme entrée standard

# Listes contenant des séquences d'entiers, utilisées plus loin comme schémas de permutation pour la simulation des rotations de dé
# Chaque liste représente la permutation d'indices de faces du dé pour un type de rotation spécifique
a = [0,2,5,3]  # Séquence d'indices pour la première famille de rotation
b = [0,1,5,4]  # Séquence d'indices pour la deuxième famille de rotation
c = [1,2,4,3]  # Séquence d'indices pour la troisième famille de rotation

# Fonction permettant de déterminer si deux dés (listes d'entiers) sont identiques à une rotation près
def sortdice(dice1, dice2, p, q, r):
    # Cette fonction tente toutes les combinaisons possibles de rotation selon trois axes pour superposer les deux dés
    # Les listes p, q, et r servent à indiquer les schémas de rotation à appliquer à dice1 pour couvrir toutes les orientations
    for i in range(4):  # Répéter 4 fois (il y a 4 rotations autour du premier axe)
        # Effectuer une rotation sur dice1 selon l'axe décrit par la liste p
        dice1[p[0]], dice1[p[1]], dice1[p[2]], dice1[p[3]] = dice1[p[1]], dice1[p[2]], dice1[p[3]], dice1[p[0]]
        for j in range(4):  # Répéter 4 fois (pour le deuxième axe)
            # Effectuer une rotation sur dice1 selon l'axe décrit par la liste q
            dice1[q[0]], dice1[q[1]], dice1[q[2]], dice1[q[3]] = dice1[q[1]], dice1[q[2]], dice1[q[3]], dice1[q[0]]
            for k in range(4):  # Répéter 4 fois (pour le troisième axe)
                # Effectuer une rotation sur dice1 selon l'axe décrit par la liste r
                dice1[r[0]], dice1[r[1]], dice1[r[2]], dice1[r[3]] = dice1[r[1]], dice1[r[2]], dice1[r[3]], dice1[r[0]]
                if dice1 == dice2:
                    # Si après ces rotations, les deux dés ont la même configuration de faces,
                    # ils sont considérés comme identiques (même à une rotation près)
                    return True  # Indique que les deux dés sont identiques (il existe une orientation les superposant)
    return False  # Aucun arrangement n'a permis de superposer les deux dés, ils sont différents

# Fonction vérifiant que tous les dés d'une liste sont différents à toute rotation près
def all_different(N, dices):
    # N : nombre de dés dans la liste dices
    # dices : liste de N listes, chaque sous-liste représente les valeurs des faces d'un dé
    for i in range(N - 1):  # Parcours tous les indices sauf le dernier, pour comparer chaque paire unique
        dice1 = dices[i]  # On prend le dé à la position i
        for j in range(i + 1, N):  # Pour chaque dé suivant seulement (évite les comparaisons en double)
            dice2 = dices[j]
            # Comme sortdice modifie dice1, faire une copie pour ne pas altérer les données originales
            # .copy() crée une nouvelle liste indépendante avec le même contenu
            if sortdice(dice1.copy(), dice2, a, b, c):
                # Si deux dés sont identiques à toute rotation près, il existe au moins un doublon
                return False  # Indique que tous les dés ne sont pas différents
    # Si aucune paire de dés n'est identique à une rotation près, ils sont tous différents entre eux
    return True  # Indique que tous les dés sont différents

# Lecture du nombre de dés depuis l'entrée standard (normalement sys.stdin, ou un fichier si PYDEV="True")
N = int(input())  # Convertit la chaîne d'entrée en entier, nombre de dés

# Lecture des N dés et fabrication de la liste 'dices'
dices = []  # Initialisation de la liste qui contiendra chaque dé
for _ in range(N):  # Répéter N fois (une boucle par dé à lire)
    # input() lit une ligne, split() découpe la ligne en morceaux,
    # map(int, ...) convertit chaque morceau en entier,
    # list(...) met tout cela dans une nouvelle liste
    dices.append(list(map(int, input().split())))

# Si tous les dés sont différents (pas de doublon à une rotation près), afficher "Yes", sinon "No"
# Utilise une expression conditionnelle (ternaire) pour choisir la chaîne affichée selon le résultat
print("Yes" if all_different(N, dices) else "No")  # Affiche "Yes" si tous les dés sont différents, sinon "No"