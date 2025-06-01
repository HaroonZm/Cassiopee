def calculate_discounted_price(x, y, b, p):
    """
    Calcule le prix total avec application possible d'une remise selon les quantités.

    Args:
        x (int): Prix unitaire de l'article b.
        y (int): Prix unitaire de l'article p.
        b (int): Quantité achetée de l'article b.
        p (int): Quantité achetée de l'article p.

    Returns:
        int: Prix total après application de la remise éventuelle, arrondi à l'entier inférieur.
    """
    # Cas où la quantité de b est inférieure à 5 et la quantité de p est inférieure à 2
    if b < 5 and p < 2:
        # Calcule le prix normal et le prix avec remise sur quantités minimales (5 pour b et 2 pour p)
        prix_normal = x * b + y * p
        prix_remise = (x * 5 + y * 2) * 0.8
        ans = min(prix_normal, prix_remise)

    # Cas où la quantité de b est au moins 5 et p est inférieur à 2
    elif b >= 5 and p < 2:
        # Calcule le prix normal et le prix avec remise sur p minimale
        prix_normal = x * b + y * p
        prix_remise = (x * b + y * 2) * 0.8
        ans = min(prix_normal, prix_remise)

    # Cas où la quantité de b est inférieure à 5 et p est au moins 2
    elif b < 5 and p >= 2:
        # Calcule le prix normal et le prix avec remise sur b minimale
        prix_normal = x * b + y * p
        prix_remise = (x * 5 + y * p) * 0.8
        ans = min(prix_normal, prix_remise)

    # Cas où les quantités de b et p sont respectivement au moins 5 et 2
    else:
        # Applique directement la remise sur le prix total
        ans = (x * b + y * p) * 0.8

    # Retourne le prix arrondi à l'entier inférieur
    return int(ans)


def main():
    """
    Fonction principale qui lit le nombre de cas, puis pour chaque cas,
    lit les données d'entrée, calcule et affiche le prix après remise.
    """
    # Lecture du nombre de cas à traiter
    n = int(input())

    # Traitement de chaque cas
    for _ in range(n):
        # Lecture des prix unitaires et quantités pour b et p
        x, y, b, p = map(int, input().split())
        # Calcul du prix final avec remise
        ans = calculate_discounted_price(x, y, b, p)
        # Affichage du résultat
        print(ans)


# Exécution de la fonction principale
if __name__ == "__main__":
    main()