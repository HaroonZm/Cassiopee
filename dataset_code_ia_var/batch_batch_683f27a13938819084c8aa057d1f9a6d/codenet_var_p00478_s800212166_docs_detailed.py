def count_rotations_with_substring():
    """
    Demande à l'utilisateur de saisir une chaîne 'x', puis un entier 'n' représentant le nombre de chaînes à traiter.
    Pour chaque chaîne saisie, vérifie si 'x' apparaît dans l'une de ses rotations.
    Affiche le nombre total de chaînes pour lesquelles 'x' apparaît comme sous-chaîne dans au moins une rotation.
    """
    # Lecture de la chaîne cible 'x'
    x = input("Chaîne cible x : ")
    # Lecture du nombre de chaînes à traiter
    n = int(input("Nombre de chaînes à vérifier n : "))
    # Initialise le compteur de réponses positives
    ans = 0

    # Boucle sur chaque chaîne à traiter
    for i in range(n):
        # Lecture de la chaîne à vérifier et conversion en liste de caractères
        y = list(input(f"Chaîne #{i+1} à vérifier : "))
        # Pour permettre de simuler toutes les rotations, on ajoute les (len(x)-1) premiers caractères à la fin
        for j in range(len(x) - 1):
            y.append(y[j])
        # Conversion de la liste de caractères en chaîne
        y = "".join(y)
        # Vérifie si 'x' apparaît comme sous-chaîne dans la chaîne étendue de 'y'
        if x in y:
            ans += 1
    # Affiche le résultat final
    print(ans)

# Appel de la fonction principale
count_rotations_with_substring()