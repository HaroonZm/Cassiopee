#! /usr/bin/env python

# Importation des modules standards de Python, utilisés pour différentes tâches.
import os  # Module pour les opérations système (ici non utilisé dans le code).
import sys  # Module pour interagir avec le système d'exploitation et l'interpréteur Python (ici non utilisé explicitement).
import itertools  # Module pour les outils combinatoires et d'itérations (ici non utilisé dans le code).
import math  # Module fournissant des fonctions mathématiques standard (ici non utilisé dans le code).
from collections import Counter, defaultdict  # Importation de structures de données utiles pour compter et pour des dictionnaires avec valeurs par défaut (ici non utilisé dans le code).

# Définition d'une classe appelée Main.
class Main(object):  # On hérite explicitement de object pour compatibilité Python 2.

    def __init__(self):
        # Le constructeur est vide pour l'instant. Il pourrait servir à initialiser des attributs pour la classe Main.
        pass

    def solve(self):
        '''
        Cette fonction contient la logique principale du programme et fera toute la résolution du problème.
        '''
        # Boucle principale qui permet de traiter plusieurs jeux de données d'affilée.
        while True:
            # Lecture de deux entiers N et M à partir de l'entrée standard.
            # Chaque ligne est lue avec raw_input(), puis split() pour séparer les valeurs, et map(int, ...) pour convertir chaque chaîne en entier.
            N, M = map(int, raw_input().split())

            # Si les deux valeurs N et M sont égales à zéro en même temps, il s'agit du cas terminal, donc on sort de la boucle.
            if N == M == 0:
                break

            # Création d'un tableau à deux dimensions nommé "record".
            # Ce tableau va contenir pour chaque m (ligne), pour chaque t (colonne), une valeur initialisée à 0.
            # On crée M+1 lignes (pour chaque possible m de 1 à M inclus), et 2000 colonnes pour les valeurs possibles de t.
            # Par compréhension de liste, on répète [0]*2000 (une ligne de 2000 zéros) pour chaque i de 0 à M inclus.
            record = [[0] * 2000 for i in range(M+1)]

            # Lecture du nombre total d'enregistrements r à traiter pour ce cas de test, à l'aide de input().
            # input() lit une ligne de l'entrée standard et l'évalue comme une expression Python ; ici elle retourne un entier r.
            r = input()

            # Boucle qui va se répéter r fois pour lire chaque enregistrement.
            for i in range(r):
                # Lecture de quatre entiers via raw_input, séparés et convertis en int : t, n, m, s
                # t : l'heure ou l'indice de temps de l'évènement
                # n : un identifiant pour une personne (non utilisé ici)
                # m : l'identifiant d'une salle ou autre entité (index de ligne dans record)
                # s : un indicateur de type de changement (1 pour arrivée, 0 pour départ)
                t, n, m, s = map(int, raw_input().split())

                # Si s vaut 1, cela veut dire qu'un événement d'entrée s'est produit, on augmente la valeur correspondante de record.
                if s == 1:
                    record[m][t] += 1  # On incrémente la case correspondant à la salle m et au temps t.
                else:
                    # Sinon, s vaut autre chose (probablement 0), on décrémente la même case, représentant un événement de sortie.
                    record[m][t] -= 1

            # La boucle suivante sert à transformer le tableau record pour obtenir un effectif cumulé,
            # c'est-à-dire pour chaque salle (chaque m), le nombre de personnes présentes à chaque instant t.
            for i in range(1, M+1):
                # Pour chaque case de record[i] correspondant à la salle i, 
                # on boucle sur tous les instants j compris entre 540 et 1260 inclus (par convention, probablement des heures offertes : 9h à 21h).
                for j in range(540, 1261):
                    # On cumule la valeur précédente record[i][j-1] à la valeur courante record[i][j].
                    # Cela permet d'obtenir le nombre net de personnes présentes à chaque instant.
                    record[i][j] += record[i][j-1]

            # Lecture du nombre de requêtes q à traiter, toujours avec input() pour obtenir un entier.
            q = input()

            # Boucle sur toutes les requêtes.
            for i in range(q):
                # Lecture de trois entiers qui décrivent chaque requête : ts, te, m 
                # ts : temps de début (inclus)
                # te : temps de fin (exclu, car on boucle de ts à te-1 plus bas)
                # m : identifiant de la salle pour laquelle faire la requête
                ts, te, m = map(int, raw_input().split())

                # On initialise la variable de réponse de la requête à zéro.
                ans = 0

                # On va compter combien de créneaux horaires (de ts à te-1) dans la salle m sont occupés:
                for j in range(ts, te):
                    # Si, pour cet instant j et cette salle m, la valeur correspondante dans record est supérieure ou égale à 1,
                    # cela veut dire qu'il y a au moins une personne présente à ce moment-là.
                    if record[m][j] >= 1:
                        ans += 1  # On incrémente le compteur de créneaux occupés.

                # Affichage du résultat pour la requête courante.
                print ans  # Affiche directement la valeur (en Python 2, print est une instruction, pas une fonction).

        # À la fin, on retourne None explicitement, même si ce n'est pas strictement nécessaire.
        return None

# Ceci vérifie si le script est exécuté directement (pas importé comme module).
if __name__ == '__main__':
    # On crée une instance de la classe Main.
    m = Main()
    # On appelle sa méthode solve() pour exécuter la logique principale.
    m.solve()