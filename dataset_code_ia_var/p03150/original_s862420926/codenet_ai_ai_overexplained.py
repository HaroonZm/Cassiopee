# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier.
# La fonction input() permet à l'utilisateur de taper une entrée, qui sera stockée dans la variable 's'.
s = input()

# Définit la variable 'k' contenant la chaîne 'keyence'.
# Cette chaîne est celle que le programme va rechercher sous une certaine forme dans 's'.
k = 'keyence'

# Initialise la variable 'r' à la valeur 'NO'.
# Cette variable sert à indiquer si une condition spécifique a été remplie ou non plus loin dans le code.
r = 'NO'

# Démarre une boucle for qui va itérer sur une séquence d'entiers allant de 0 jusqu'à la longueur de 'k' (exclu).
# La fonction len(k) retourne le nombre de caractères dans la chaîne 'k', soit 7 ici.
# La variable 'i' prendra ainsi successivement les valeurs 0, 1, 2, 3, 4, 5 et 6.
for i in range(len(k)):
    # Pour chaque valeur de 'i', le code prend une partie du début de 's' (de l'indice 0 jusqu'à l'indice i-1)
    # avec la notation de tranchage s[:i] (slicing), et la concatène avec une partie de la fin de 's'
    # (allant de l'indice -7+i jusqu'à la fin de la chaîne s, c'est-à-dire les derniers 7-i caractères).
    # L'idée est de retirer une sous-chaîne de longueur (7 - i), située quelque part dans 's', puis de
    # vérifier si la concaténation des parties restantes est exactement égale à 'keyence'.
    # La condition vérifie donc si la chaîne obtenue est identique à 'k'.
    if s[:i] + s[-7+i:] == k:
        # Si la condition est vraie, cela signifie qu'en retirant une certaine sous-chaîne de 's',
        # on obtient exactement la chaîne 'keyence'.
        # On affecte alors la valeur 'YES' à la variable 'r' pour indiquer que la condition est remplie.
        r = 'YES'
        # On quitte immédiatement la boucle grâce à l'instruction 'break' car on n'a plus besoin de vérifier d'autres cas.
        break

# Affiche la valeur de la variable 'r', qui sera soit 'YES' si la condition a été remplie précédemment,
# soit 'NO' si aucune condition n'a été remplie lors des itérations de la boucle.
print(r)