def process_bus_stops():
    """
    Lit le nombre d'arrêts de bus 'n', la capacité initiale de personnes 'm',
    puis pour chaque arrêt, lit le nombre de personnes qui sortent 'a' et celles qui entrent 'b'.
    Calcule et affiche la capacité maximale atteinte pendant le trajet si le bus n'a jamais de capacité négative,
    ou affiche '0' dès que la capacité devient négative.
    """
    # Lecture du nombre d'arrêts
    n = int(input())
    # Lecture de la capacité initiale (nombre de personnes dans le bus au début)
    m = int(input())
    # Initialisation de la capacité maximale atteinte par le bus
    S_max = m

    # Traitement de chaque arrêt de bus
    for i in range(n):
        # Lecture du nombre de personnes qui descendent (a) et montent (b) à cet arrêt
        a, b = map(int, input().split())
        # Mise à jour du nombre de personnes dans le bus après cet arrêt
        m += a - b
        # Vérification si le nombre de personnes devient négatif (plus de personnes descendent que présentes)
        if m < 0:
            print(0)
            break  # Arrêt de l'exécution car situation impossible
        # Mise à jour de la capacité maximale si nécessaire
        S_max = max(S_max, m)
    else:
        # Si la boucle n'a pas rencontré de capacité négative, afficher la capacité maximale atteinte
        print(S_max)

# Appel de la fonction principale
process_bus_stops()