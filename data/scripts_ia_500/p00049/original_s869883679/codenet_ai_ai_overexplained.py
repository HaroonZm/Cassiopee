# Initialisation de la variable 'a' à 0
# Cette variable servira à compter le nombre d'occurrences du groupe sanguin "A"
a = 0

# Initialisation de la variable 'b' à 0
# Cette variable servira à compter le nombre d'occurrences du groupe sanguin "B"
b = 0

# Initialisation de la variable 'o' à 0
# Cette variable servira à compter le nombre d'occurrences du groupe sanguin "O"
o = 0

# Initialisation de la variable 'ab' à 0
# Cette variable servira à compter le nombre d'occurrences du groupe sanguin "AB"
ab = 0

# Boucle infinie qui va permettre de lire les entrées utilisateur jusqu'à interruption
while True:
    try:
        # Lecture d'une ligne de texte depuis l'entrée standard (clavier)
        # La méthode input() attend que l'utilisateur tape quelque chose puis appuie sur Enter
        # La chaîne lue est ensuite scindée en deux parties à partir de la virgule grâce à split(",")
        # 'n' reçoit la première partie, 'bt' la deuxième partie
        n, bt = input().split(",")
        
        # Condition qui vérifie si la valeur de 'bt' est la chaîne de caractères "A"
        if bt == "A":
            # Si c'est le cas, on incrémente de un le compteur des "A"
            a += 1
        # Condition qui vérifie si la valeur de 'bt' est la chaîne de caractères "B"
        elif bt == "B":
            # Incrémente le compteur des "B" de un
            b += 1
        # Condition qui vérifie si la valeur de 'bt' est la chaîne de caractères "O"
        elif bt == "O":
            # Incrémente le compteur des "O" de un
            o += 1
        # Condition qui vérifie si la valeur de 'bt' est la chaîne de caractères "AB"
        elif bt == "AB":
            # Incrémente le compteur des "AB" de un
            ab += 1
    except:
        # Si une erreur se produit dans le bloc try (par exemple, aucune entrée ou entrée mal formée)
        # On sort de la boucle infinie avec 'break', ce qui interrompt la lecture des entrées
        break

# Affichage des résultats stockés dans les variables 'a', 'b', 'ab' et 'o'
# La fonction print() affiche plusieurs arguments en les séparant par défaut par des espaces
# Ici, on utilise l'argument 'sep' pour spécifier que les valeurs doivent être affichées sur des lignes distinctes,
# en remplaçant l'espace par un saut de ligne ("\n")
print(a, b, ab, o, sep="\n")