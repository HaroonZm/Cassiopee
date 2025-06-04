def is_two_pairs(s):
    """
    Détermine si la chaîne d'entrée contient exactement deux paires de caractères différents.

    Args:
        s (str): Une chaîne de 4 caractères.

    Returns:
        str: "Yes" si la chaîne contient deux paires de caractères différents (par exemple AABB), sinon "No".
    """
    # Convertir la chaîne en liste de caractères pour permettre le tri
    chars = list(s)
    # Trier la liste pour regrouper les caractères identiques
    chars.sort()

    # Après le tri, la chaîne doit être de la forme XXYY où X != Y
    # Cela signifie : 
    # - les deux premiers caractères sont identiques
    # - les deux derniers caractères sont identiques
    # - le caractère du milieu n'est pas le même que le premier
    if chars[0] == chars[1] and chars[2] == chars[3] and chars[1] != chars[2]:
        return "Yes"
    else:
        return "No"

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, appelle la fonction de vérification 
    puis affiche le résultat.
    """
    # Lire la chaîne entrée par l'utilisateur
    s = input()
    # Vérifier la condition et afficher "Yes" ou "No"
    result = is_two_pairs(s)
    print(result)

# Appel du point d'entrée principal du programme
if __name__ == "__main__":
    main()