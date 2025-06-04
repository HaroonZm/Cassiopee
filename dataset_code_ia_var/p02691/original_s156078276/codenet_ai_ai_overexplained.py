from collections import defaultdict  # Importation de defaultdict, qui permet de créer un dictionnaire avec une valeur par défaut

def solve(*args: str) -> str:
    # La fonction solve prend un nombre variable d'arguments de type chaîne de caractères
    # Chaque argument passé à la fonction solve est une chaîne, soit les lignes du problème

    n = int(args[0])  # Conversion de la première ligne (taille du tableau) en entier et stockage dans n

    # La deuxième ligne (args[1]) contient la liste des entiers sous forme de chaîne de caractères, séparés par des espaces
    # La méthode split() divise cette chaîne en une liste de sous-chaînes pour chaque entier
    # La fonction map applique la conversion int à chacune de ces sous-chaînes, créant alors une séquence d'entiers
    # La fonction list convertit cette séquence en une liste d'entiers
    A = list(map(int, args[1].split()))

    ret = 0  # Initialisation d'un compteur à zéro. Ce compteur va contenir le résultat final.

    X = defaultdict(int)  # Création d'un dictionnaire spécial (defaultdict) où chaque clé inexistante a pour valeur par défaut 0

    # Début d'une boucle qui parcourt simultanément les indices et les valeurs de la liste A
    # La fonction enumerate(A) génère des paires (indice, valeur) pour chaque élément de la liste A
    for i, a in enumerate(A):
        # Pour chaque élément a à l'indice i, on calculera la clé (a + i)
        # On incrémente ensuite la valeur dans X pour cette clé de 1
        # Cela ajoute 1 à la clé (a + i) dans le dictionnaire, ou la crée avec une valeur initiale de 1 si elle n'existait pas
        X[a + i] += 1

        # On vérifie si la différence (i - a) est positive ou nulle. Cela empêche d'utiliser des indices négatifs ou hors bornes dans certaines logiques.
        if 0 <= i - a:
            # Si la condition précédente est vraie, on ajoute la valeur associée à la clé (i - a) dans X à ret
            # Si la clé (i - a) n'existe pas dans X, grâce à defaultdict, sa valeur est 0, donc on ajoute 0 sans erreur
            ret += X[i - a]

    # La fonction retourne le résultat final converti en chaîne de caractères
    return str(ret)

# Ce bloc vérifie si le script est exécuté comme programme principal, et non importé comme module
if __name__ == "__main__":
    # La fonction open(0) ouvre le flux d'entrée standard (stdin)
    # read() lit tout le contenu de l'entrée standard sous forme de chaîne de caractères
    # splitlines() divise cette chaîne en une liste où chaque ligne de texte devient un élément de la liste
    # L'opérateur * décompose cette liste pour passer chaque élément en argument séparé à la fonction solve
    # On envoie le résultat de solve à la fonction print pour l'afficher à l'écran
    print(solve(*(open(0).read().splitlines())))