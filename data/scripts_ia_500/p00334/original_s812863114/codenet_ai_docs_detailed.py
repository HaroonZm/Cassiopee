def count_duplicate_sets():
    """
    Lit un entier N depuis l'entrée standard, puis lit N lignes chacune contenant plusieurs entiers.
    Pour chaque ligne, les entiers sont triés, convertis en chaîne et stockés dans un ensemble pour éliminer les doublons.
    Enfin, affiche le nombre de doublons détectés, c'est-à-dire la différence entre N et le nombre d'ensembles uniques.
    
    Exemple d'utilisation :
    Entrée :
    3
    1 2 3
    2 1 3
    4 5 6
    
    Sortie :
    1
    (car les deux premières lignes représentent le même ensemble {1,2,3})
    """
    # Lire le nombre de lignes à traiter
    N = int(input())
    # Initialiser un ensemble pour stocker les ensembles uniques sous forme de chaînes triées
    unique_sets = set()
    
    # Pour chaque ligne d'entrée
    for _ in range(N):
        # Lire une ligne, la convertir en une liste d'entiers
        numbers = list(map(int, input().split()))
        # Trier cette liste d'entiers
        numbers.sort()
        # Convertir la liste triée en chaîne pour pouvoir l'ajouter à l'ensemble
        sorted_str = str(numbers)
        # Ajouter la représentation triée à l'ensemble unique
        unique_sets.add(sorted_str)
    
    # Calculer et afficher le nombre de duplicatas
    duplicates = N - len(unique_sets)
    print(duplicates)

# Lancer la fonction principale
count_duplicate_sets()