import sys
from sys import stdin

# Redéfinition de la fonction input pour lire efficacement les lignes depuis stdin
input = stdin.readline

def main(args):
    """
    Lit des séries de données comportant 5 paires de nombres entiers, représentant les ventes du matin (am)
    et de l'après-midi (pm) de cinq magasins. Pour chaque série, identifie le magasin ayant la plus grande
    vente totale (am + pm) et affiche la lettre du magasin (A à E) suivie de la vente totale maximale.
    Le programme s'arrête quand une paire (0, 0) comme première entrée d'une série est fournie.

    Args:
        args (list): Arguments de la ligne de commande non utilisés dans ce programme.
    """
    while True:
        # Lecture de la première paire am/pm
        am, pm = map(int, input().split())
        # Condition d'arrêt : si am == 0 et pm == 0, on termine le programme.
        if am == 0 and pm == 0:
            break

        # Initialisation de la liste des ventes totales pour les 5 magasins
        totals = [0] * 5
        # Calcul de la vente totale pour le premier magasin
        totals[0] = am + pm

        # Lecture et calcul pour les 4 magasins suivants
        for i in range(1, 5):
            am, pm = map(int, input().split())
            totals[i] = am + pm

        # Recherche de la plus grande vente et de l'indice du magasin correspondant
        top = max(totals)
        shop = totals.index(top)

        # Affichage de la lettre correspondant au magasin ('A', 'B', ..., 'E') et de la vente maximale
        print('{} {}'.format(chr(ord('A') + shop), top))

if __name__ == '__main__':
    # Lancement du programme principal, les arguments de la ligne de commande ne sont pas utilisés ici
    main(sys.argv[1:])