#!/usr/bin/env python3
# CGL_7_A: Circles - Intersection

from enum import Enum
from math import sqrt

class Relation(Enum):
    """
    Enumération des types de relations possibles entre deux cercles.
    """
    INCLUDED = 0       # Un cercle est entièrement à l'intérieur de l'autre sans toucher (inclus strictement)
    INSCRIBED = 1      # Un cercle est à l'intérieur de l'autre et touche en un point (cercle inscrit)
    INTERSECT = 2      # Les cercles se coupent en deux points
    CIRCUMSCRIBED = 3  # Les cercles sont à l'extérieur l'un de l'autre et se touchent en un point (cercle circonscrit)
    NO_CROSS = 4       # Les cercles ne se coupent pas et ne se touchent pas

def circle_intersection(c1, c2):
    """
    Détermine la relation géométrique entre deux cercles donnés.

    Args:
        c1 (list or tuple): Premier cercle, sous forme (x1, y1, r1) où (x1, y1) est le centre et r1 est le rayon.
        c2 (list or tuple): Second cercle, sous forme (x2, y2, r2) où (x2, y2) est le centre et r2 est le rayon.

    Returns:
        Relation: Enum correspondant au type de relation géométrique entre les deux cercles.
    """
    x1, y1, r1 = c1
    x2, y2, r2 = c2

    # Calcul de la distance entre les centres des deux cercles
    d = distance((x1, y1), (x2, y2))

    # Si la distance est supérieure à la somme des rayons, aucun croisement
    if d - (r1 + r2) > 1e-10:
        return Relation.NO_CROSS
    # Si la distance est égale à la somme des rayons, les cercles sont tangents extérieurement (circonscrits)
    elif abs(d - (r1 + r2)) < 1e-10:
        return Relation.CIRCUMSCRIBED
    # Si la distance est strictement comprise entre la différence et la somme des rayons, intersection en deux points
    elif d - (r2 - r1) > 1e-10:
        return Relation.INTERSECT
    # Si la distance est égale à la différence des rayons, les cercles sont tangents intérieurement (inscrits)
    elif abs(d - (r2 - r1)) < 1e-10:
        return Relation.INSCRIBED
    # Sinon, un cercle est inclus strictement dans l'autre
    else:
        return Relation.INCLUDED

def distance(p1, p2):
    """
    Calcule la distance euclidienne entre deux points en 2D.

    Args:
        p1 (tuple): Premier point sous la forme (x1, y1).
        p2 (tuple): Second point sous la forme (x2, y2).

    Returns:
        float: La distance euclidienne entre les deux points.
    """
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def run():
    """
    Lit les caractéristiques de deux cercles depuis l'entrée standard,
    détermine leur relation géométrique et affiche le résultat sous forme de valeur d'énumération.

    Les cercles sont lus dans l'ordre (x, y, r) sur deux lignes.
    Si le premier cercle a un rayon supérieur au second, ils sont échangés pour simplifier l'analyse.
    """
    # Lecture et conversion des paramètres du premier cercle
    c1 = [int(i) for i in input().split()]
    # Lecture et conversion des paramètres du second cercle
    c2 = [int(i) for i in input().split()]

    # On s'assure que c1 a un rayon inférieur ou égal à c2 (important pour la logique de juxtaposition)
    if c1[2] > c2[2]:
        c1, c2 = c2, c1

    # Calcul de la relation et affichage du résultat (valeur entière correspondante à l'enum Relation)
    print(circle_intersection(c1, c2).value)

if __name__ == '__main__':
    run()