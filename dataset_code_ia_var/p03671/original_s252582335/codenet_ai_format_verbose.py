# Demande à l'utilisateur de saisir plusieurs nombres entiers séparés par des espaces
entrée_utilisateur = input("Veuillez saisir plusieurs nombres entiers séparés par des espaces : ")

# Convertit chaque élément de l'entrée utilisateur en un entier, créant ainsi une liste d'entiers
liste_nombres_entiers = list(map(int, entrée_utilisateur.split()))

# Trie la liste des entiers dans l'ordre croissant
liste_nombres_triés = sorted(liste_nombres_entiers)

# Sélectionne les deux plus petits entiers de la liste triée
deux_plus_petits_nombres = liste_nombres_triés[:2]

# Calcule la somme des deux plus petits entiers
somme_deux_plus_petits_nombres = sum(deux_plus_petits_nombres)

# Affiche le résultat
print(somme_deux_plus_petits_nombres)