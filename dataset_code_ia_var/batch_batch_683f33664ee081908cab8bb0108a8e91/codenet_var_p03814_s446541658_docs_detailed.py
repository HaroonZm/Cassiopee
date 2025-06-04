def count_between_first_A_and_last_Z(s: str) -> int:
    """
    Calcule le nombre de caractères entre la première occurrence de 'A' et la dernière occurrence de 'Z' dans la chaîne.
    
    Plus précisément, retourne la distance (en nombre de caractères, bornes incluses) entre la position de la première 'A'
    et la position de la dernière 'Z' de la chaîne. Si 'A' ou 'Z' n'est pas présent, le comportement par défaut est de retourner 1 (comme pour la chaîne "AZ").
    
    Args:
        s (str): La chaîne de caractères à analyser.
        
    Returns:
        int: Le nombre de caractères compris entre la première 'A' et la dernière 'Z', bornes incluses.
    """
    # Recherche de la position de la première occurrence de 'A'
    first_A_index = s.find("A")
    # Recherche de la position de la dernière occurrence de 'Z'
    last_Z_index = s.rfind("Z")
    # Calcul de la distance entre les deux indices, en incluant les bornes
    length = last_Z_index - first_A_index + 1
    return length

# Lecture de l'entrée utilisateur
input_string = input()
# Appel de la fonction et affichage du résultat
print(count_between_first_A_and_last_Z(input_string))