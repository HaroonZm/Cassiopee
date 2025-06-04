def calculate_min_value(A: int, B: int, C: int) -> int:
    """
    Calcule le minimum entre C et la partie entière de la division de B par A.

    Arguments:
        A (int): Le premier entier, utilisé comme diviseur.
        B (int): Le deuxième entier, utilisé comme dividende.
        C (int): Le troisième entier, valeur à comparer.

    Retourne:
        int: Le minimum entre C et la partie entière de B divisée par A.
    """
    # Effectuer la division entière de B par A et convertir le résultat en entier
    division_result = int(B / A)
    # Comparer le résultat de la division avec C et retourner la plus petite valeur
    return min(division_result, C)

def main():
    """
    Fonction principale du script.
    Lit trois entiers depuis l'entrée standard,
    calcule la valeur minimale selon la logique spécifiée,
    puis affiche le résultat.
    """
    # Lire l'entrée utilisateur sous forme d'une chaîne, séparer les valeurs et les convertir en entiers
    A, B, C = map(int, input().split())
    # Appeler la fonction de calcul avec les valeurs saisies
    result = calculate_min_value(A, B, C)
    # Afficher le résultat calculé
    print(result)

# Exécuter la fonction principale si ce script est lancé directement
if __name__ == "__main__":
    main()