def is_possible_sequence(N, A, B, C, D):
    """
    Détermine s'il est possible de former une séquence de N entiers telle que :
    - Le premier est A
    - La somme totale des autres entiers autorise des différences dans l'intervalle [C, D]
    - La somme totale de la séquence est comprise entre les bornes B (min et max incluses)

    Plus précisément, le problème revient à vérifier s'il existe une configuration pour laquelle :
        A + (N - 1) * C - (C + D) * i <= B <= A + (N - 1) * D - (C + D) * i
    pour un i entier compris entre 0 et N - 1.

    Args:
        N (int): Nombre d'éléments dans la séquence.
        A (int): Valeur initiale de la séquence.
        B (int): Somme totale cible à atteindre ou borne à respecter.
        C (int): Valeur minimale qu'une différence dans la séquence peut prendre.
        D (int): Valeur maximale qu'une différence dans la séquence peut prendre.

    Returns:
        bool: True si une telle séquence est possible, False sinon.
    """
    E = C + D  # La somme des bornes inférieure et supérieure sur les différences

    # Teste tous les choix possibles de i (de 0 à N-1 inclus)
    for i in range(N):
        # Calcule la borne inférieure possible pour la somme
        lower_bound = A + (N - 1) * C - E * i

        # Calcule la borne supérieure possible pour la somme
        upper_bound = A + (N - 1) * D - E * i

        # Vérifie si B est compris dans l'intervalle [lower_bound, upper_bound]
        if lower_bound <= B <= upper_bound:
            return True  # Une solution valide a été trouvée

    # Si aucune solution n'a été trouvée après toutes les itérations
    return False

if __name__ == "__main__":
    # Lecture des entrées de l'utilisateur sous forme de cinq entiers espacés
    N, A, B, C, D = map(int, input().split())

    # Appelle la fonction de vérification
    if is_possible_sequence(N, A, B, C, D):
        print("YES")
    else:
        print("NO")