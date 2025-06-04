def longest_substring_A_to_Z(s):
    """
    Calcule la longueur du plus long sous-ensemble de la chaîne 's' qui commence par le premier 'A' 
    et se termine par le dernier 'Z', incluant toutes les lettres entre les deux, extrêmes inclus.
    
    Paramètres:
        s (str): La chaîne de caractères à analyser.
    
    Retourne:
        int: La longueur du sous-ensemble compris entre le premier 'A' et le dernier 'Z', 
             ou 0 si l'un des caractères n'est pas trouvé.
    """
    # Détermination de la longueur de la chaîne
    l = len(s)
    # Liste pour stocker les indices où la lettre 'A' apparaît dans la chaîne
    a = []
    # Liste pour stocker les indices où la lettre 'Z' apparaît dans la chaîne
    z = []
    
    # Parcourt chaque caractère de la chaîne à l'aide de son indice
    for i in range(l):
        # Si la lettre courante est 'A', on ajoute son indice à la liste 'a'
        if s[i] == "A":
            a.append(i)
        # Si la lettre courante est 'Z', on ajoute son indice à la liste 'z'
        elif s[i] == "Z":
            z.append(i)
    
    # Si au moins une occurrence de 'A' et de 'Z' ont été trouvées,
    # on calcule la longueur du sous-ensemble demandé
    if a and z:
        ans = (max(z) - min(a) + 1)
    else:
        # Aucun 'A' ou 'Z' trouvé, donc la longueur est 0
        ans = 0
    
    return ans

# Lecture de la chaîne de caractères entrée par l'utilisateur
user_input = input()
# Appel de la fonction avec la chaîne saisie
result = longest_substring_A_to_Z(user_input)
# Affichage du résultat
print(result)