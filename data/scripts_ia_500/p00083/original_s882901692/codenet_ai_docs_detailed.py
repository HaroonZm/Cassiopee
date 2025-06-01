#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def determine_era(date):
    """
    Détermine l'ère japonaise correspondant à une date donnée.

    Cette fonction prend une date sous forme de tuple (année, mois, jour),
    et compare cette date avec les périodes des différentes ères japonaises
    modernes (Meiji, Taisho, Showa, Heisei).

    Paramètres:
    ----------
    date : tuple(int, int, int)
        Un tuple contenant l'année, le mois et le jour.

    Retour:
    -------
    str
        Une chaîne indiquant l'ère. Pour les époques modernes,
        la chaîne est suivie de l'année dans l'ère, du mois et du jour,
        sous forme: "era anno_mois_jour".
        Pour les dates avant 1868-09-08, retourne "pre-meiji".

    Exemples:
    ---------
    >>> determine_era((1870, 4, 10))
    'meiji 3 4 10'
    >>> determine_era((1860, 1, 1))
    'pre-meiji'
    """
    # Comparaison avec les limites des ères historiques japonaises
    if date < (1868, 9, 8):
        # Date antérieure à l'ère Meiji
        return 'pre-meiji'
    elif date < (1912, 7, 30):
        # Ère Meiji : commence en 1868-09-08 jusqu'à 1912-07-29
        # L'année dans l'ère est l'année grégorienne moins 1867
        era_year = date[0] - 1867
        return 'meiji {} {} {}'.format(era_year, date[1], date[2])
    elif date < (1926, 12, 25):
        # Ère Taisho : commence en 1912-07-30 jusqu'à 1926-12-24
        era_year = date[0] - 1911
        return 'taisho {} {} {}'.format(era_year, date[1], date[2])
    elif date < (1989, 1, 8):
        # Ère Showa : commence en 1926-12-25 jusqu'à 1989-01-07
        era_year = date[0] - 1925
        return 'showa {} {} {}'.format(era_year, date[1], date[2])
    else:
        # Ère Heisei : commence en 1989-01-08
        era_year = date[0] - 1988
        return 'heisei {} {} {}'.format(era_year, date[1], date[2])

def main():
    """
    Lit les lignes depuis l'entrée standard, chacune représentant une date au format
    "année mois jour", les convertit en tuples d'entiers, puis affiche l'ère japonaise
    correspondante avec l'année, le mois et le jour dans cette ère.

    Fonctionnement:
    --------------
    - Chaque ligne lue sur stdin est supposée contenir 3 entiers séparés par des espaces.
    - Chaque date est interprétée et convertie en l'ère japonaise correspondante.
    - Le résultat est affiché sur stdout.
    """
    for line in stdin:
        # Nettoie la ligne et convertit les valeurs en entiers pour former la date
        date = tuple(int(s) for s in line.split())
        # Déterminer l'ère et afficher le résultat
        print(determine_era(date))

if __name__ == '__main__':
    main()