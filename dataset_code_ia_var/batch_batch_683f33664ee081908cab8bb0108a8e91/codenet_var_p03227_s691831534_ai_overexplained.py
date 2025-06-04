# Demande à l'utilisateur de saisir une chaîne de caractères via l'entrée standard (clavier).
# La fonction input() affiche éventuellement un message et attend que l'utilisateur tape quelque chose et appuie sur Entrée.
S = input()

# Vérifie si la longueur de la chaîne S est exactement égale à 3 caractères.
# len() calcule le nombre de caractères présents dans la chaîne S.
if len(S) == 3:
    # Si la condition précédente est vraie, alors on veut afficher la chaîne S à l'envers.
    # S[::-1] est une technique de 'slicing' (« tranchage de chaîne ») :
    # - Le premier deux-points indique de prendre tous les caractères, du début à la fin,
    # - Le -1 indique de parcourir la chaîne dans l'ordre inverse (de la fin vers le début).
    print(S[::-1])
else:
    # Sinon, c'est-à-dire si la longueur de S n'est PAS exactement 3,
    # on affiche simplement la chaîne S telle quelle, sans modification.
    print(S)