def check_string_chain():
    """
    Lit une ligne d'entrée de l'utilisateur, divise l'entrée en trois chaînes distinctes,
    puis vérifie si la dernière lettre de la première chaîne (a) est égale à la première lettre
    de la deuxième chaîne (b) ET si la dernière lettre de la deuxième chaîne (b) est égale à 
    la première lettre de la troisième chaîne (c). Affiche 'YES' si les deux conditions sont vraies,
    sinon affiche 'NO'.
    """
    # Lire une ligne de l'utilisateur, diviser la chaîne en trois parties et les stocker sous forme de chaînes
    a, b, c = map(str, input().split())

    # Vérifier si la dernière lettre de 'a' correspond à la première lettre de 'b'
    # ET que la dernière lettre de 'b' correspond à la première lettre de 'c'
    if a[-1] == b[0] and b[-1] == c[0]:
        # Afficher 'YES' si les deux conditions sont remplies
        print('YES')
    else:
        # Sinon, afficher 'NO'
        print('NO')

# Appeler la fonction principale
check_string_chain()