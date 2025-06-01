# Demande à l'utilisateur d'entrer une ligne de texte via le clavier
# La fonction input() affiche une invite vide et récupère ce que l'utilisateur tape
# L'entrée est reçue sous forme de chaîne de caractères (string)
# La méthode split() est appelée sur cette chaîne pour la diviser en plusieurs sous-chaînes,
# en utilisant par défaut l'espace comme séparateur.
# Par exemple, si l'utilisateur entre "3 4 5", split() retournera la liste ["3", "4", "5"]
user_input = input()  # Récupération de la saisie utilisateur

# Découpage de la chaîne de caractères en une liste de chaînes, en séparant sur les espaces
split_input = user_input.split()  # Liste de chaînes contenant les différents nombres

# La fonction map() applique une fonction donnée à chaque élément d'un itérable (ici, split_input)
# map(int, split_input) applique la fonction int() à chaque élément de split_input,
# transformant ainsi chaque chaîne numérique en un entier.
# La fonction list() convertit ensuite ce résultat map (un objet itérable) en une liste réelle.
# Ainsi, on obtient une liste d'entiers.
i = list(map(int, split_input))  # Conversion des chaînes en entiers

# On accède à l'élément d'indice 1 de la liste i, c'est-à-dire le deuxième nombre saisi
# Puis on le divise par l'élément d'indice 0 (premier nombre saisi)
# Ensuite, on multiplie le résultat par l'élément d'indice 2 (troisième nombre saisi)
# Effectivement, ce calcul suit la formule : (i[1] / i[0]) * i[2]
result = (i[1] / i[0]) * i[2]  # Calcul demandé avec les éléments de la liste

# Enfin, la fonction print() affiche le résultat du calcul sur la console,
# ce qui permet à l'utilisateur de voir la sortie du programme
print(result)  # Affichage du résultat final à l'écran