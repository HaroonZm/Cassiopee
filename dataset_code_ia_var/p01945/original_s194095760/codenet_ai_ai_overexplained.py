# Demande à l'utilisateur de rentrer une chaîne de caractères au clavier
# La fonction input() affiche une invite vide et récupère ce que l'utilisateur tape jusqu'à appuyer sur Entrée
line = input()

# Initialise une variable entière appelée 'lebel' à 0
# Cette variable servira de compteur pour suivre le niveau d'imbrication des parenthèses
lebel = 0

# Débute une boucle 'for' pour parcourir tous les indices dans la chaîne 'line'
# 'range(len(line))' génère une séquence de nombres entiers allant de 0 à la longueur de la chaîne moins 1
# Chaque nombre 'i' représente l'indice d'un caractère dans la chaîne 'line'
for i in range(len(line)):
    # Vérifie si le caractère à la position 'i' de la chaîne 'line' est un astérisque ('*')
    # Le double égal '==' vérifie si deux valeurs sont identiques
    if line[i] == '*':
        # Affiche la valeur courante de la variable 'lebel' à l'écran
        # print() convertit la variable en chaîne de caractères et l'affiche
        print(lebel)
        # Le mot-clé 'break' interrompt immédiatement la boucle 'for', on quitte donc la boucle ici
        break
    # Vérifie ensuite si le caractère à la position actuelle 'i' est une parenthèse ouvrante '('
    if line[i] == '(':
        # Si c'est le cas, on incrémente (augmente de 1) la variable 'lebel' à l'aide de l'opérateur +=
        # Cela signifie qu'on entre dans un nouveau niveau de parenthèses
        lebel += 1
    # Sinon, si le caractère à la position 'i' est une parenthèse fermante ')'
    elif line[i] == ')':
        # On décrémente (diminue de 1) la variable 'lebel' pour signaler qu'on sort d'un niveau de parenthèses
        lebel -= 1
# La boucle termine quand on a parcouru tous les caractères de la chaîne ou quand on rencontre un astérisque ('*')