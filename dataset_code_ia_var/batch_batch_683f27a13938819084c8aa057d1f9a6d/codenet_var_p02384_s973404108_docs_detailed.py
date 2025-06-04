from enum import Enum
import sys
import math

# Constantes utilisées dans le programme
BIG_NUM = 2000000000       # Un grand nombre arbitraire, généralement utilisé pour l'initialisation de minimum/maximum
MOD = 1000000007           # Une valeur de modulo typiquement utilisée dans des problèmes de programmation compétitive
EPS = 0.000000001          # Une petite valeur epsilon pour la comparaison de flottants

# Indices des faces du dé (pour référence) :
# 0: Dessus, 1: Devant, 2: Droite, 3: Gauche, 4: Derrière, 5: Face opposée au dessus

class Dice:
    """
    Classe représentant un dé à 6 faces.
    Permet de simuler des rotations du dé et de répondre à des requêtes sur la position des nombres sur les faces.
    """

    def __init__(self):
        """
        Initialise un dé avec une disposition standard des faces.
        Initialise également l'ordre des rotations possibles pour retrouver toute configuration.
        """
        self.number = [i for i in range(6)]  # Valeurs actuelles des faces du dé
        self.work = [i for i in range(6)]    # Liste de travail utilisée lors des rotations
        # Séquence d'ordres pour permettre d'atteindre toutes configurations de faces
        self.order = 'NNNNWNNNWNNNENNNENNNWNNN'

    def setNumber(self, n0, n1, n2, n3, n4, n5):
        """
        Attribue les valeurs aux six faces du dé.

        Args:
            n0: Valeur de la face supérieure (top).
            n1: Valeur de la face avant (front).
            n2: Valeur de la face droite.
            n3: Valeur de la face gauche.
            n4: Valeur de la face arrière.
            n5: Valeur de la face opposée (bottom).
        """
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5

    def roll(self, loc):
        """
        Fait tourner le dé dans une des quatre directions cardinales (E, N, S, W).

        Args:
            loc: Un caractère représentant la direction ('E', 'N', 'S' ou 'W')
        """
        # Copie des valeurs actuelles avant manipulation
        for i in range(6):
            self.work[i] = self.number[i]

        if loc == 'E':
            # Rotation vers l'est
            # Les indices évoluent ainsi : gauche -> dessus, dessus -> droite, droite -> dessous, dessous -> gauche
            self.setNumber(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        elif loc == 'N':
            # Rotation vers le nord
            # Les indices évoluent ainsi : avant -> dessus, dessous -> avant, dessus -> arrière, arrière -> dessous
            self.setNumber(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif loc == 'S':
            # Rotation vers le sud (inverse du nord)
            self.setNumber(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1])
        elif loc == 'W':
            # Rotation vers l'ouest (inverse de l'est)
            self.setNumber(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])

    def query(self, top_num, front_num):
        """
        Trouve et retourne la valeur de la face droite lorsque la face supérieure vaut 'top_num' et la face avant vaut 'front_num'.

        Args:
            top_num: Valeur recherchée sur la face du dessus.
            front_num: Valeur recherchée sur la face avant.

        Returns:
            La valeur sur la face droite dans cette configuration,
            ou -1 si aucune configuration correspondante n'a été trouvée.
        """
        # Sauvegarde de l'état actuel du dé afin de restaurer ultérieurement
        self.save_data = [i for i in range(6)]
        for i in range(len(self.number)):
            self.save_data[i] = self.number[i]

        ret = -1  # Valeur retournée en cas de configuration non trouvée

        # Itération sur toutes les rotations nécessaires pour atteindre n'importe quelle configuration du dé
        for i in range(len(self.order)):
            self.roll(self.order[i])
            # On vérifie si le dessus et l'avant sont dans la bonne configuration
            if self.number[0] == top_num and self.number[1] == front_num:
                ret = self.number[2]  # On retourne la valeur de la face droite (indice 2)
                break

        # Restauration de la configuration initiale du dé
        for i in range(len(self.number)):
            self.number[i] = self.save_data[i]

        return ret

# Lecture des valeurs initiales des faces du dé fournies par l'utilisateur
dice = Dice()
table = list(map(int, input().split()))
dice.setNumber(table[0], table[1], table[2], table[3], table[4], table[5])

# Lecture du nombre de requêtes à traiter
num_query = int(input())
for loop in range(num_query):
    # Pour chaque requête : lire dessus et avant, puis répondre avec la valeur à droite
    top_num, front_num = map(int, input().split())
    print("%d" % (dice.query(top_num, front_num)))