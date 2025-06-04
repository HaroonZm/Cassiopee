"""
URL du problème : http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0513
Cette solution a été jugée AC (Accepted)
"""

import sys                            # Importe le module "sys", qui fournit un accès à certaines variables utilisées ou maintenues par l'interpréteur Python.
from sys import stdin                 # Depuis le module "sys", importe précisément "stdin", qui fait référence à l'entrée standard (typiquement le clavier ou un flux de fichier).
from itertools import chain           # Importe "chain" du module "itertools", qui permet de chaîner des listes ou des itérables ensemble en un seul itérable.
input = stdin.readline                # Redéfinit "input" pour le rendre équivalent à "stdin.readline". Cela permet de lire rapidement des lignes de l'entrée standard, généralement plus efficace que la fonction "input()" native.

def flatten(listOfLists):
    """
    Cette fonction prend en argument une liste composée de plusieurs listes imbriquées à un seul niveau,
    puis retourne toutes les valeurs de ces sous-listes comme une seule séquence plate.
    Exemple : flatten([[1,2],[3,4]]) => 1,2,3,4
    Ici, la fonction utilise chain.from_iterable, qui est plus rapide qu'une double boucle.
    """
    return chain.from_iterable(listOfLists)

def cut(k):
    """
    Cette fonction réalise l'opération de "cut" (couper le paquet de cartes).
    Paramètre :
     - k : indique où couper le paquet de cartes. Les k premières cartes deviennent les dernières.
    Utilise la variable globale 'cards' pour manipuler la liste des cartes.
    L'opération consiste à diviser cards en deux sous-listes, puis à les concaténer en inversant leur ordre.
    """
    global cards                        # Indique que l'on veut manipuler la variable globale 'cards', et pas en définir une nouvelle locale.
    yellow = cards[:k]                  # "yellow" contient les k premières cartes du paquet.
    blue = cards[k:]                    # "blue" contient toutes les cartes restantes après le k-ième élément.
    cards = blue + yellow               # "cards" devient la concaténation de "blue" suivi de "yellow". Les premières cartes vont à la fin.

def shuffle():
    """
    Cette fonction réalise ce qui est appelé un "shuffle" (mélange spécial).
    Sépare le paquet de cartes en deux moitiés, puis alterne une carte de chaque moitié.
    Utilise la variable globale 'cards' (liste complète des cartes) et 'N' (taille de chaque moitié).
    Exemple : pour cards=[1,2,3,4], après shuffle() => [1,3,2,4]
    """
    global cards                        # Manipule la variable globale 'cards'
    yellow = cards[:N]                  # "yellow" correspond à la première moitié du paquet.
    blue = cards[N:]                    # "blue" est la seconde moitié.
    temp = [[y, b] for y, b in zip(yellow, blue)]   # Utilise zip pour assembler les deux moitiés deux à deux. Chaque paire devient une petite liste [y, b].
    cards = list(flatten(temp))         # "temp" est une liste de petites listes. On l'aplatit en une seule liste avec flatten, puis on la remet dans "cards".

cards = []  # Déclare la variable globale 'cards' comme une liste vide.

def main(args):
    """
    Fonction principale. Exécute les différentes opérations de mélange sur le paquet de cartes en fonction de l'entrée utilisateur.
    - Lit le nombre de cartes par paquet (n).
    - Initialise le paquet de cartes (numérotées de 1 à 2n inclus).
    - Applique m opérations successives (shuffle/cut), selon les commandes reçues.
    - Affiche finalement le résultat.
    """
    global cards                        # Spécifie que l'on va manipuler la variable globale 'cards' dans cette fonction.
    n = int(input())                    # Lit une ligne, la convertit en entier, stocke dans 'n'. Cela correspond à la moitié du paquet de cartes.
    N = n                               # Nombre de cartes dans chacune des deux moitiés (sert à shuffle()).
    m = int(input())                    # Lit le nombre d'opérations effectuées sur le paquet.

    # Initialise le paquet de cartes.
    # cards = [1, 2, ..., 2n]
    cards = [x for x in range(1, (2 * n) + 1)]     # Crée une liste contenant les cartes de 1 à 2n inclusivement.

    # Pour chaque opération à effectuer sur le paquet
    for _ in range(m):
        op = int(input())              # Lit la prochaine opération (0 ou un entier positif) et la convertit en entier.
        if op == 0:
            # Si 'op' vaut 0, alors on effectue un shuffle spécial
            # Cette opération intercale les deux moitiés du paquet
            temp = [[y, b] for y, b in zip(cards[:n], cards[n:])]  # zip assemble chaque carte de la première moitié avec celle de la seconde
            cards = list(flatten(temp))      # On aplatit temp pour obtenir la nouvelle liste de cartes après shuffle
        else:
            # Si 'op' est différent de 0, on effectue un "cut" à l'endroit 'op'
            # Cela signifie que les op premières cartes vont à la fin du paquet
            cards = cards[op:] + cards[:op]  # Crée une nouvelle liste avec les cartes réordonnées selon la coupe

    # Affiche le paquet de cartes final, une carte par ligne
    print('\n'.join(map(str, cards)))        # map transforme chaque élément de cards en chaîne de caractères, puis join assemble chaque carte sur une nouvelle ligne

# Point d'entrée standard d'un script Python
if __name__ == '__main__':                 # Vérifie si ce fichier est exécuté comme programme principal et non importé comme module dans un autre script
    main(sys.argv[1:])                     # Appelle la fonction main. sys.argv[1:] contient les arguments de la ligne de commande (non utilisés ici, mais requis par la signature attendue).