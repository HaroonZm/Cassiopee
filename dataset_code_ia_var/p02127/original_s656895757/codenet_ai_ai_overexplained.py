# Demande à l'utilisateur de saisir une chaîne de caractères, qui sera assignée à la variable 's'
s = input()
# Demande à l'utilisateur de saisir une autre chaîne.
# On ajoute explicitement un espace au début de cette chaîne et on l'assigne à la variable 't'.
t = " " + input()

# Initialisation d'une liste 'line' avec une seule valeur 1.
# Cette liste va servir pour stocker des compteurs multipositionnels, à la façon d'un compteur en base arbitraire.
line = [1]

# Initialisation de la variable 'next' à 1.
# 'next' va pointer vers la prochaine position de caractère à comparer dans la chaîne 't'
next = 1

# Calcul de la longueur de la chaîne 't', et assignation du résultat à 't_size'
t_size = len(t)

# Initialisation d'un indicateur booléen 'flag' à False.
# Ce flag n'est jamais utilisé par la suite, mais il est initialisé ici.
flag = False

# Boucle for qui itère à travers chaque caractère de la chaîne 's'
for i in s:
    # Vérifie si le caractère courant de 'i' est égal au caractère de 't' à la position 'next'
    # Cela permet de suivre la progression de l'assemblage de 't' dans 's'.
    if t[next] == i:
        # Incrémente la première valeur de la liste 'line' de 1.
        # Ceci correspond à faire avancer le compteur à la position suivante.
        line[0] += 1
        # Met à jour 'next' en le mettant égal à la nouvelle valeur de line[0]
        next = line[0]
        # Ajoute un nouveau zéro à la fin de la liste 'line'
        # Cela prépare le compteur pour un éventuel passage à une position supplémentaire.
        line += [0]
        # Initialise 'j' à 0, pour servir d'index lors de l'ajustement des retenues du compteur
        j = 0
        # Tant que la valeur 'line[j]' atteint la taille de la chaîne 't'
        while line[j] == t_size:
            # Remet la valeur line[j] à 0 (comme dans l'addition avec retenue)
            line[j] = 0
            # Incrémente la prochaine position line[j + 1] de 1 et met à jour 'next' avec cette nouvelle valeur.
            next = line[j + 1] = line[j + 1] + 1
            # Passe à la position suivante du compteur
            j += 1
        # Si le dernier élément de 'line' est égal à 0
        if line[-1] == 0:
            # On le retire (en quelque sorte, "nettoyage" des zéros non significatifs)
            line.pop()
# Affiche la longueur de la liste 'line' moins 1.
# Ceci représente le nombre de fois où il a fallu un nouvel "étage" pour compter.
print(len(line) - 1)