def max_fuel_after_stations():
    """
    Calcule la quantité maximale de carburant disponible après avoir traversé une série de stations.

    Le programme lit en entrée :
    - n (int) : le nombre de stations.
    - m (int) : la quantité initiale de carburant.
    Ensuite, pour chaque station, il lit deux entiers a et b représentant respectivement
    le carburant gagné et le carburant utilisé à cette station.

    Il calcule la quantité de carburant restant après chaque station en tenant compte des gains et des pertes.
    Si la quantité de carburant devient négative, on considère que le voyage ne peut pas continuer à partir de cette station.
    L'objectif est de trouver la quantité maximale de carburant jamais atteinte au cours du trajet,
    ou 0 si la quantité est négative après une station.

    Affiche la quantité maximale de carburant atteinte.

    Exemple d'entrée :
    3
    10
    2 3
    4 5
    3 4

    Exemple de sortie :
    11
    """
    # Lecture du nombre de stations
    n = int(input())
    # Lecture de la quantité initiale de carburant
    m = int(input())

    # ans stocke la quantité maximale de carburant observée jusqu'à présent
    # c est la quantité courante de carburant qui évolue à chaque station
    ans = c = m

    # Parcours de chaque station
    for _ in range(n):
        # Lecture des gains et pertes de carburant à la station courante
        a, b = map(int, input().split())

        # Si le carburant courant est négatif, on ne peut plus continuer, on ignore cette station
        if c < 0:
            continue

        # Mise à jour du carburant courant après avoir gagné a et perdu b
        c += a - b

        # Mise à jour du maximum de carburant si la valeur courante est supérieure
        if ans < c:
            ans = c

        # Si le carburant devient négatif, on les remplacer par 0 dans ans car le voyage est interrompu
        if c < 0:
            ans = 0

    # Affichage du maximum de carburant atteint
    print(ans)