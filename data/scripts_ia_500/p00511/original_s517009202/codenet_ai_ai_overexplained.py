# Demande à l'utilisateur de saisir une valeur initiale, qui sera stockée dans une variable nommée 'all'.
# La fonction input() prend l'entrée utilisateur sous forme de chaîne de caractères et la convertit en un objet Python,
# ici probablement en nombre si l'utilisateur saisit un chiffre.
all = input()

# On entre dans une boucle infinie, c'est-à-dire que ce bloc de code va être répété indéfiniment jusqu'à ce qu'une condition d'arrêt soit rencontrée.
while True:
    # Le bloc try nous permet de gérer proprement les erreurs qui pourraient survenir dans le bloc de code à l'intérieur,
    # ici notamment pour gérer la fin de l'entrée standard (EOFError).
    try:
        # On demande à l'utilisateur d'entrer une chaîne de caractères correspondant à une opération.
        # raw_input() lit une ligne de texte entrée par l'utilisateur de la console.
        # Cela fonctionne en Python 2. En Python 3, raw_input() n'existe plus et il faut utiliser input().
        str = raw_input()

        # On vérifie si la chaîne entrée est un symbole '='.
        # Si c'est le cas, cela signifie que l'utilisateur veut afficher le résultat final et sortir de la boucle.
        if str == '=':
            # Affiche la valeur courante de 'all' qui a été modifiée au cours des opérations.
            print all
            # On quitte la boucle infinie grâce à l'instruction break.
            break

        # Si la chaîne n'est pas '=', on attend une nouvelle entrée de l'utilisateur,
        # qui est censée être un nombre (opérande) pour l'opération arithmétique.
        num = input()

        # Si la chaîne entrée est '+', on additionne à la variable 'all' la valeur de 'num'.
        if str == '+':
            all += num
        # Sinon si la chaîne entrée est '-', on soustrait 'num' de 'all'.
        elif str == '-':
            all -= num
        # Sinon si la chaîne entrée est '*', on multiplie 'all' par 'num'.
        elif str == '*':
            all = all * num
        # Sinon si la chaîne entrée est '/', on divise 'all' par 'num'.
        elif str == '/':
            all = all / num

    # Ce bloc except intercepte une exception de type EOFError,
    # qui est levée lorsque l'entrée standard est fermée (par exemple Ctrl+D sous Unix).
    # Cela permet de sortir proprement de la boucle et ainsi du programme.
    except EOFError:
        break