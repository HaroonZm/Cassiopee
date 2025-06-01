def process(x, y, h, w):
    """
    Calcule un score basé sur la somme des dimensions x, y, h et la largeur w.

    La fonction applique une série de conditions sur la somme x + y + h et la valeur w
    pour déterminer un score correspondant. Si aucune condition n'est remplie, le score renvoyé est 0.

    Paramètres:
    x (int): première dimension
    y (int): deuxième dimension
    h (int): troisième dimension
    w (int): largeur

    Retour:
    int: score calculé en fonction des conditions définies
    """
    # Calcule la somme des dimensions x, y et h
    dimension_sum = x + y + h

    # Vérifie chaque condition dans l'ordre et renvoie la valeur associée si elle est vraie
    if dimension_sum <= 60 and w <= 2:
        return 600
    elif dimension_sum <= 80 and w <= 5:
        return 800
    elif dimension_sum <= 100 and w <= 10:
        return 1000
    elif dimension_sum <= 120 and w <= 15:
        return 1200
    elif dimension_sum <= 140 and w <= 20:
        return 1400
    elif dimension_sum <= 160 and w <= 25:
        return 1600
    else:
        # Aucun critère n'a été rempli, renvoie 0
        return 0

def main():
    """
    Lit plusieurs ensembles de données depuis l'entrée standard, calcule la somme des scores
    pour chaque ensemble en utilisant la fonction process, et affiche les résultats.

    La lecture s'arrête dès qu'un entier 0 est rencontré indiquant la fin des données.

    Pour chaque ensemble:
    - Lit un entier n indiquant le nombre de lignes suivantes.
    - Pour chaque ligne, lit quatre entiers x, y, h, w.
    - Calcule les scores avec process et accumule la somme.
    - Ajoute la somme au résultat final.

    Affiche enfin les sommes de chaque ensemble, une par ligne.
    """
    result = []

    while True:
        # Lit le nombre d'éléments à traiter dans cet ensemble
        n = int(input())
        if n == 0:
            # Condition d'arrêt de la boucle de lecture
            break

        total = 0
        for _ in range(n):
            # Lit les quatre valeurs x, y, h, w séparées par des espaces
            x, y, h, w = map(int, input().split())
            # Calcule le score correspondant et l'ajoute au total
            total += process(x, y, h, w)

        # Stocke le total calculé pour cet ensemble dans la liste des résultats
        result.append(total)

    # Affiche tous les résultats, chaque total sur une ligne séparée
    print('\n'.join(map(str, result)))

# Point d'entrée principal du script
if __name__ == "__main__":
    main()