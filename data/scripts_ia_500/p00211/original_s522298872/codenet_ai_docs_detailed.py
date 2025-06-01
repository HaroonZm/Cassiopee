from sys import stdin
readline = stdin.readline

from fractions import Fraction
from fractions import gcd
from functools import reduce

from collections import namedtuple
Runner = namedtuple('Runner', 'd v')

def common_denominator(r0, ri):
    """
    Calcule le dénominateur commun entre deux fractions représentant les temps des coureurs.
    
    Paramètres:
    - r0 (Runner) : Le premier coureur avec ses attributs d (distance) et v (vitesse).
    - ri (Runner) : Un autre coureur avec ses attributs d (distance) et v (vitesse).
    
    Retour:
    - int : Le dénominateur de la fraction représentant le rapport entre les temps des deux coureurs.
    """
    # Calcul du temps relatif sous forme de fraction : (distance0 * vitesse_i) / (vitesse0 * distance_i)
    # On récupère ensuite le dénominateur de cette fraction pour trouver un multiple commun.
    return Fraction(r0.d * ri.v, r0.v * ri.d).denominator

def lcm(a, b):
    """
    Calcule le plus petit commun multiple (PPCM) de deux entiers.
    
    Paramètres:
    - a (int) : Premier entier.
    - b (int) : Deuxième entier.
    
    Retour:
    - int : Le plus petit commun multiple de a et b.
    """
    # Le PPCM est donné par le produit divisé par le plus grand commun diviseur (PGCD)
    return a * b // gcd(a, b)

while True:
    # Lire le nombre de coureurs
    n = int(readline())
    if n == 0:
        # Condition de sortie si aucun coureur n'est donné
        break

    # Lecture des données de chaque coureur : distance et vitesse
    runners = [Runner(*map(int, readline().split())) for _ in range(n)]
    
    # Calcul des dénominateurs communs entre le premier coureur et chaque autre coureur
    denominators = [common_denominator(runners[0], ri) for ri in runners[1:]]
    
    # Calcul du PPCM de tous ces dénominateurs pour synchroniser les temps
    round_of_0 = int(reduce(lcm, denominators))
    
    # Calcul du temps total correspondant au coureur de référence (le premier), en prenant en compte le PPCM
    time = Fraction(runners[0].d * round_of_0, runners[0].v)
    
    # Pour chaque coureur, on calcule et affiche son temps correspondant en ajustant avec distance et vitesse
    for ri in runners:
        print(time * ri.v / ri.d)