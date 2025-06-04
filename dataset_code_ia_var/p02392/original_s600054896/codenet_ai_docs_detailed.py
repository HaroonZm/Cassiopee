def check_strictly_increasing():
    """
    Demande trois entiers à l'utilisateur, séparés par des espaces,
    puis vérifie si ces entiers sont strictement croissants (a < b < c).
    Affiche "Yes" si la condition est vraie, sinon affiche "No".
    """
    # Lecture de la saisie utilisateur sous forme de chaîne de caractères
    # La méthode input() lit une ligne depuis l'entrée standard.
    # La méthode split() sépare la chaîne en une liste selon les espaces.
    # La fonction map(int, ...) convertit chaque élément de la liste en entier.
    # Enfin, list(...) crée une liste d'entiers à partir de l'objet map.
    a, b, c = list(map(int, input("Entrez trois entiers séparés par des espaces : ").split()))
    
    # Vérification si les trois valeurs sont strictement croissantes
    # L'expression a < b < c retourne True seulement si a < b et b < c.
    if a < b < c:
        # Si la condition est remplie, afficher "Yes"
        print("Yes")
    else:
        # Sinon, afficher "No"
        print("No")

# Exécution de la fonction principale
check_strictly_increasing()