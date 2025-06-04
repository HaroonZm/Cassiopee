import math

MOD = 10 ** 9 + 7  # Constante pour la division modulaire (un grand nombre premier utilisé pour éviter les débordements)

def compute_pattern_count(n, m):
    """
    Calcule le nombre de configurations possibles selon les valeurs de n et m.
    Le résultat est ajusté selon les contraintes suivantes :
    - Si la différence absolue entre n et m est supérieure ou égale à 2, il n'y a aucune configuration valide.
    - Sinon, le nombre de configurations est le produit des factorielles de n et m.
    - Si n et m sont égaux, le résultat est doublé.

    Args:
        n (int): Premier entier (par exemple, nombre de types A)
        m (int): Deuxième entier (par exemple, nombre de types B)

    Returns:
        int: Nombre total de configurations possibles, modulo MOD.
    """
    if abs(n - m) >= 2:
        # Aucune configuration possible si la différence dépasse 1
        return 0
    result = math.factorial(n) * math.factorial(m)
    if n == m:
        # Doubler le résultat si n et m sont identiques
        result *= 2
    return result % MOD

def main():
    """
    Fonction principale :
    - Récupère deux entiers en entrée standard
    - Calcule et affiche le nombre de configurations valides modulo MOD
    """
    # Lecture de la saisie utilisateur et conversion en deux entiers
    n, m = map(int, input().split())
    # Calcul du nombre de configurations possibles
    pattern_count = compute_pattern_count(n, m)
    # Affichage du résultat
    print(pattern_count)

# Appel de la fonction principale pour exécuter le programme
if __name__ == "__main__":
    main()