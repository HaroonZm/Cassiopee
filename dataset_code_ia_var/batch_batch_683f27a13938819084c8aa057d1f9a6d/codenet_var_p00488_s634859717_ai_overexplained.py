# Création d'une liste vide appelée l. Cette liste va contenir trois entiers.
l = []

# Démarrage d'une boucle for. La boucle va s'exécuter 3 fois. La fonction range(3) génère les entiers 0, 1 et 2.
for i in range(3):
    # Demande à l'utilisateur de saisir une valeur au clavier. La fonction input retourne une chaîne de caractères.
    # int() convertit la chaîne de caractères saisie en entier.
    tmp = int(input())
    # Ajoute l'entier obtenu à la fin de la liste l, en utilisant la méthode append().
    l.append(tmp)

# Création d'une deuxième liste vide appelée j. Cette liste va contenir deux entiers.
j = []

# Nouveau bloc de boucle for. Cette fois, la boucle va s'exécuter 2 fois (i prend les valeurs 0 et 1).
for i in range(2):
    # Demande à l'utilisateur un autre entier, convertit l'entrée en entier comme précédemment.
    tmp = int(input())
    # Ajoute ce nouvel entier à la liste j.
    j.append(tmp)

# La fonction min() retourne la plus petite valeur d'une séquence (ici, d'une liste).
# min(l) donne le plus petit des trois entiers stockés dans l.
# min(j) donne le plus petit des deux entiers stockés dans j.
# On additionne ces deux valeurs minimales, puis on retranche 50 au résultat.
# Le résultat de ce calcul est stocké dans la variable a.
a = min(l) + min(j) - 50

# Affiche la valeur stockée dans a sur la sortie standard (habituellement l'écran).
print(a)