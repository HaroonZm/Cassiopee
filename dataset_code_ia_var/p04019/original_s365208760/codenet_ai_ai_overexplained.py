# Demande à l'utilisateur d'entrer une chaîne de caractères via le clavier.
# La fonction input() lit cette entrée et retourne la chaîne.
# list() convertit la chaîne de caractères en une liste où chaque caractère devient un élément séparé de la liste.
S = list(input())

# Initialise une variable appelée check à la valeur 0.
# Cette variable va servir de drapeau (flag) pour indiquer si certaines conditions sont remplies ou non.
# Si sa valeur reste 0, cela signifiera que tout est correct.
# Si sa valeur passe à 1, cela signifiera qu'une condition attendue n'est pas respectée.
check = 0

# Vérifie si la chaîne contient la lettre 'E'.
if 'E' in S:
    # Si c'est le cas, vérifie alors si la lettre 'W' est également présente.
    if 'W' in S:
        # Si 'W' est présente, ne rien faire.
        pass
    else:
        # Sinon, cela signifie qu'il manque la lettre 'W' alors qu'il y a 'E'.
        # Dans ce cas, on met check à 1 pour indiquer qu'une condition n'est pas remplie.
        check = 1

# Vérifie si la chaîne contient la lettre 'W'.
if 'W' in S:
    # Si c'est le cas, vérifie si 'E' est également présente.
    if 'E' in S:
        # Si 'E' est présente, ne rien faire.
        pass
    else:
        # Sinon, on met check à 1 car il manque 'E' alors qu'il y a 'W'.
        check = 1

# Vérifie si la chaîne contient la lettre 'N'.
if 'N' in S:
    # Si c'est le cas, vérifie si 'S' est également présente.
    if 'S' in S:
        # Si 'S' est présente, ne rien faire.
        pass
    else:
        # Sinon, il manque 'S' alors qu'il y a 'N'.
        check = 1

# Vérifie si la chaîne contient la lettre 'S'.
if 'S' in S:
    # Si c'est le cas, vérifie si 'N' est également présente.
    if 'N' in S:
        # Si 'N' est présente, ne rien faire.
        pass
    else:
        # Sinon, il manque 'N' alors qu'il y a 'S'.
        check = 1

# À la fin, vérifie si le drapeau check est resté à 0.
if check == 0:
    # Si check est égal à 0, cela veut dire que toutes les paires de directions sont correctement présentes ou absentes.
    print('Yes')  # Affiche "Yes" pour indiquer que toutes les conditions sont respectées.
else:
    # Si check a été mis à 1 au moins une fois, cela veut dire qu'une condition n'est pas respectée.
    print('No')   # Affiche "No" pour indiquer que toutes les conditions ne sont pas respectées.