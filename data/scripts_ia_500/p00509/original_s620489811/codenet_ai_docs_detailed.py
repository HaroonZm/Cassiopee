import sys
from sys import stdin
from itertools import product

# Override the input function to read lines from standard input quickly
input = stdin.readline

def is_prime(n):
    """
    Détermine si un nombre entier n est un nombre premier.

    Args:
        n (int): Le nombre à tester.

    Returns:
        bool: True si n est premier, False sinon.

    Description:
        - Les nombres inférieurs à 2 ne sont pas premiers.
        - 2 est le plus petit nombre premier.
        - Les nombres pairs supérieurs à 2 ne sont pas premiers.
        - Pour les autres, on teste la divisibilité par tous les nombres impairs
          jusqu'à la racine carrée de n (optimisation classique pour tester la primalité).
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Test des diviseurs impairs de 3 à racine carrée de n
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def solve(n, c):
    """
    Trouve un palindrome premier construit à partir de paramètres donnés.

    Args:
        n (int): La longueur de la partie initiale du palindrome (sans le chiffre central c).
        c (int): Le chiffre central du palindrome. Si c est négatif, il n'y a pas de chiffre central.

    Returns:
        int: Un nombre palindrome premier trouvé satisfaisant les critères, ou un nombre "dummy" si
             n est supérieur à 4 car la recherche exhaustive devient trop coûteuse.

    Description:
        - Si c >= 0, on cherche un palindrome de la forme t + str(c) + t[::-1] où t est une chaîne de longueur n.
        - Sinon, le palindrome est simplement t + t[::-1].
        - Pour n > 4, la recherche est trop grande donc on retourne juste un nombre "dummy" grand.
        - Sinon, on génère toutes les combinaisons possibles de chiffres pour t, en excluant ceux avec un '0' en premier
          (pour ne pas commencer par un zéro, ce qui ferait un nombre avec moins de digits).
        - On teste la primalité de chaque palindrome généré.
        - Retourne le premier palindrome premier trouvé, ou "dummy" si aucun n'est trouvé.
    """
    if c >= 0:
        # Nombre de remplacement "dummy" très grand pour éviter calculs longs si n>4.
        dummy = int('9'*n + str(c) + '9'*n)
    else:
        dummy = int('9'*n + '9'*n)

    # Si la taille est trop grande, on renvoie directement le dummy.
    # Source de la méthode : https://www.ioi-jp.org/joi/2005/2006-m1-prob_and_sol/2006-m1-t5-review.html
    if n > 4:
        return dummy

    found = False
    ans = -1

    # Génère toutes les combinaisons de chiffres de longueur n avec chiffres de 0 à 9
    # en commençant par un chiffre non nul (pas de zéros en début de nombre)
    for p in product('9876543210', repeat=n):
        if p[0] == '0':
            continue
        t = ''.join(p)
        # Construction du palindrome selon la valeur de c
        if c >= 0:
            ans = int(t + str(c) + t[::-1])
        else:
            ans = int(t + t[::-1])
        # Vérification que le palindrome est premier
        if is_prime(ans):
            found = True
            break

    if found:
        return ans
    else:
        return dummy

def main(args):
    """
    Fonction principale qui lit les entrées, calcule la solution et affiche le résultat.

    Args:
        args (list): Arguments en ligne de commande (non utilisés ici).

    Comportement:
        - Lit deux entiers n et c à partir de l'entrée standard.
        - Calcule le palindrome premier correspondant à ces paramètres.
        - Affiche le résultat sur la sortie standard.
    """
    n, c = map(int, input().split())
    result = solve(n, c)
    print(result)

if __name__ == '__main__':
    # Exécution du programme principal avec les arguments de la ligne de commande
    main(sys.argv[1:])