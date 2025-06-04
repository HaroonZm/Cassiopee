#!/usr/bin/python

# Importation du module os, qui permet d'interagir avec le système d'exploitation
import os
# Importation du module sys, qui fournit un accès à certaines variables et fonctions liées à l'interpréteur Python
import sys
# Importation du module math, qui offre des fonctions mathématiques telles que sqrt (racine carrée)
import math

# Définition de la fonction principale de résolution du problème.
# Elle prend en paramètre un objet f qui permet de lire les entrées.
def solve(f):
    # Lecture d'un entier représentant le nombre d'éléments à traiter.
    n = f.read_int()
    # Si ce nombre est zéro, cela signifie la fin des données, donc on arrête la boucle en levant une exception appropriée.
    if n == 0:
        raise StopIteration
    # Création d'une liste ary contenant n éléments, où chaque élément est une liste de flottants lue depuis l'entrée.
    # Pour chaque élément, on utilise la méthode read_float_list() de l'objet f pour lire une ligne de flottants sous forme de liste.
    ary = [f.read_float_list() for _ in xrange(n)]

    # Définition initiale des bornes sur l'axe des x.
    # x_min correspond à la valeur minimale possible pour x, ici -100.0.
    x_min = -100.0
    # x_max correspond à la valeur maximale possible pour x, ici 100.0.
    x_max = 100.0

    # Effectuer 60 itérations pour chercher la meilleure valeur de x possible.
    # Il s'agit d'une recherche ternaire qui réduit progressivement l'intervalle [x_min, x_max].
    for _ in xrange(60):
        # Calcul de c1, qui est le premier point de découpage dans la recherche ternaire sur x.
        # Il correspond à un tiers du chemin entre x_min et x_max.
        c1 = (x_min*2 + x_max) / 3
        # Calcul de c2, le second point de découpage, aux deux-tiers de l'intervalle.
        c2 = (x_min + x_max*2) / 3
        # On compare le résultat de search_y(ary, c1) avec search_y(ary, c2).
        # search_y trouve la "meilleure" valeur de y pour un x donné ; ici, on cherche le maximum (puisqu'on compare >).
        if search_y(ary, c1) > search_y(ary, c2):
            # Si c1 est meilleur que c2, la meilleure valeur se situe entre x_min et c2.
            x_max = c2
        else:
            # Sinon, elle se situe entre c1 et x_max.
            x_min = c1

    # La recherche ternaire sur x étant terminée, on calcule la meilleure valeur possible,
    # puis on applique la racine carrée à celle-ci (car il s'agissait de carrés de distances ou de rayons).
    # La valeur x_max est utilisée ici pour obtenir le résultat final.
    return math.sqrt(search_y(ary, x_max))

# Fonction auxiliaire qui effectue une recherche ternaire mais sur l'axe y pour une valeur de x donnée.
def search_y(ary, x):
    # Définition initiale des bornes sur l'axe des y, correspondant à l'espace de recherche
    y_min = -100.0
    y_max = 100.0

    # Effectuer 60 itérations pour raffiner la valeur de y.
    for _ in xrange(60):
        # Calcul des points de tiers c1 et c2.
        c1 = (y_min*2 + y_max) / 3
        c2 = (y_min + y_max*2) / 3
        # On compare la fonction calc(ary, x, ...) en c1 et c2.
        if calc(ary, x, c1) > calc(ary, x, c2):
            # Si c1 produit une valeur supérieure, la meilleure zone est entre y_min et c2.
            y_max = c2
        else:
            # Sinon, entre c1 et y_max.
            y_min = c1

    # A la fin de la recherche, on retourne la valeur maximale résultante pour y_max.
    return calc(ary, x, y_max)

# Fonction calc qui effectue un calcul sur la liste ary pour un point (x, y) donné.
# Elle retourne la plus petite valeur d'une expression mathématique pour chaque élément de ary.
def calc(ary, x, y):
    # Pour chaque item dans ary, on calcule l'expression suivante :
    # item[2] ** 2 : le carré du troisième élément (supposément un rayon ou une distance)
    # (item[0] - x) ** 2 : le carré de la différence entre le premier élément et x
    # (item[1] - y) ** 2 : le carré de la différence entre le second élément et y
    # On soustrait la somme des deux derniers du carré du rayon).
    # On rassemble toutes ces valeurs dans une liste et on retourne la plus petite d'entre elles grâce à min().
    return min([
        item[2] ** 2 - (item[0] - x) ** 2 - (item[1] - y) ** 2
        for item in ary
    ])

# Définition d'une classe Reader destinée à faciliter la lecture des données depuis un fichier ou depuis l'entrée standard.
class Reader(object):
    # Constructeur de la classe.
    def __init__(self, filename=None):
        # Indique si le mode test est activé, c'est-à-dire si un fichier d'entrée a été spécifié.
        self.test_mode = filename is not None
        # Nombre de cas à traiter, initialisé à 1.
        self.cases = 1
        # Buffer pour stocker les lignes lues du fichier, utile pour la lecture séquentielle.
        self.buffer = []
        # Si le mode test est activé (donc un fichier d'entrée est donné)
        if self.test_mode:
            # Ouverture du fichier en lecture (mode par défaut)
            with open(filename) as f:
                # Flag pour repérer les lignes blanches (séparations éventuelles entre cas)
                blank_flg = False
                # Lecture ligne par ligne
                for line in f:
                    # Suppression des espaces en début et fin de ligne
                    line = line.strip()
                    # Si la ligne n'est pas vide
                    if line:
                        # On l'ajoute au buffer de lecture
                        self.buffer.append(line)
                        # On note que la dernière ligne n'était pas vide
                        blank_flg = False
                    else:
                        # Si une nouvelle ligne vide vient d'être rencontrée et que la précédente n'était pas blanche
                        if not blank_flg:
                            # On incrémente le nombre de cas (case count)
                            self.cases += 1
                        # On note que la ligne courante est vide
                        blank_flg = True

    # Méthode interne qui lit une ligne du buffer s'il existe (fichier), ou depuis l'entrée standard sinon
    def __readline(self):
        # Si le mode test est activé (lecture depuis le fichier), on extrait la première ligne du buffer (suppression en même temps)
        return self.buffer.pop(0) if self.test_mode else raw_input()

    # Méthode pour lire et convertir la prochaine ligne en entier
    def read_int(self):
        return int(self.__readline())

    # Méthode pour lire et convertir la prochaine ligne en virgule flottante
    def read_float(self):
        return float(self.__readline())

    # Méthode pour lire et convertir la prochaine ligne en long (typiquement sur Python 2)
    def read_long(self):
        return long(self.__readline())

    # Méthode pour lire la prochaine ligne comme chaîne de caractères
    def read_str(self):
        return self.__readline()

    # Méthode pour lire une liste d'entiers depuis une ligne d'entrée (les valeurs séparées par des espaces)
    def read_int_list(self):
        return [int(item) for item in self.__readline().split()]

    # Méthode pour lire une liste de flottants depuis une ligne
    def read_float_list(self):
        return [float(item) for item in self.__readline().split()]

    # Méthode pour lire une liste de long depuis une ligne
    def read_long_list(self):
        return [long(item) for item in self.__readline().split()]

    # Méthode pour lire une liste de chaînes de caractères
    def read_str_list(self):
        return self.__readline().split()

# Partie principale du programme, point d'entrée s'il est lancé comme script
if __name__ == '__main__':
    # Si un argument est passé en ligne de commande, on l'utilise comme nom de fichier, sinon aucun fichier
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    # Création d'une instance de Reader en lui passant le nom du fichier (ou rien)
    f = Reader(filename)
    # Boucle permettant d'exécuter la fonction solve jusqu'à ce qu'une exception StopIteration soit levée (fin des données)
    while True:
        try:
            # Appel de la fonction solve pour le prochain cas et impression du résultat à l'écran
            print solve(f)
        except StopIteration:
            # Si plus de cas à traiter, on sort de la boucle
            break