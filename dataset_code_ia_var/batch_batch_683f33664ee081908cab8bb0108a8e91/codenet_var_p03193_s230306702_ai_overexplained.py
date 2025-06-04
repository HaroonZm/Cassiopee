# Demande à l'utilisateur de saisir une ligne de texte, stockée dans la variable 'nhw'
nhw = input()

# Coupe la ligne saisie à chaque espace pour obtenir une liste de chaînes de caractères.
# Par exemple, si l'utilisateur entre "3 10 20", la liste devient ["3", "10", "20"].
nhw = nhw.split(" ")

# Transforme chaque élément de la liste (qui sont des chaînes de caractères représentant des nombres)
# en un entier avec la fonction int(x), et construit une nouvelle liste avec ces entiers.
nhw = [int(x) for x in nhw]

# Initialise une variable 'count' à 0.
# Cette variable va servir à compter combien de fois une certaine condition sera vérifiée plus loin dans le code.
count = 0

# Commence une boucle pour répéter une action un certain nombre de fois.
# Le nombre de répétitions est donné par le premier élément de la liste 'nhw', qui est l'entier à l'indice 0 : nhw[0].
for i in range(nhw[0]):
    # A chaque itération (tour de boucle), on demande à l'utilisateur d'entrer une nouvelle ligne de texte.
    ab = input()
    
    # On coupe la ligne entrée à chaque espace pour obtenir une liste de chaînes.
    ab = ab.split(" ")
    
    # On convertit chaque entrée de la liste ab en un entier, en utilisant une compréhension de liste.
    ab = [int(x) for x in ab]
    
    # On vérifie une condition : 
    # Si le premier nombre de la liste ab (ab[0]) est supérieur ou égal au second élément de nhw (nhw[1])
    # ET que le second nombre de la liste ab (ab[1]) est supérieur ou égal au troisième élément de nhw (nhw[2])
    if ab[0] >= nhw[1] and ab[1] >= nhw[2]:
        # Si la condition est vraie, on incrémente la variable 'count' de 1, c'est-à-dire qu'on lui ajoute 1.
        count += 1

# Affiche la valeur de la variable 'count', c'est-à-dire le nombre de fois où la condition de la boucle a été remplie.
print(count)