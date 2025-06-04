import sys  # Importe le module sys, qui fournit des fonctions et des objets utilisés pour interagir avec l'interpréteur Python.
from sys import stdin  # Importe stdin, qui représente l'entrée standard (généralement le clavier ou un fichier redirigé).
input = stdin.readline  # Redéfinit la fonction input pour qu'elle lise une ligne depuis l'entrée standard plus efficacement.

def main(args):  # Définit une fonction nommée main qui prend un argument appelé args (généralement la liste des arguments de la ligne de commande, mais elle n'est pas utilisée ici).
    # Crée une liste appelée pastas. Cette liste comprendra trois entiers.
    # On utilise une compréhension de liste pour lire trois lignes de l'entrée standard.
    # Pour chaque itération (il y en a 3, car range(3) produit 0, 1, 2), on lit une ligne avec input(), 
    # puis on convertit cette ligne lue (une chaîne de caractères qui inclut\n) en entier avec int().
    pastas = [int(input()) for _ in range(3)]
    
    # Même chose pour les boissons (drinks). On crée une liste qui contiendra deux entiers.
    # On effectue deux itérations (car range(2) produit 0, 1),
    # à chaque fois on lit une ligne et on la convertit en entier.
    drinks = [int(input()) for _ in range(2)]

    # On utilise la fonction min() pour trouver l'élément le moins cher (le plus petit entier) dans la liste pastas.
    # On fait de même pour drinks, c'est-à-dire le moins cher dans la liste des boissons.
    # On additionne les deux minima (le moins cher des pâtes et le moins cher des boissons).
    # Ensuite, on soustrait 50 au résultat (cela représente une réduction automatique de 50 unités de la monnaie locale).
    total = min(pastas) + min(drinks) - 50

    # Affiche le total calculé à l'écran. print() convertit l'entier en chaîne de caractères et l'affiche.
    print(total)

# Ceci est un idiome standard en Python pour ne pas exécuter une section de code si le fichier est importé comme un module.
# Le code dans cette condition ne s'exécutera que si le fichier est exécuté comme le programme principal.
if __name__ == '__main__':
    # Appelle la fonction main, en passant la liste des arguments de la ligne de commande,
    # à l'exception du premier élément sys.argv[0] (qui est le nom du script).
    main(sys.argv[1:])