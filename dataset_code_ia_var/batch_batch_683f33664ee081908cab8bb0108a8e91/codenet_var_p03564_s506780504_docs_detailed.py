def compute_final_value(n, k):
    """
    Calcule la valeur finale en appliquant, sur n étapes, l'une des deux opérations à chaque étape :
    - Si la valeur courante (ans) est strictement inférieure à k, elle est multipliée par 2.
    - Sinon, k lui est ajouté.

    Args:
        n (int): Le nombre d'étapes à effectuer.
        k (int): Le seuil et l'incrément pour l'opération d'addition.

    Returns:
        int: La valeur résultante après n étapes.
    """
    ans = 1  # Initialisation de la variable résultat à 1
    # Boucle exécutée n fois
    for _ in range(n):
        # Si la valeur actuelle est inférieure à k, on la double
        if ans < k:
            ans *= 2
        # Sinon, on ajoute k à la valeur actuelle
        else:
            ans += k
    return ans

if __name__ == "__main__":
    # Lecture de n et k en entrée utilisateur
    n = int(input())
    k = int(input())
    # Calcul et affichage du résultat final selon l'algorithme défini
    result = compute_final_value(n, k)
    print(result)