import math  # Module mathématique de base : fournit des fonctions mathématiques standard (ex : sqrt, sin, cos)
import string  # Donne accès à des constantes et des fonctions utiles pour manipuler des chaînes de caractères (ex : string.ascii_letters)
import itertools  # Fournit des outils pour la manipulation efficace des itérateurs (permutations, produits cartésiens, etc.)
import fractions  # Contient des classes pour gérer les fractions (utile pour la précision arithmétique exacte)
import heapq  # Fournit une implémentation efficace de files de priorité (heaps, min-heaps)
import collections  # Offre des structures de données spécialisées, comme deque, Counter, defaultdict...
import re  # Module d'expressions régulières pour la manipulation avancée de chaînes de caractères
import array  # Implémentation efficace et compacte de tableaux numériques simples
import bisect  # Fournit des fonctions pour l'insertion et la recherche binaires dans des listes triées
import sys  # Donne accès à des objets et fonctions liés à l'interpréteur Python (ex : sys.stdin, sys.stdout)
import random  # Pour générer des nombres, choix et échantillonnages au hasard
import time  # Pour chronométrer, mesurer et manipuler le temps
import copy  # Fournit des fonctions pour copier des objets (profondément ou non)
import functools  # Utilitaire de programmation fonctionnelle (decorators, partial, reduce...)

# Permet de modifier la limite maximale de profondeur de récursion autorisée par Python (par défaut, 1000)
# Ici, on la met à 10^7 pour éviter un "RecursionError" dans les cas de profondeurs extrêmes.
sys.setrecursionlimit(10**7)

# On définit une constante pour représenter une "infinie" grande valeur entière.
inf = 10**20

# On définit une petite constante (epsilon) pour la comparaison de nombres flottants, afin d'éviter des erreurs d'arrondi.
eps = 1.0 / 10**10

# Le modulo utilisé dans beaucoup de problèmes d'arithmétique modulaire, typiquement pour éviter les débordements d'entiers.
mod = 10**9+7

# "dd" stocke la liste des 4 déplacements orthogonaux possibles sur une carte (haut, droite, bas, gauche) pour des parcours de grille.
dd = [(-1,0),(0,1),(1,0),(0,-1)]

# "ddn" donne les 8 mouvements voisins dans une grille (y compris les diagonales), pour les parcours ou la recherche autour d'un point.
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonction LI() : lit la ligne en entrée standard, la découpe sur les espaces (split()},
# convertit chaque morceau en int (entier Python), et renvoie la liste des entiers.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Comme LI(), mais retourne les entiers indexés à partir de 0 (donc on retire 1 à chaque valeur).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Pareil, mais pour des nombres flottants (float)
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne de texte depuis l'entrée standard, la découpe par espace et renvoie une liste de chaînes.
def LS():
    return sys.stdin.readline().split()

# Lis une unique ligne, convertit en entier Python, renvoie cet entier.
def I():
    return int(sys.stdin.readline())

# Pareil, mais pour lire un float
def F():
    return float(sys.stdin.readline())

# Lis une chaîne de caractères (avec input(), qui lit jusqu'à '\n'), renvoie la chaîne brute.
def S():
    return input()

# Fonction affiche le texte (s) à l'écran et s'assure qu'il s'affiche immédiatement (flush=True vide le buffer de sortie).
def pf(s):
    return print(s, flush=True)

# Début de la fonction principale
def main():
    rr = []  # Liste qui contiendra les résultats pour chaque jeu de données rencontré, qu'on affichera à la fin

    while True:  # Boucle infinie, sortira explicitement par un break quand nécessaire
        a = S()  # Lit une première chaîne de caractères (typiquement une série de chiffres ou de '?')
        if a == '0':  # Si la chaîne est '0', alors on considère que c'est un signal d'arrêt
            break
        b = S()  # Lire la deuxième chaîne au même format que 'a'
        c = S()  # Lire la troisième chaîne au même format que 'a' et 'b'

        # On calcule la longueur maximale parmi les trois chaînes, afin de les égaliser par ajout éventuel de zéros
        ml = max([len(a),len(b),len(c)])

        # Si la longueur de 'a' est inférieure à la taille maximale, on lui préfixe des '0'
        if len(a) < ml:
            a = '0' * (ml-len(a)) + a
        # Pareil pour 'b'
        if len(b) < ml:
            b = '0' * (ml-len(b)) + b
        # Pareil pour 'c'
        if len(c) < ml:
            c = '0' * (ml-len(c)) + c

        # On initialise un tableau à deux dimensions pour stocker les "chemins" de calculs intermédiaires :
        # Chaque élément r[i] = [sans retenue, avec retenue] et on a ml+1 éléments, soit un pour chaque position + la position de départ.
        r = [[0,0] for _ in range(ml+1)]
        # On initialise le cas de départ : à la position 0 (avant d’avoir ajouté le moindre chiffre) on n’a qu’une seule possibilité, sans retenue.
        r[0][0] = 1

        # On va parcourir chaque chiffre (de droite à gauche car dans l’addition on commence par les unités)
        for i in range(ml):
            # Les index se lisent depuis la fin, donc [ml-i-1] est la position correspondante (à l’envers)
            ai = a[ml-i-1]
            bi = b[ml-i-1]
            ci = c[ml-i-1]

            # On prépare deux tableaux temporaires pour les cas de "pas de retenue" (r0) et "avec retenue" (r1)
            r0 = [0,0]  # [r0[0] : pas de retenue, r0[1] : avec retenue]
            r1 = [0,0]  # Idem pour r1

            # Par défaut si = 0 (on peut avoir des zéros en début), mais pour la position la plus élevée, on ne peut pas mettre de zéro en tête donc on impose si=1
            si = 0
            if i == ml - 1:
                si = 1  # Pour le chiffre le plus significatif, on démarre à 1 pour éviter des nombres à 0 non significatifs

            # On construit les listes de choix possibles pour chaque caractère
            # Si c'est un '?', tous les chiffres possibles sont permis dans le bon intervalle sinon seule la valeur imposée
            al = range(si,10)
            if ai != '?':
                al = [int(ai)]
            bl = range(si,10)
            if bi != '?':
                bl = [int(bi)]
            cl = range(si,10)
            if ci != '?':
                cl = [int(ci)]

            # On parcourt toutes les possibilités de chiffres pour 'a', 'b', 'c' à cette position
            for ac,bc,cc in itertools.product(al,bl,cl):
                abc = ac+bc  # On additionne les chiffres sélectionnés pour a et b à cette position

                # On vérifie si (ac+bc) modulo 10 est égal à cc, cas standard sans retenue en sortie
                if abc % 10 == cc:
                    # Si le total dépasse 9, il y aura une retenue vers le chiffre supérieur pour la prochaine itération
                    if abc > 9:
                        r0[1] += 1  # Incrémente le cas [avec retenue]
                    else:
                        r0[0] += 1  # Incrémente le cas [pas de retenue]
                # Sinon, si en ajoutant 1 (pour une retenue précédente) modulo 10 on tombe sur cc
                elif (abc+1) % 10 == cc:
                    # Si le total plus la retenue dépasse 9 aussi, là aussi, il y aura encore une retenue propagée
                    if abc > 8:
                        r1[1] += 1
                    else:
                        r1[0] += 1

            # Calcul des transitions dynamiques :
            # La nouvelle valeur sans retenue (r[i+1][0]) s'obtient en cumulant toutes les façons d'y arriver soit d'un état sans retenue (r0[0]) soit d'un état avec retenue (r1[0])
            r[i+1][0] += r0[0] * r[i][0]
            r[i+1][0] += r1[0] * r[i][1]
            # Pareil pour l'état "avec retenue" : cumul des transitions qui aboutissent à garder une retenue sur cette position
            r[i+1][1] += r0[1] * r[i][0]
            r[i+1][1] += r1[1] * r[i][1]

        # A la fin du parcours, r[ml][0] contient le nombre total de façons de compléter les chaînes pour obtenir la bonne addition sans retenue finale
        # On prend le résultat modulo 'mod' pour éviter des entiers trop grands
        rr.append(r[ml][0] % mod)

    # On assemble tous les résultats, chacun sur une ligne, au format chaîne de caractères.
    return '\n'.join(map(str,rr))

# Appel de la fonction principale et affichage du résultat final à l'écran
print(main())