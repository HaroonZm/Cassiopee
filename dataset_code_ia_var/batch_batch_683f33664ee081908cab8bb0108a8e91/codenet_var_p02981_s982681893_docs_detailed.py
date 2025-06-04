def calculate_minimum_cost(n, a, b):
    """
    Calcule le coût minimum entre parcourir un trajet avec un tarif à l'unité (a * n)
    ou prendre un taxi avec un coût fixe (b).

    Args:
        n (int): Le nombre d'unités à parcourir.
        a (int): Le coût par unité.
        b (int): Le coût fixe du taxi.

    Returns:
        int: Le coût minimal pour le trajet.
    """
    # Calcul du coût total si l'on paye le tarif à l'unité
    tarif_unitaire = a * n

    # Le coût du taxi est un coût fixe
    tarif_taxi = b

    # On retourne le coût minimum entre le tarif unitaire et le tarif taxi
    return min(tarif_unitaire, tarif_taxi)

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur et conversion en entiers : n, a, et b
    n, a, b = map(int, input().split())
    
    # Calcul et affichage du coût minimal
    resultat = calculate_minimum_cost(n, a, b)
    print(resultat)