# AOJ 0160 Delivery Fee
# Python3 2018.6.18 bal4u

def calculate_delivery_fee(n, orders):
    """
    Calcule les frais de livraison totaux pour une série de commandes.

    Args:
        n (int): Nombre de commandes.
        orders (list of tuples): Liste contenant les informations (x, y, h, w) pour chaque commande.
            - x (int): Position x du point de livraison.
            - y (int): Position y du point de livraison.
            - h (int): Hauteur du colis.
            - w (int): Poids du colis.

    Returns:
        int: Frais de livraison totaux calculés pour toutes les commandes.
    """
    # Table des tarifs de livraison selon la catégorie calculée
    tbl = [600, 800, 1000, 1200, 1400, 1600]

    fee = 0  # Initialisation des frais totaux

    for order in orders:
        x, y, h, w = order
        
        # Somme x + y + h, utilisée pour déterminer la catégorie de distance/volume
        s = x + y + h

        # Ne calculer les frais que si la somme et le poids sont dans les limites autorisées
        if s <= 160 and w <= 25:

            # Initialisation des indices de catégorie pour distance/volume (k1) et poids (k2)
            k1 = k2 = 0

            # Calcul de l'indice k1 basé sur la somme s
            # Si s <= 60, coût minimal (indice 0)
            if s <= 60:
                k1 = 0
            # Sinon, on calcule une catégorie supplémentaire par tranche de 20 après 61
            else:
                k1 = (s - 61) // 20 + 1

            # Calcul de l'indice k2 basé sur le poids w
            # Si poids <= 2 kg, coût minimal (indice 0)
            if w <= 2:
                k2 = 0
            # Sinon, on calcule une catégorie supplémentaire par tranche de 5 kg après 1
            else:
                k2 = (w - 1) // 5 + 1

            # On choisit la catégorie la plus élevée entre le volume/distance et le poids
            if k1 < k2:
                k1 = k2

            # Ajout du tarif correspondant à la catégorie retenue
            fee += tbl[k1]

    return fee

if __name__ == "__main__":
    while True:
        # Lecture du nombre de commandes
        n = int(input())
        # Condition de sortie : n == 0
        if n == 0:
            break

        orders = []
        # Lecture des informations pour chaque commande
        for _ in range(n):
            x, y, h, w = map(int, input().split())
            orders.append((x, y, h, w))

        # Calcul et affichage du montant total des frais
        total_fee = calculate_delivery_fee(n, orders)
        print(total_fee)