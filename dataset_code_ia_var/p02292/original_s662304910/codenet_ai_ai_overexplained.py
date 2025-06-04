#!/usr/bin/env python

"""
Ce programme lit une ligne contenant les coordonnées de deux points dans le plan (p0 et p1), suivie d'un entier q,
puis q lignes avec chacune les coordonnées d'un point test (p2). Pour chaque p2, il détermine la position relative
de p2 par rapport au segment orienté p0->p1 : à droite (CLOCKWISE), à gauche (COUNTER_CLOCKWISE), sur la droite
avant p0 (ONLINE_BACK), après p1 (ONLINE_FRONT), ou sur le segment lui-même (ON_SEGMENT).
"""

import sys  # Importation du module sys pour lire l'entrée standard (stdin).

# EPS est une petite valeur utilisée pour comparer des nombres réels à cause des imprécisions de calcul flottant.
EPS = 1e-9

def cross(a, b):
    # Produit vectoriel de deux nombres complexes (utilisé pour déterminer l'orientation).
    # Le produit vectoriel donne une valeur positive, négative, ou zéro en fonction de la position relative de b par rapport à a.
    # Si on considère les complexes comme des vecteurs (x, y), cross(a, b) = a.x * b.y - a.y * b.x.
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    # Produit scalaire de deux nombres complexes considérés comme des vecteurs du plan.
    # Cela donne l'avancement de b le long de a (cosinus de l'angle * norme des deux vecteurs).
    return a.real * b.real + a.imag * b.imag

def calc_distance(p_info):
    # Cette fonction prend une liste d'itérables de chaînes contenant les coordonnées des points à tester.
    for point in p_info:
        # Pour chaque point à tester :
        # On extrait la partie réelle (abscisse) et imaginaire (ordonnée), on les convertit en entiers.
        p2_real, p2_imag = map(int, point)
        # On crée un nombre complexe à partir des coordonnées : p2 = x + y * i
        p2 = p2_real + p2_imag * 1j
        # a est le vecteur du segment p0->p1 (c'est-à-dire p1 moins p0). b est le vecteur p0->p2.
        a, b = p1 - p0, p2 - p0
        # On commence par tester le sens de rotation via le produit vectoriel :
        if cross(a, b) > EPS:
            # Si le produit vectoriel est positif (au-delà d’une petite marge d’erreur), p2 est "à gauche" du segment orienté p0->p1.
            print('COUNTER_CLOCKWISE')
        elif cross(a, b) < -1 * EPS:
            # Si le produit vectoriel est négatif (au-delà de la marge), p2 est "à droite" du segment orienté p0->p1.
            print('CLOCKWISE')
        elif dot(a, b) < -1 * EPS:
            # Si le vecteur b forme un angle obtus avec a (produit scalaire négatif), p2 est derrière p0 (donc en arrière du segment).
            print('ONLINE_BACK')
        elif abs(a) < abs(b):
            # Si la longueur du segment (a) est plus courte que celle de p0->p2 (b), p2 est au-delà de p1 ("devant" le segment).
            print('ONLINE_FRONT')
        else:
            # Sinon, p2 est aligné sur la droite support du segment, et se situe sur le segment p0->p1 inclusivement.
            print('ON_SEGMENT')
    # Fin de la fonction, retourne None par défaut.
    return None

if __name__ == '__main__':
    # Point d'entrée principal quand ce script est exécuté directement.
    # On lit toutes les lignes de l'entrée standard (par exemple, fichiers ou saisie clavier).
    _input = sys.stdin.readlines()  # _input est une liste de chaînes, chaque chaîne représente une ligne de l'entrée.

    # La première ligne contient quatre entiers : x0, y0, x1, y1, représentant p0 (début du segment), p1 (fin du segment).
    base_line = tuple(map(int, _input[0].split()))  # On découpe la ligne en sous-chaînes puis on les convertit en int.

    # On construit deux complexes (p0 et p1) à partir de la base_line. zip(base_line[::2], base_line[1::2]) regroupe les x et y.
    p0, p1 = (x + y * 1j for x, y in zip(base_line[::2], base_line[1::2]))

    # La deuxième ligne de l'entrée contient le nombre de points à tester (q_num).
    q_num = int(_input[1])  # Conversion directe en entier.

    # Les lignes suivantes contiennent les q_num points à tester ; chaque ligne est divisée en deux entiers pour x et y.
    # map(lambda x: x.split(), _input[2:]) applique split() à chaque ligne pour produire une liste ["x", "y"].
    q_list = map(lambda x: x.split(), _input[2:])

    # On appelle la fonction principale avec la liste des points à tester.
    calc_distance(q_list)