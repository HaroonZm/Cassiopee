#!/usr/bin/env python

import sys
import datetime

"""
Ce programme lit plusieurs ensembles de données depuis l'entrée standard.
Chaque ensemble de données est composé de deux entiers sur une même ligne,
représentant le mois et le jour respectivement.
Le programme s'arrête lorsque le mois est égal à 0.

Pour chaque ensemble de données valide, il affiche le jour de la semaine en anglais
correspondant à la date donnée dans l'année 2004.

Les noms des jours de la semaine sont les suivants :
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
"""

def get_weekday(month, day):
    """
    Calcule le jour de la semaine en anglais pour une date donnée.

    Args:
        month (int): Le numéro du mois (1 à 12).
        day (int): Le jour du mois.

    Returns:
        str: Le nom du jour de la semaine en anglais correspondant à la date.
             Les valeurs possibles sont : "Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday".

    Remarque:
        La fonction utilise l'année 2004 comme année de référence, car c'est une année bissextile,
        ce qui est utile pour gérer la validité des dates.
    """
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    # datetime.date.weekday() renvoie un entier de 0 (lundi) à 6 (dimanche)
    return weekdays[datetime.date(2004, month, day).weekday()]

def main():
    """
    Fonction principale qui lit les entrées et affiche les jours de la semaine.

    Elle lit en boucle chaque ligne de l'entrée standard, qui doit contenir deux entiers
    séparés par un espace représentant le mois et le jour.
    Si le mois vaut 0, la boucle s'interrompt et le programme se termine.

    Pour chaque mois différent de 0, elle calcule et affiche le jour de la semaine correspondant.
    """
    while True:
        # Lire une ligne depuis l'entrée standard
        s = sys.stdin.readline()
        # Convertir les deux valeurs en entiers : mois et jour
        month, day = [int(x) for x in s.split()]
        # Condition d'arrêt : si le mois est 0, quitter la fonction
        if month == 0:
            return
        # Afficher le jour de la semaine correspondant à la date donnée
        print(get_weekday(month, day))

if __name__ == '__main__':
    main()