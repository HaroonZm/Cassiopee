# Définition de la fonction check qui va comparer deux chaînes de caractères t et s
def check(t, s):
    # Initialisation d'une variable count à 0
    # Cette variable servira à compter le nombre de caractères différents entre les deux chaînes
    count = 0
    # La fonction range(len(t)) crée un itérable de nombres entiers allant de 0 jusqu'à la longueur de t (exclue)
    # Donc, cela permet d'accéder à chaque indice de la chaîne t, un par un
    for i in range(len(t)):
        # On compare le caractère de s et le caractère de t à la même position i
        # Si ces caractères sont différents (c'est-à-dire qu'ils ne sont pas égaux)
        if s[i] != t[i]:
            # On incrémente la variable count de 1
            # Cela signifie qu'un caractère ne correspond pas à l'autre à cet emplacement
            count += 1
    # Une fois la boucle terminée, la variable count contient le nombre total de positions où t et s diffèrent
    return count

# On demande à l'utilisateur de saisir une chaîne de caractères et on l'assigne à la variable s
# La fonction input() attend que l'utilisateur saisisse une valeur, puis appuie sur Entrée
s = input()
# On demande à l'utilisateur de saisir une deuxième chaîne de caractères et on l'assigne à la variable t
# Cela permet d'avoir deux chaînes à comparer plus tard
t = input()

# On définit une variable ans et on lui donne une valeur très grande (9999999999)
# Cela servira de valeur de départ pour chercher le minimum dans les comparaisons futures
ans = 9999999999

# On va boucler dans la plage allant de 0 jusqu'à la longueur de s moins la longueur de t plus 1
# range(len(s) - len(t) + 1) produira tous les indices de début possibles pour des sous-chaînes de s
# ayant exactement la même longueur que t
for i in range(len(s) - len(t) + 1):
    # A chaque itération, on extrait une sous-chaîne de s commençant à l'indice i et de longueur len(t)
    # s[i:i+len(t)] sélectionne les caractères de s depuis la position i jusqu'à (i + len(t) - 1) inclus
    # On passe cette sous-chaîne, ainsi que t, à la fonction check
    # check(t, s[i:i+len(t)]) va donc compter combien de caractères diffèrent entre t et la sous-chaîne de s
    # La fonction min(ans, ...) retourne la plus petite valeur entre ans et le résultat retourné par check
    # Cela permet de stocker dans ans le plus petit nombre de différences trouvé jusqu'à présent
    ans = min(ans, check(t, s[i:i+len(t)]))

# Après avoir testé toutes les sous-chaînes possibles de s de la même longueur que t,
# la variable ans contient le plus petit nombre de différences trouvé
# On affiche ce résultat sur la sortie standard (l'écran)
print(ans)