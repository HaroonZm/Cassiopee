import sys  # On importe le module sys afin d'accéder à des fonctionnalités système comme les arguments ou stdin.
from sys import stdin  # On importe spécifiquement stdin de sys afin de lire plus efficacement l'entrée standard.

# On redéfinit la fonction d'entrée input pour lire plus rapidement avec stdin.readline (plus rapide que input()).
input = stdin.readline

def closest_part(points, n):
    """
    Cette fonction cherche la distance minimale entre deux points dans une liste de points 'points',
    où chaque point est représenté par un tuple (x, y). Elle utilise un algorithme de type 'Divide-and-Conquer',
    qui divise le problème en sous-problèmes plus petits pour le résoudre plus efficacement qu'une double boucle naïve.
    Elle renvoie le carré de la plus petite distance trouvée.
    """

    # Cas de base : si le sous-ensemble contient au plus 1 point, on ne peut pas former une paire, donc la distance infinie.
    if n <= 1:
        return float('inf')  # L'infini représente l'absence de solution valable.

    # On sépare le tableau en deux moitiés.
    m = n // 2  # On calcule l'indice du milieu pour séparer en deux groupes à peu près égaux.
    x = points[m][0]  # On récupère la coordonnée x du point situé au milieu, qui servira de séparation.

    # Appel récursif sur chacune des deux moitiés, on calcule la plus petite distance possible dans chaque partie.
    # closest_part(points[:m], m) : partie gauche (du début jusqu'à l'indice m exclus)
    # closest_part(points[m:], n-m) : partie droite (de l'indice m jusqu'à la fin)
    d = min(closest_part(points[:m], m), closest_part(points[m:], n - m))
    # Maintenant, 'd' contient la meilleure (plus petite) distance trouvée dans les deux moitiés.

    # Pour combiner les solutions, on doit vérifier la 'bande' centrale de largeur sqrt(d)
    # On trie la liste temporairement selon la coordonnée y, ce qui est essentiel à l'optimisation du temps.
    points.sort(key=lambda p: p[1])  # Ici, p est un tuple (x, y). On trie du plus petit au plus grand par y.

    # On crée une liste pour mémoriser les points qui sont proches de la séparation centrale en x.
    b = []

    # Pour chaque point p du tableau trié selon y :
    for p in points:
        # On vérifie si le point p est suffisamment proche de la médiane x pour qu'une paire potentiellement plus courte existe.
        # Le carré de la différence en x doit être strictement inférieur à la distance minimale actuelle (d).
        if (p[0] - x) ** 2 >= d:
            continue  # Si ce n'est pas le cas, on passe au point suivant, car il ne peut pas battre d.

        # On compare p à tous les points q mémorisés dans b (dont l'ordonnée y est proche)
        for q in b:
            dx = p[0] - q[0]  # Différence horizontale.
            dy = p[1] - q[1]  # Différence verticale.
            # Comme b est dans l'ordre décroissant de y (insertion en tête),
            # dès que la différence en y au carré excède d, on peut arrêter.
            if dy ** 2 >= d:
                break  # Aucun autre q ne pourra donner une meilleure distance, donc on arrête la boucle.
            d = min(d, dx ** 2 + dy ** 2)  # Si la paire (p, q) est plus rapprochée, on met à jour d.

        # On insère p en tête de b pour garantir que b est trié du plus grand au plus petit y.
        b.insert(0, p)

    # On retourne finalement la plus petite distance au carré trouvée pour cette partie.
    return d

def main(args):
    """
    Fonction principale du programme. Elle lit les entrées, appelle l'algorithme principal, et affiche la solution.
    """
    n = int(input())  # On lit le nombre de points à traiter, en convertissant l'entrée en entier.
    # On construit une liste de tuples, chaque tuple représentant les coordonnées (x, y) d'un point données ligne par ligne.
    points = [tuple(map(int, input().split())) for _ in range(n)]
    # On trie la liste initiale selon les coordonnées x, condition requise pour le bon fonctionnement de l'algorithme.
    points.sort()

    # On appelle la fonction qui va calculer la distance minimale et on stocke le résultat dans 'result'.
    result = closest_part(points, n)
    # On affiche le résultat final (c'est le carré de la distance la plus courte).
    print(result)

# Ce test permet de lancer la fonction main() uniquement si le script est exécuté directement, pas importé comme module.
if __name__ == '__main__':
    main(sys.argv[1:])  # On passe les arguments de la ligne de commande à main, sauf le premier (nom du script).