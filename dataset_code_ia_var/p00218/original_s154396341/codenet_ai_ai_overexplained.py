# Début d'une boucle infinie, elle continuera de tourner tant que le programme ne rencontre pas une instruction 'break'
while True :
    # Lecture d'une ligne de texte depuis l'entrée standard (généralement le clavier)
    # Cette ligne est convertie en entier, et la valeur stockée dans la variable 'n'
    n = int(input())
    # Vérification si la valeur de 'n' est exactement égale à 0
    # Si c'est le cas, la boucle est interrompue grâce à l'instruction 'break'
    if n == 0 :
        break

    # Boucle for itérative allant de 0 à n-1 inclus, donc qui s'exécute exactement n fois
    for i in range(n) :
        # Lecture d'une ligne complète de texte depuis l'entrée standard
        # La méthode input() renvoie une chaîne de caractères (string)
        # Cette chaîne est découpée (séparateur: espace) en plusieurs morceaux avec la méthode split()
        # Chaque morceau est converti en entier avec map(int, ...)
        # Les trois résultats sont respectivement affectés aux variables 'm', 'e', 'j'
        m, e, j = map(int, input().split())
        # Premier critère: vérifie si l'une des trois notes est exactement 100
        # L'opérateur 'or' vérifie que cette condition soit vraie pour au moins une des trois variables
        if m == 100 or e == 100 or j == 100 :
            # Affichage du caractère "A" sur une ligne
            print("A")
        # Deuxième critère: la moyenne arithmétique des deux premières notes (mathématiques 'm' et anglais 'e') est au moins 90
        elif (m + e) / 2 >= 90 :
            print("A")
        # Troisième critère: la moyenne arithmétique des trois matières est au moins 80
        elif (m + e + j) / 3 >= 80 :
            print("A")
        # Quatrième critère: moyenne arithmétique des trois matières est au moins 70
        elif (m + e + j) / 3 >= 70 :
            print("B")
        # Cinquième critère: la moyenne des trois matières est au moins 50
        # ET au moins une des notes 'm' ou 'e' (maths ou anglais) est supérieure ou égale à 80
        elif (m + e + j) / 3 >= 50 and (m >= 80 or e >= 80) :
            print("B")
        # Cas par défaut : toutes les autres situations qui ne correspondent à aucun des critères précédents
        else :
            print("C")