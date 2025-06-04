def check_strictly_increasing():
    """
    Demande à l'utilisateur de saisir trois entiers séparés par des espaces,
    puis vérifie si les entiers forment une séquence strictement croissante (a < b < c).
    
    Affiche 'Yes' si la condition est vérifiée, sinon affiche 'No'.
    """
    # Demande à l'utilisateur de saisir trois entiers séparés par des espaces, puis les convertit en entiers.
    a, b, c = map(int, input("Entrez trois entiers séparés par des espaces : ").split())

    # Vérifie si a est strictement inférieur à b et si b est strictement inférieur à c.
    if a < b < c:
        # Si la condition est respectée, affiche 'Yes'.
        print('Yes')
    else:
        # Sinon, affiche 'No'.
        print('No')

# Appelle la fonction principale pour exécuter la vérification.
check_strictly_increasing()