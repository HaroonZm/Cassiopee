def calculate_combinations(N, M):
    """
    Calcule le nombre total de paires distinctes pouvant être formées dans deux groupes distincts.

    Plus précisément, pour un groupe de N éléments et un groupe de M éléments, cette fonction retourne
    la somme du nombre de façons de choisir deux éléments distincts dans chacun des groupes.

    Args:
        N (int): Nombre d'éléments dans le premier groupe.
        M (int): Nombre d'éléments dans le second groupe.

    Returns:
        int: Le total des combinaisons possibles de deux dans chaque groupe (N C 2 + M C 2).
    """
    # Calcul du nombre de combinaisons dans le premier groupe (N C 2)
    combos_first_group = N * (N - 1) // 2

    # Calcul du nombre de combinaisons dans le deuxième groupe (M C 2)
    combos_second_group = M * (M - 1) // 2

    # Retourne la somme des deux
    return combos_first_group + combos_second_group

def main():
    """
    Fonction principale qui demande à l'utilisateur de saisir deux entiers séparés par des espaces,
    puis affiche la somme des combinaisons de deux éléments pour chaque groupe.
    """
    # Lecture des entrées utilisateur et conversion en entiers
    N, M = map(int, input().split())

    # Calcul du résultat à l'aide de la fonction 'calculate_combinations'
    ans = calculate_combinations(N, M)

    # Affichage du résultat final
    print(ans)

if __name__ == '__main__':
    main()