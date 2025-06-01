"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0123
"""
import sys

def solve(r500, r1000):
    """
    Détermine le classement (rank) d'un moniteur de fréquence cardiaque basé sur deux mesures :
    r500 : FCM à 500 kcal/min
    r1000 : FCM à 1000 kcal/min

    Le classement est déterminé selon des critères spécifiques avec des seuils de fréquence cardiaque
    comparés aux mesures fournies. Le résultat est un code de rang (par exemple, 'AAA', 'AA', etc.).

    Args:
        r500 (float): Fréquence cardiaque à 500 kcal/min.
        r1000 (float): Fréquence cardiaque à 1000 kcal/min.

    Returns:
        str: Le rang correspondant selon les critères. Si aucune condition n'est remplie, retourne 'NA'.
    """
    # Liste des critères avec seuils pour r500, r1000 et le rang associé.
    criteria = [
        (35.50,  71.0, 'AAA'),
        (37.50,  77.0, 'AA'),
        (40.0,   83.0, 'A'),
        (43.0,   89.0, 'B'),
        (50.0,  105.0, 'C'),
        (55.0,  116.0, 'D'),
        (70.0,  148.0, 'E')
    ]

    rank = None  # Initialisation du rang à None

    # Parcours de chaque critère afin de vérifier si r500 et r1000 sont inférieurs aux seuils donnés
    for c500, c1000, r in criteria:
        if r500 < c500 and r1000 < c1000:
            rank = r  # Attribue le rang correspondant
            break    # Sort de la boucle dès qu'un rang est trouvé

    # Si aucun critère n'a été satisfait, le rang est 'NA' (non applicable)
    if rank is None:
        rank = 'NA'

    return rank


def main(args):
    """
    Fonction principale qui lit les entrées depuis stdin.
    Chaque ligne contient deux valeurs flottantes représentant r500 et r1000.

    Pour chaque ligne lue, elle calcule le rang à l'aide de la fonction solve
    et imprime le résultat sur stdout.

    Args:
        args (list): Liste des arguments en ligne de commande (non utilisée ici).
    """
    for line in sys.stdin:
        # Extraction des deux valeurs float sur la ligne après suppression des espaces
        r500, r1000 = [float(x) for x in line.strip().split()]
        # Calcul du rang avec la fonction solve
        result = solve(r500, r1000)
        # Affichage du rang déterminé
        print(result)


if __name__ == '__main__':
    # Exécution du programme principal avec les arguments de la ligne de commande (non utilisés)
    main(sys.argv[1:])