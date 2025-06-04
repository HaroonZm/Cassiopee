def compare_three_numbers():
    """
    Demande à l'utilisateur de saisir trois nombres entiers séparés par des espaces,
    puis vérifie si les trois nombres sont strictement croissants (a < b < c).
    Affiche 'Yes' si c'est le cas, sinon affiche 'No'.
    """

    # Entrée utilisateur : trois nombres sous forme de chaînes, séparés par un espace
    str_a, str_b, str_c = input("Entrez trois entiers séparés par des espaces : ").split()
    
    # Conversion des valeurs saisies en entiers
    a = int(str_a)
    b = int(str_b)
    c = int(str_c)

    # Vérification si les nombres sont dans l'ordre croissant strict
    if a < b < c:
        print("Yes")
    else:
        print("No")

# Appel de la fonction principale
compare_three_numbers()