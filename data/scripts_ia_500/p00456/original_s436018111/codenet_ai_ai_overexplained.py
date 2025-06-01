# Initialisation d'une liste vide nommée dataW pour stocker les données associées à W
dataW = [] 

# Initialisation d'une liste vide nommée dataK pour stocker les données associées à K
dataK = []

# Une boucle for qui va s'exécuter 10 fois (de 0 à 9)
for i in range (10):
    # Lecture d'une entrée utilisateur convertie en entier et stockée dans la variable 'a'
    a = int(input())
    # Ajout de la valeur entière 'a' à la liste dataW en utilisant la méthode append
    dataW.append(a)

# Tri des éléments de la liste dataW par ordre croissant
dataW.sort()

# Calcul de la somme des trois plus grandes valeurs dans dataW
# dataW[9] correspond au dernier élément (la plus grande valeur après tri)
# dataW[8] correspond à l'avant-dernier élément
# dataW[7] correspond au troisième plus grand élément
pointW = dataW[9] + dataW[8] + dataW[7]

# Une seconde boucle for similaire à la première, mais pour collecter des données dans dataK
for i in range(10):
    # Lecture d'une entrée utilisateur convertie en entier et stockée dans 'a'
    a = int(input())
    # Ajout de 'a' à la liste dataK
    dataK.append(a)

# Tri des éléments de dataK dans l'ordre croissant
dataK.sort()

# Calcul de la somme des trois plus grandes valeurs dans dataK
pointK = dataK[9] + dataK[8] + dataK[7]

# Affichage des résultats des calculs, c’est-à-dire les sommes des trois plus grands éléments de dataW et dataK
print(pointW, pointK)