# Demande à l'utilisateur de saisir une première chaîne de caractères, qui est lue depuis l'entrée standard
# La valeur est stockée dans la variable 's'
s = input()

# Demande à l'utilisateur de saisir une seconde chaîne de caractères, qui est lue également depuis l'entrée standard
# La valeur est stockée dans la variable 't'
t = input()

# Crée une liste de booléens appelée 'l' ayant la même longueur que la chaîne 's'
# Remplit cette liste entièrement de la valeur False
# Cela signifie que chaque élément de 'l' est initialisé à False
l = [False] * len(s)

# Initialise la variable 'c' à 0
# 'c' servira à compter le nombre de caractères correspondants lors de la comparaison de sous-chaînes
c = 0

# Initialise la variable 'm' à 0
# 'm' va garder en mémoire la valeur maximum trouvée pour 'c' pendant toutes les itérations
m = 0

# Utilise une boucle 'for' pour définir la variable 'x'
# La fonction range() génère une séquence de nombres, commençant à 0 par défaut
# La fin de la séquence est (len(s) - len(t) + 1), ce qui garantit que les sous-chaînes extraites de 's' ont la même longueur que 't'
# Cela permet de faire glisser une fenêtre de la taille de 't' sur 's' pour toutes les positions possibles
for x in range(len(s) - len(t) + 1):
    # Réinitialise le compteur 'c' à 0 à chaque nouvelle position de la fenêtre
    c = 0
    # Démarre une nouvelle boucle 'for' imbriquée pour la variable 'y'
    # Cette boucle parcourt tous les indices valides de la chaîne 't'
    for y in range(len(t)):
        # Extrait une sous-chaîne 'w' de 's' qui part de l'indice 'x' et prend len(t) caractères
        # Cela correspond à la fenêtre courante de la même longueur que 't'
        w = s[x:x + len(t)]
        # Compare le caractère de la sous-chaîne 'w' à la position 'y' avec le caractère de 't' à la même position 'y'
        # Si les caractères sont égaux, cela signifie qu'il y a une correspondance de caractères à cet emplacement précis
        if w[y] == t[y]:
            # Incrémente la variable 'c' de 1 pour noter cette correspondance
            c += 1
    # Met à jour la variable 'm' en prenant la valeur maximale entre la valeur courante de 'm' et la valeur courante de 'c'
    # Cela permet de mémoriser le meilleur score trouvé sur toutes les fenêtres considérées jusqu'à présent
    m = max(m, c)

# À la fin des boucles, affiche le résultat du calcul : la différence entre la longueur de 't' et la valeur maximale 'm'
# Cette différence indique le nombre minimum de modifications nécessaires pour faire correspondre une sous-chaîne de 's' à 't'
print(len(t) - m)