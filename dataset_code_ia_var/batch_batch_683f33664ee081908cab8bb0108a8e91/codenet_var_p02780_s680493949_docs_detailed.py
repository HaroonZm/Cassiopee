def max_expected_value_subarray(n, k, p):
    """
    Calcule la valeur d'espérance maximale parmi toutes les sous-listes de longueur k de la liste p,
    en supposant que chaque élément p_i représente la valeur maximale possible lors du lancer d'un dé
    à p_i faces, donc l'espérance pour ce dé est (p_i + 1)/2. La somme maximale trouvée est convertie
    en valeur d'espérance globale.

    Args:
        n (int): Taille de la liste p.
        k (int): Longueur des sous-listes considérées.
        p (list of int): Liste des valeurs maximales possibles pour chaque élément.

    Returns:
        float: La valeur d'espérance maximale calculée parmi toutes les sous-listes de taille k.
    """

    # Initialisation pour la somme de la première fenêtre de longueur k
    before_pi = p[0]  # Premier élément de la fenêtre courante
    before_sum = sum(p[0:k]) + 0.0  # Somme initiale de la première sous-liste de longueur k, conversion explicite en float
    suml = [sum(p[0:k])]  # Liste pour stocker la somme de chaque sous-liste de taille k

    # Parcourt toutes les sous-listes consécutives de taille k en mettant à jour efficacement la somme
    for i in range(1, n - k + 1):
        # Met à jour la somme courante en retirant l'élément sortant et en ajoutant le nouvel élément entrant dans la fenêtre
        before_sum = before_sum - before_pi + p[i + k - 1]
        suml.append(before_sum)  # Ajoute la somme de la fenêtre courante à la liste
        before_pi = p[i]         # Met à jour l'élément sortant pour la prochaine itération

    # Calcule l'espérance maximale : (somme maximale des sous-listes + k) / 2.0
    # (Chaque élément p_i correspond à une valeur d'attente de (p_i + 1)/2, donc la formule globale s'applique)
    return (max(suml) + k) / 2.0


def main():
    """
    Fonction principale pour lire les entrées utilisateur, calculer l'espérance maximale et afficher le résultat.
    """
    # Lecture de deux entiers n et k à partir de l'entrée standard, séparés par un espace
    n, k = map(int, input().split())

    # Lecture de la liste entière p à partir de l'entrée standard
    p = list(map(int, input().split()))

    # Calcul de l'espérance maximale via l'appel de la fonction dédiée
    result = max_expected_value_subarray(n, k, p)

    # Affichage du résultat calculé
    print(result)


# Si ce fichier est exécuté en tant que script principal, lance la fonction main()
if __name__ == "__main__":
    main()