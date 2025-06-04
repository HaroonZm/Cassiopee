# Initialisation de la variable 'a' à 0, qui va compter le nombre de sang de groupe 'A'
a = 0

# Initialisation de la variable 'b' à 0, qui va compter le nombre de sang de groupe 'B'
b = 0

# Initialisation de la variable 'o' à 0, qui va compter le nombre de sang de groupe 'O'
o = 0

# Initialisation de la variable 'ab' à 0, qui va compter le nombre de sang de groupe 'AB'
ab = 0

# Début d'une boucle infinie. 'while True' signifie que la boucle continuera jusqu'à ce qu'une instruction 'break' soit rencontrée
while True:
    try:
        # Demande à l'utilisateur d'entrer une chaîne de caractères. Par exemple : "Jean,A"
        # La fonction input() lit la saisie de l'utilisateur depuis le clavier, sous forme de texte
        # Ensuite, la méthode split(",") découpe cette chaîne en une liste, en utilisant la virgule comme séparateur
        # Par exemple : si l'utilisateur entre "Marie,B", alors n vaudra "Marie" et bt vaudra "B"
        n, bt = input().split(",")
        
        # Vérifie si la variable 'bt' (qui contient le groupe sanguin sous forme de texte) est exactement égale à "A"
        if bt == "A":
            # Si le groupe est "A", incrémente (ajoute 1) à la variable 'a'
            a += 1
        # Si bt n'est pas "A", vérifie si bt est égal à "B"
        elif bt == "B":
            # Si le groupe est "B", incrémente (ajoute 1) à la variable 'b'
            b += 1
        # Si bt n'est pas "A" ni "B", vérifie si bt est égal à "O"
        elif bt == "O":
            # Si le groupe est "O", incrémente (ajoute 1) à la variable 'o'
            o += 1
        # Si bt n'est pas "A", "B" ni "O", vérifie s'il est égal à "AB"
        elif bt == "AB":
            # Si le groupe est "AB", incrémente (ajoute 1) à la variable 'ab'
            ab += 1
        # Si aucune condition n'est vraie, le programme ne fait rien (aucun bloc 'else' ici)
    except:
        # Si une erreur (une exception) survient dans le bloc 'try'
        # Cela peut arriver si l'utilisateur n'entre rien, ou si la saisie n'est pas au bon format
        # Dans ce cas, on sort de la boucle infinie grâce au mot-clé 'break'
        break

# Affiche le contenu des variables 'a', 'b', 'ab', 'o', chacune sur une ligne différente
# La fonction print() affiche des informations à l'écran
# L'argument 'sep="\n"' indique que chaque valeur doit être séparée par un saut de ligne (nouvelle ligne)
print(a, b, ab, o, sep="\n")