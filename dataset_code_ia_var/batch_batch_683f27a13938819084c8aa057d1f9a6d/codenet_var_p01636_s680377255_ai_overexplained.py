# Demande à l'utilisateur d'entrer une chaîne de caractères via l'entrée standard.
# La fonction raw_input() lit une ligne de texte de l'utilisateur et la retourne sous forme de chaîne (str).
s = raw_input()

# Initialise une variable appelée 'ans' à 0.
# Cette variable servira à compter le nombre de fois où une certaine condition est satisfaite dans la boucle à venir.
ans = 0

# Utilise une boucle for pour parcourir chaque indice 'i' dans la chaîne 's'.
# La fonction range(len(s)) génère une séquence de nombres entiers allant de 0 jusqu'à la longueur de la chaîne 's' moins 1.
# Cela permet d'itérer sur chaque position possible dans la chaîne, y compris la première (indice 0) et la dernière (indice len(s) - 1).
for i in range(len(s)):
    # Vérifie si le caractère à la position 'i' dans la chaîne est le caractère '0'.
    # s[i] permet d'accéder au caractère à l'indice 'i' de la chaîne 's'.
    # De plus, on vérifie que 'i' n'est pas l'indice du dernier élément de la chaîne.
    # len(s) - 1 donne l'indice de la dernière position de la chaîne.
    if s[i] == "0" and i != len(s) - 1:
        # Si la condition ci-dessus est vraie, on utilise 'continue' pour passer à l'itération suivante de la boucle.
        # Cela signifie que tout le code restant dans cette boucle ne sera pas exécuté pour cette itération spécifique.
        continue

    # On définit la variable 'left' comme la partie gauche de la chaîne, avant la position 'i'.
    # s[:i] extrait tous les caractères depuis le début de la chaîne jusqu'à l'indice 'i' (exclu).
    # int(s[:i]) convertit cette sous-chaîne en entier.
    # Si 'i' vaut 0 (c'est-à-dire que s[:0] est une chaîne vide), alors on affecte simplement la valeur 0 à 'left' grâce au 'if i else 0'.
    left = int(s[:i]) if i else 0

    # On définit la variable 'right' comme la partie droite de la chaîne à partir de la position 'i' jusqu'à la fin.
    # s[i:] extrait tous les caractères de l'indice 'i' à la fin de la chaîne.
    # int(s[i:]) convertit cette sous-chaîne en entier.
    right = int(s[i:])

    # Vérifie deux conditions en même temps à l'aide de l'opérateur logique 'and':
    # 1. Vérifie si la valeur de 'left' est inférieure ou égale à celle de 'right' (left <= right).
    # 2. Vérifie si le reste (modulo) de la division de 'left' par 2 est égal au reste de la division de 'right' par 2,
    #    c'est-à-dire que 'left' et 'right' sont soit tous les deux pairs, soit tous les deux impairs.
    if left <= right and left % 2 == right % 2:
        # Si les deux conditions sont remplies, incrémente la variable 'ans' de 1.
        # ans += 1 est équivalent à ans = ans + 1.
        ans += 1

# Affiche la valeur finale de 'ans' à l'aide de la fonction print.
# Cela montre combien d'indices 'i' satisfont les conditions spécifiées ci-dessus.
print ans