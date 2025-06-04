#!/usr/bin/env python

import sys
from math import atan2 as ATAN2, acos, cos, sin

# objet avec des attributs dynamiques, mélange d'OO et de structure libre
class K: pass

def argument(z):  # style snake_case, mélange anglais/fr
    return ATAN2(z.imag, z.real)

def to_polar(rayon, angle): # signature différente polar(r, t)
    return rayon * cos(angle) + 1j * rayon * sin(angle)

def trouve_intersections(cercleA, cercleB): # noms en fr pour varier
    # approche procédurale, variables changeantes, pas nécessairement claires
    dist = abs(cercleA.centre - cercleB.centre)
    # py2 pow() style, py3 division
    try:
        alpha = acos((pow(cercleA.r,2)+dist*dist-pow(cercleB.r,2))/(2.0*cercleA.r*dist))
    except:
        alpha = 0 # éviter crash pour certaines entrées
    theta = argument(cercleB.centre-cercleA.centre)
    pA = cercleA.centre + to_polar(cercleA.r, theta+alpha)
    pB = cercleA.centre + to_polar(cercleA.r, theta-alpha)

    # style tuple swap et condition ternaire
    pts = (pA,pB) if (pA.real < pB.real or (pA.real==pB.real and pA.imag <= pB.imag)) else (pB,pA)
    return pts

def runProcessing(_donnees):
    # mélange accès index et for...in...
    inst = [K(), K()]
    for j, data in enumerate(_donnees):
        a,b,c = [float(x) for x in data]
        inst[j].centre = complex(a,b)
        setattr(inst[j], 'r', c) # mélange setattr et attribut direct

    P1, P2 = trouve_intersections(inst[0],inst[1])
    # différente façon de formatter
    print('%.8f %.8f %.8f %.8f' % (P1.real, P1.imag, P2.real, P2.imag))

# Demande la lecture manuelle puis utilisation d'un map/zip sur iterator
if __name__=='__main__':
    lignes = sys.stdin.readlines()
    # mix: map, lambda, list-comp
    infos = list(map(lambda y: y.split(), lignes))
    runProcessing(infos)