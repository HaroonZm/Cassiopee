# Demande à l'utilisateur de saisir une valeur et lit cette valeur en tant que chaîne de caractères (string) depuis l'entrée standard (le clavier).
# La fonction input() affiche une invite vide si aucun argument n'est donné, et attend que l'utilisateur tape une saisie valide.
# Une fois que l'utilisateur a fini de saisir et qu'il appuie sur Entrée, la saisie est renvoyée à la suite du programme sous forme de chaîne.
# La fonction int() convertit ensuite cette chaîne de caractères en un entier.
n = int(input())

# La déclaration if vérifie une condition.
# Dans ce cas, nous vérifions si la variable n est égale à 3, ou bien à 5, ou bien à 7.
# L'opérateur '==' teste l'égalité entre deux valeurs. Par exemple, n == 3 sera True uniquement si n est exactement égal à 3.
# L'opérateur 'or' est un opérateur logique qui retourne True si au moins une des conditions connectées est vraie.
# Donc si n vaut 3, 5 ou 7, l'expression entière (n==3 or n==5 or n==7) vaudra True.
if n == 3 or n == 5 or n == 7:
    # Si la condition du if (au-dessus) est vraie, le code indente (décalé d'une tabulation ou de 4 espaces) s'exécute.
    # Ici, on utilise la fonction print() pour afficher du texte à l'écran, en l'occurrence la chaîne "YES".
    print("YES")
else:
    # else capture tous les autres cas où la condition du if n'est pas remplie.
    # Le code indenté dans le bloc else s'exécutera seulement si la condition du if est fausse.
    # Encore une fois, print() affiche du texte, ici la chaîne "NO".
    print("NO")