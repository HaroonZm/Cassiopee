# Initialisation d'une liste vide pour stocker les nombres saisis
list1 = []

# Boucle pour demander à l'utilisateur d'entrer 6 nombres entiers
for i in range(6):
    n = int(input())  # Conversion de l'entrée utilisateur en entier
    list1.append(n)   # Ajout du nombre à la liste list1

# Séparation de list1 en deux listes : list2 contient les éléments à partir de l'index 4,
# list1 contient les éléments avant l'index 4
list2 = list1[4:]
list1 = list1[:4]

# Tri de list1 dans l'ordre croissant
list1.sort()
# Suppression du premier élément de list1 (le plus petit après tri)
del list1[0]

# Tri de list2 dans l'ordre croissant
list2.sort()
# Suppression du premier élément de list2 (le plus petit après tri)
del list2[0]

# Calcul de la somme des éléments restants dans list1
sum1 = sum(list1)
# Calcul de la somme des éléments restants dans list2
sum2 = sum(list2)

# Affichage de la somme totale des deux sommes calculées
print(sum1 + sum2)