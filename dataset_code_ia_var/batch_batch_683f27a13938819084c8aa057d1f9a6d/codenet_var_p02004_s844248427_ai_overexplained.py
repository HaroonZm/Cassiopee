# Demande à l'utilisateur d'entrer une chaîne de caractères depuis le clavier et stocke cette chaîne dans la variable S.
S = input()

# Initialise une variable "count" à 0.
# Cette variable va servir à compter le nombre de fois où la direction fait un tour complet vers la droite.
count = 0

# Initialise une variable "direction" à 0.
# Cette variable va servir à compter le "score" directionnel en fonction des caractères rencontrés.
direction = 0

# Parcourt chaque indice de la chaîne S, de 0 jusqu'à (longueur de S) - 1.
for i in range(len(S)):
    # Si le caractère à la position i est égal à la chaîne de caractère 'R',
    # cela signifie qu'on a rencontré une indication vers la droite.
    if S[i] == 'R':
        # Incrémente la variable direction de 1.
        direction += 1
    else:
        # Si le caractère n'est pas 'R' (peut-être 'L' ou autre),
        # on considère qu'on a rencontré une indication vers la gauche et on décrémente.
        direction -= 1
    # Si la variable direction atteint exactement la valeur 4,
    # cela signifie qu'on a tourné 4 fois vers la droite, effectuant un cycle complet (360 degrés).
    if direction == 4:
        # Incrémente la variable count de 1 pour marquer qu'un tour complet a été effectué.
        count += 1
        # Remet la direction à 0 pour entamer le comptage d'un nouveau cycle complet.
        direction = 0
    # Si la variable direction atteint la valeur -4,
    # cela signifie qu'on a tourné 4 fois vers la gauche, soit un tour complet dans l'autre sens.
    elif direction == -4:
        # Ici, contrairement au cas précédent, on ne compte pas ce tour, on fait juste repartir la direction à 0.
        direction = 0

# Affiche (imprime) la valeur de la variable count, qui correspond au nombre de cycles complets de "4R".
print(count)