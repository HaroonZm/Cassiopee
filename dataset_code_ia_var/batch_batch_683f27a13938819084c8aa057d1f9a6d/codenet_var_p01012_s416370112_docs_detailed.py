def parse_input_line():
    """
    Lit une ligne de l'entrée standard, sépare les valeurs par les espaces, convertit chacune en un entier
    et les retourne sous forme de liste de trois éléments.

    Returns:
        list: Une liste contenant trois entiers parsés depuis l'entrée utilisateur.
    """
    return [int(i) for i in input().split()]

def compute_expression(a, b, exp):
    """
    Calcule l'expression mathématique suivante :
        0.5 * (1.0 + ((a^2 + b^2)^exp) / ((a + b)^(2 * exp)))

    Args:
        a (int): Premier entier de l'expression.
        b (int): Deuxième entier de l'expression.
        exp (int): Exposant à appliquer dans le calcul.

    Returns:
        float: Le résultat du calcul de l'expression.
    """
    numerator = (a**2 + b**2) ** exp         # Calcule le numérateur : (a^2 + b^2)^exp
    denominator = (a + b) ** (2 * exp)       # Calcule le dénominateur : (a + b)^(2*exp)
    result = 0.5 * (1.0 + numerator / denominator)  # Applique la formule globale
    return result

def main():
    """
    Fonction principale qui récupère deux lignes d'entrée utilisateur, extrait les valeurs,
    calcule les résultats selon la formule définie, multiplie les deux résultats,
    puis affiche la valeur finale.
    """
    # Lecture et extraction des trois entiers de la première ligne d'entrée
    m, n, x = parse_input_line()
    # Lecture et extraction des trois entiers de la deuxième ligne d'entrée
    k, l, y = parse_input_line()
    
    # Calcul du premier résultat selon la formule
    res1 = compute_expression(m, n, x)
    # Calcul du deuxième résultat selon la même formule
    res2 = compute_expression(k, l, y)
    
    # Produit des deux résultats pour obtenir la valeur finale
    res = res1 * res2
    
    # Affichage du résultat final
    print(res)

# Appel de la fonction principale pour exécuter le script
if __name__ == "__main__":
    main()