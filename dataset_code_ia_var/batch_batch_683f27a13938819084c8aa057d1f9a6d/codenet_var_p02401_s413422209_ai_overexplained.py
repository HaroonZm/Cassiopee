# Commence une boucle infinie qui ne s'arrêtera que si une condition explicite de sortie est rencontrée à l'intérieur de la boucle
while True:
    # Lis une ligne de texte entrée par l'utilisateur via le clavier (input retourne une chaîne de caractères)
    # Utilise la méthode split() pour découper la chaîne saisie en sous-chaînes à chaque espace rencontré
    # Ce découpage génère une liste de trois éléments (supposant un format comme '3 + 5')
    # Les trois éléments sont attribués dans l'ordre aux variables 'a', 'op' et 'b' respectivement
    a, op, b = input().split()
    
    # Convertit la variable 'a', qui est au départ une chaîne, en un entier (int)
    a = int(a)
    # Convertit la variable 'b', qui est aussi une chaîne issue de l'entrée utilisateur, en un entier (int)
    b = int(b)
    
    # Si l'opérateur fourni (op) est exactement le caractère '?' 
    # Cela sert ici de condition d'arrêt : si l'utilisateur entre '?' comme opérateur, la boucle s'arrête
    if op == "?":
        # On sort de la boucle à l'aide de l'instruction break
        break
    # Vérifie si l'opérateur est le signe plus '+', ce qui indique une addition
    elif op == "+":
        # Affiche la somme de 'a' et 'b' dans la console grâce à la fonction print()
        print(a + b)
    # Vérifie si l'opérateur est le signe moins '-', ce qui indique une soustraction
    elif op == "-":
        # Affiche la différence entre 'a' et 'b' dans la console
        print(a - b)
    # Vérifie si l'opérateur est le symbole de multiplication '*'
    elif op == "*":
        # Affiche le produit de 'a' et 'b' dans la console
        print(a * b)
    # Si aucune des conditions précédentes n'est remplie, c'est à dire si l'opérateur n'est ni '?', '+', '-', ni '*'
    else:
        # Effectue une division entière (quotient de 'a' par 'b', résultat arrondi vers zéro)
        # Affiche le résultat de cette division entière.
        print(a // b)