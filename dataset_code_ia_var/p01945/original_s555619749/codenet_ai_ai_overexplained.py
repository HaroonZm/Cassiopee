# Demande à l'utilisateur de saisir une chaîne de caractères via la console.
# La chaîne saisie est transformée en liste où chaque caractère devient un élément séparé de la liste.
S = list(input())

# Calcule la longueur de la liste S (c'est-à-dire le nombre total de caractères dans la chaîne saisie).
S_l = len(S)

# Initialise la variable n à 0. Cette variable sera utilisée comme compteur ou index lors des boucles.
n = 0

# Initialise deux listes vides l et r. Elles sont déclarées mais non utilisées dans ce code.
l = []
r = []

# Initialise deux variables f_l et f_r à 0.
# Ces variables serviront à compter les parenthèses ouvrantes et fermantes rencontrées de chaque côté d'un caractère '*'.
f_l, f_r = 0, 0

# Boucle for qui itère depuis 0 jusqu'à l'index du caractère '*' (non inclus) dans la liste S.
# La méthode S.index('*') donne la position du premier '*' rencontré dans la chaîne.
for n in range(S.index('*')):
    # Vérifie si le caractère à la position n est une parenthèse ouvrante '('.
    if S[n] == '(':
        # Si oui, incrémente f_l de 1.
        f_l += 1
    # Si le caractère est une parenthèse fermante ')', alors
    elif S[n] == ')':
        # Décrémente f_l de 1.
        f_l -= 1

# Boucle for qui itère sur un nombre de fois égal à la distance entre la fin de la liste et la position du '*'.
# Cette fois-ci, le parcours se fait depuis la fin de la liste jusqu'à juste après '*'.
for n in range(S_l - S.index('*')):
    # Calcule l'index du caractère à examiner en partant de la fin de la liste.
    # S_l-n-1 donne le bon index pour parcourir la liste à l'envers.
    if S[S_l - n - 1] == ')':
        # Si le caractère est une parenthèse fermante, incrémente f_r de 1.
        f_r += 1
    # Si le caractère est une parenthèse ouvrante, alors
    elif S[S_l - n - 1] == '(':
        # Décrémente f_r de 1.
        f_r -= 1

# Affiche le minimum entre les deux compteurs f_l et f_r.
# Cela donne le plus petit des déséquilibres de parenthèses autour du caractère '*'.
print(min(f_r, f_l))