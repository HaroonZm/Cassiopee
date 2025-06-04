def is_odd_product(a: int, b: int) -> bool:
    """
    Détermine si le produit de deux entiers est impair.

    Arguments:
        a (int): Premier entier.
        b (int): Deuxième entier.

    Retourne:
        bool: True si le produit a * b est impair, False sinon.
    """
    # Calculer le produit de a et b, puis vérifier si le résultat est impair
    return (a * b) % 2 != 0

def main():
    """
    Point d'entrée principal du programme.
    Lit deux entiers depuis l'entrée standard, vérifie si leur produit est impair,
    et affiche "Yes" si c'est le cas, "No" sinon.
    """
    # Lire une ligne de l'entrée utilisateur et extraire deux entiers
    a, b = map(int, input("Entrez deux entiers séparés par un espace : ").split())

    # Vérifier si le produit est impair et afficher le résultat approprié
    if is_odd_product(a, b):
        print("Yes")
    else:
        print("No")

# Exécuter la fonction principale si ce script est lancé directement
if __name__ == "__main__":
    main()