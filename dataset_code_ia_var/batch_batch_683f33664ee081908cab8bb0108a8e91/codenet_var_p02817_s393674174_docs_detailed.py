def swap_and_concatenate():
    """
    Demande à l'utilisateur de saisir une chaîne de caractères,
    sépare cette chaîne en utilisant les espaces comme séparateurs,
    puis affiche la concaténation du deuxième élément et du premier élément de la liste résultante.
    """
    # Demander à l'utilisateur de saisir une chaîne de caractères
    a = input("Veuillez saisir des mots séparés par des espaces : ")

    # Séparer la chaîne saisie en une liste de mots, découpés sur les espaces
    aa = a.split()

    # Concaténer le deuxième élément (indice 1) et le premier élément (indice 0) de la liste
    # Supposer que l'utilisateur saisit au moins deux mots, sinon cela lèvera une exception
    result = aa[1] + aa[0]

    # Afficher le résultat obtenu
    print(result)

# Appel de la fonction principale
swap_and_concatenate()