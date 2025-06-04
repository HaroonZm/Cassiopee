def compute_max_possible_units(A: int, B: int, C: int) -> int:
    """
    Calcule le nombre maximal d'unités entières d'un produit/service pouvant être achetées,
    en fonction du coût unitaire A, du montant total disponible B, et du nombre maximum d'unités C.

    Args:
        A (int): Coût unitaire de chaque unité.
        B (int): Montant total d'argent disponible.
        C (int): Nombre maximal d'unités pouvant être achetées (limite supérieure).

    Returns:
        int: Le nombre maximal d'unités pouvant être achetées sans dépasser le budget ni la limite maximale.
    """
    # Calcul du coût total pour acheter le nombre maximal permis d'unités (C)
    total_required = A * C

    # Si le budget permet d'acheter la quantité maximale (C), retournez C
    if B >= total_required:
        return C
    else:
        # Sinon, calculez combien d'unités peuvent être achetées avec le budget disponible
        # On utilise l'entier de la division (budget // prix unitaire)
        return B // A

def main():
    """
    Fonction principale pour récupérer les entrées utilisateur, calculer le résultat et l'afficher.
    """
    # Lecture de l'entrée utilisateur : trois entiers séparés par des espaces.
    # Par exemple : 10 500 30
    A, B, C = map(int, input().split())

    # Calcul du résultat en appelant la fonction dédiée
    result = compute_max_possible_units(A, B, C)

    # Affichage du nombre maximum d'unités achetables
    print(result)

if __name__ == "__main__":
    main()