# Demande à l'utilisateur de saisir une chaîne de caractères et stocke la valeur saisie dans la variable T.
T = input()

# Demande à l'utilisateur de saisir une deuxième chaîne de caractères et stocke la valeur saisie dans la variable P.
P = input()

# Vérifie si la longueur de la chaîne P est supérieure à celle de la chaîne T.
# Si c'est le cas, il n'est pas possible que P se trouve dans T, donc on ne fait rien (avec la commande 'pass').
if len(P) > len(T):
    pass  # L'instruction 'pass' indique que rien ne se passe dans ce bloc if.
else:
    # Calcule la longueur de la chaîne P et la stocke dans une variable 'p' pour éviter de la recalculer plusieurs fois.
    p = len(P)
    # Crée une liste vide 'ans' qui servira à stocker les indices où la sous-chaîne P commence dans T.
    ans = []
    # Parcourt tous les indices possibles i dans T où une sous-chaîne de longueur égale à P peut commencer.
    # range(len(T) - len(P) + 1) permet de ne pas dépasser la longueur de T lors de l'extraction de sous-chaînes.
    for i in range(len(T)-len(P)+1):
        # Crée une chaîne vide 'tmp' qui va contenir la sous-chaîne extraite de T à chaque itération.
        tmp = ""
        # Parcourt les indices j allant de i jusqu'à i+p (c’est-à-dire une sous-chaîne de la même longueur que P).
        for j in range(i,i+p):
            # Ajoute le caractère T[j] à la chaîne temporaire 'tmp' à chaque itération de la boucle interne.
            tmp += T[j]
        # Après avoir construit la sous-chaîne, compare 'tmp' à la chaîne P. Si elles sont identiques :
        if tmp == P:
            # Ajoute l’indice i à la liste 'ans' car à cet endroit, P apparaît dans T.
            ans.append(i)
    
    # Parcourt tous les éléments de la liste 'ans', qui correspondent aux indices trouvés.
    for i in ans:
        # Affiche chaque indice où la sous-chaîne P apparaît dans T.
        print(i)