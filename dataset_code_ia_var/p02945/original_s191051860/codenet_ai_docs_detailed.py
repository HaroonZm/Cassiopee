def main():
    """
    Fonction principale qui lit deux entiers depuis l'entrée standard,
    calcule leur somme, différence et produit, puis affiche la valeur maximale parmi ces trois résultats.
    """
    # Lecture d'une ligne depuis l'entrée utilisateur, découpage en tokens, conversion en entiers
    a, b = [int(n) for n in input("Entrez deux entiers séparés par un espace : ").split()]
    
    # Calcul de la somme des deux entiers
    sum_res = a + b
    # Calcul de la différence entre le premier et le second entier
    diff_res = a - b
    # Calcul du produit des deux entiers
    prod_res = a * b
    
    # Création d'une liste contenant les trois résultats calculés
    results = [sum_res, diff_res, prod_res]
    
    # Recherche de la valeur maximale parmi les trois résultats
    max_result = max(results)
    
    # Affichage du résultat maximal
    print(max_result)

if __name__ == "__main__":
    main()