def main():
    """
    Lit trois entiers de l'entrée standard :
    - n : le nombre d'éléments ou la quantité désirée.
    - a : le coût unitaire ou une valeur associée à chaque élément.
    - b : une valeur limite ou un plafond maximal.
    Affiche le minimum entre le coût total pour n éléments (a * n) et la limite b.
    """
    # Lecture de trois entiers séparés par des espaces depuis l'entrée standard
    n, a, b = map(int, input().split())

    # Calcul du coût total : coût unitaire multiplié par la quantité
    total_cost = a * n

    # Détermination de la valeur minimale entre le coût total et la limite imposée
    result = min(b, total_cost)

    # Affiche la valeur minimale calculée
    print(result)

if __name__ == "__main__":
    main()