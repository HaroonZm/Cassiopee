# Initialisation d'une variable appelée 'sum' avec la valeur 0
# Cette variable servira à accumuler la somme des nombres que l'utilisateur va entrer
sum = 0

# Début d'une boucle 'for' qui va s'exécuter 10 fois
# Le mot-clé 'range(10)' génère une suite de nombres de 0 à 9 (10 nombres en total)
# Le caractère '_' est utilisé ici comme une variable temporaire pour indiquer que sa valeur n'a pas d'importance
for _ in range(10):
    # Appel de la fonction 'input()' qui attend que l'utilisateur entre une donnée au clavier
    # Le texte entré est initialement une chaîne de caractères (string)
    # La fonction 'int()' convertit cette chaîne de caractères en un entier (integer)
    l = int(input())
    
    # Ajout de l'entier saisi par l'utilisateur à la variable 'sum'
    # L'opérateur '+=' signifie "ajoute la valeur de droite à la variable de gauche"
    sum += l

# Après la fin de la boucle, la variable 'sum' contient la somme totale des 10 nombres entrés
# La fonction 'print()' affiche cette somme à l'écran pour que l'utilisateur puisse la voir
print(sum)