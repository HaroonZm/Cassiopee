def is_first_last_same(N: str) -> str:
    """
    Vérifie si le premier et le dernier caractère de la chaîne 'N' sont identiques.
    
    Args:
        N (str): Chaîne de caractères à analyser (supposée non vide).
    
    Returns:
        str: "Yes" si le premier et le dernier caractère sont identiques, "No" sinon.
    """
    # Récupère le premier caractère
    first_char = N[0]
    # Récupère le dernier caractère
    last_char = N[-1]
    # Compare les deux et retourne "Yes" si identiques, "No" sinon
    if first_char == last_char:
        return "Yes"
    else:
        return "No"

# Lecture de l'entrée utilisateur
N = input()
# Appel de la fonction et affichage du résultat
print(is_first_last_same(N))