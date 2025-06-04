def count_specific_patterns(n, a):
    """
    Compte le nombre d'opérations nécessaires pour supprimer certains motifs consécutifs dans la liste 'a'.

    Le motif détecté est :
      - Un triplet de valeurs identiques consécutives (a[i-1] == a[i] == a[i+1]), ou
      - Un motif de deux valeurs consécutives égales (a[i] == a[i+1]), ou
      - Un motif de deux valeurs égales en occurance précédente (a[i-1] == a[i])

    La fonction parcourt la liste et incrémente un compteur lorsqu’un de ces motifs est trouvé, 
    en respectant la logique décrite dans le code original.

    Args:
        n (int): Taille de la liste d'entiers à analyser.
        a (list of int): Liste d'entiers à traiter.

    Returns:
        int: Nombre total de motifs trouvés correspondant aux critères ci-dessus.
    """

    counter = 0  # Initialise le compteur de motifs trouvés à zéro
    i = 1       # Commence l'analyse à partir du deuxième élément (indice 1)

    # Parcours la liste jusqu'à l'avant-dernier élément pour éviter les dépassements d'indice
    while i < n - 1:
        # Si l'élément courant est différent du précédent et du suivant, "saute" deux éléments
        if a[i-1] != a[i] and a[i] != a[i+1]:
            i += 2
        # Si trois éléments consécutifs sont identiques, incrémente le compteur et saute deux éléments
        elif a[i-1] == a[i] == a[i+1]:
            counter += 1
            i += 2
        # Si l'élément courant est identique au suivant, saute un élément
        elif a[i] == a[i+1]:
            i += 1
        # Si l'élément courant est identique au précédent (mais différent du suivant), incrémente le compteur et saute un élément
        elif a[i-1] == a[i]:
            i += 1
            counter += 1

    # Si la boucle termine à l'avant-dernier élément, vérifie un dernier motif pour la fin
    if i == n - 1:
        if a[i] == a[i-1]:
            counter += 1

    return counter

def main():
    """
    Fonction principale :
      - Lit la taille de la liste,
      - Lit la liste d'entiers à partir de l'entrée utilisateur,
      - Appelle la fonction de traitement,
      - Affiche le résultat.
    """
    n = int(input())  # Lit la taille de la liste
    a = list(map(int, input().split()))  # Convertit la ligne d'entrée en liste d'entiers
    result = count_specific_patterns(n, a)  # Calcule le nombre de motifs
    print(result)  # Affiche le résultat à l'écran

if __name__ == "__main__":
    main()