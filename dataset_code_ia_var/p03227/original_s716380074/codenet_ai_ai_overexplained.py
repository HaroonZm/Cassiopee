# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier
# La fonction input() affiche une invite (ici vide) et attend que l'utilisateur tape quelque chose, puis appuie sur Entrée
string = input()

# len(string) calcule la longueur de la chaîne (nombre de caractères contenus dans la variable string)
# On compare cette longueur à 3 avec l'opérateur == pour voir si la chaîne contient exactement 3 caractères
if len(string) == 3:
    # Si la condition est vraie (la chaîne a exactement 3 caractères), alors on exécute ce bloc
    # string[::-1] permet d'inverser la chaîne de caractères :
    #   - L'opérateur [] permet de faire un "slice" (sous-chaîne)
    #   - Les 2 points :: signifient que l'on ne change pas le début ni la fin du slice
    #   - Le -1 indique de parcourir la chaîne à l'envers (pas de -1)
    # print() affiche à l'écran ce qui lui est passé en argument ; ici, on affiche la chaîne inversée
    print(string[::-1])
else:
    # Sinon (si la longueur de la chaîne n'est pas exactement 3 caractères)
    # On affiche la chaîne telle quelle, sans la modifier
    print(string)