def read_input():
    """
    Lit une ligne d'entrée standard, sépare les valeurs par des espaces et les convertit en entiers.
    Retourne une liste de trois entiers.
    """
    return [int(i) for i in input().split()]

def compute_partial_result(a, b, exp):
    """
    Calcule la valeur partielle selon la formule :
    0.5 * [1.0 + ((a^2 + b^2)^exp) / ((a + b)^(2*exp))]
    
    Args:
        a (int): premier entier.
        b (int): deuxième entier.
        exp (int): exposant à utiliser dans le calcul.
        
    Returns:
        float: résultat partiel du calcul.
    """
    numerator = (a ** 2 + b ** 2) ** exp
    denominator = (a + b) ** (2 * exp)
    return 0.5 * (1.0 + numerator / denominator)

def main():
    """
    Fonction principale qui orchestre la lecture des entrées, le calcul des résultats partiels
    puis le calcul et l'affichage du résultat final.
    """
    # Lecture de la première triplet (m, n, x)
    m, n, x = read_input()
    # Lecture de la deuxième triplet (k, l, y)
    k, l, y = read_input()
    # Calcul du premier terme partiel
    partial1 = compute_partial_result(m, n, x)
    # Calcul du second terme partiel
    partial2 = compute_partial_result(k, l, y)
    # Produit des deux termes pour obtenir le résultat final
    result = partial1 * partial2
    # Affichage du résultat
    print(result)

if __name__ == "__main__":
    main()