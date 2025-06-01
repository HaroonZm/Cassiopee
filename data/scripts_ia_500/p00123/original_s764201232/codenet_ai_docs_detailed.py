import sys

# Liste des catégories de notation correspondant à des indices de gravité.
R = ["AAA", "AA", "A", "B", "C", "D", "E", "NA"]

def categorize_temperature(value):
    """
    Catégorise une valeur de température en fonction de plages définies.
    
    Args:
        value (float): La température à catégoriser.
    
    Returns:
        int: L'indice de catégorie correspondant dans la liste R.
             Les indices vont de 0 (meilleur) à 7 (pire).
    """
    if value < 35.5:
        return 0
    elif value < 37.5:
        return 1
    elif value < 40:
        return 2
    elif value < 43:
        return 3
    elif value < 50:
        return 4
    elif value < 55:
        return 5
    elif value < 70:
        return 6
    else:
        return 7

def categorize_pressure(value):
    """
    Catégorise une valeur de pression en fonction de plages définies.
    
    Args:
        value (float): La pression à catégoriser.
    
    Returns:
        int: L'indice de catégorie correspondant dans la liste R.
             Les indices vont de 0 (meilleur) à 7 (pire).
    """
    if value < 71:
        return 0
    elif value < 77:
        return 1
    elif value < 83:
        return 2
    elif value < 89:
        return 3
    elif value < 105:
        return 4
    elif value < 116:
        return 5
    elif value < 148:
        return 6
    else:
        return 7

def main():
    """
    Lit les entrées standard ligne par ligne, each contenant deux nombres flottants séparés par un espace,
    représentant respectivement une température et une pression. Pour chaque paire, 
    détermine la catégorie la plus sévère entre température et pression, puis imprime la 
    catégorie correspondante de la liste R.
    """
    for line in sys.stdin:
        # Suppression des espaces en début et fin de ligne, puis séparation.
        parts = line.strip().split()
        if len(parts) != 2:
            # Ignore la ligne si elle ne contient pas exactement deux valeurs
            continue
        try:
            t1, t2 = map(float, parts)
        except ValueError:
            # Ignore la ligne si les valeurs ne sont pas des flottants valides
            continue

        # Déterminer les indices de catégorie pour la température et la pression
        t5 = categorize_temperature(t1)
        t10 = categorize_pressure(t2)

        # Sélectionner la catégorie la plus sévère (indice maximum)
        t = max(t5, t10)

        # Afficher la notation associée
        print(R[t])

if __name__ == "__main__":
    main()