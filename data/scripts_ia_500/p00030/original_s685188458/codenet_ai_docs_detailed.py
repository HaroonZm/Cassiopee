import itertools

def count_combinations_with_sum(n, s):
    """
    Compte le nombre de combinaisons uniques de n chiffres distincts (0 à 9) 
    dont la somme des éléments est égale à s.

    Parameters:
    n (int): Le nombre d'éléments dans chaque combinaison.
    s (int): La somme ciblée des éléments de la combinaison.

    Returns:
    int: Le nombre total de combinaisons où la somme des éléments vaut s.
    """
    count = 0
    # Génère toutes les combinaisons distinctes de longueur n parmi les chiffres 0 à 9
    for combination in itertools.combinations(range(10), n):
        # Vérifie si la somme des éléments de la combinaison correspond à s
        if sum(combination) == s:
            count += 1
    return count

def main():
    """
    Fonction principale qui lit des paires de valeurs n et s depuis l'entrée standard,
    calcule et affiche le nombre de combinaisons de n chiffres uniques dont la somme est s.
    Le processus continue jusqu'à ce que la paire (0,0) soit saisie, ce qui arrête la boucle.
    """
    while True:
        # Lit une ligne, la décompose en deux entiers n et s
        n, s = map(int, input().split())
        # Condition d'arrêt lorsque n et s sont tous deux nuls
        if n == 0 and s == 0:
            break
        # Calcule le nombre de combinaisons satisfaisant la condition
        result = count_combinations_with_sum(n, s)
        # Affiche le résultat pour la paire n, s lue
        print(result)

if __name__ == "__main__":
    main()