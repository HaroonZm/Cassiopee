# Demande à l'utilisateur de saisir une entrée, et stocke cette entrée sous forme de chaîne de caractères dans la variable 'a'.
a = raw_input()

# Initialise un compteur 'ans' à 0, qui servira à compter le nombre de cas où certaines conditions seront remplies.
ans = 0

# Parcourt chaque position possible dans la chaîne 'a' en utilisant une boucle for et la fonction range(len(a)).
# 'i' prend alors toutes les valeurs possibles d'indices de 0 jusqu'à la longueur de 'a' moins 1.
for i in range(len(a)):
    # Vérifie d'abord si le caractère à la position 'i' dans la chaîne 'a' est strictement égal à "0"
    # et si cet indice n'est pas le dernier caractère de la chaîne (donc on n'est pas à la fin).
    # On utilise 'i != len(a) - 1' pour s'assurer que nous ne sommes pas au dernier caractère.
    if a[i] == "0" and i != len(a) - 1:
        # Si la condition est vraie, on utilise 'continue' pour ignorer le reste du code de la boucle
        # et passer à l'itération suivante du for, sans rien faire sur cet indice.
        continue

    # Calcule la variable 'a1', qui est le nombre entier constitué des caractères de la chaîne 'a'
    # qui vont du début jusqu'à, mais non compris, l'indice 'i'.
    # On utilise 'a[:i]' pour obtenir cette sous-chaîne. Si i est égal à 0, alors a[:i] donne une chaîne vide.
    # Dans ce cas, on considère 'a1' égal à 0 (puisqu'il n'y a aucun chiffre avant i).
    if i:
        a1 = int(a[:i])
    else:
        a1 = 0

    # Calcule la variable 'a2', qui est le nombre entier constitué des caractères de la chaîne 'a'
    # qui vont de l'indice 'i' jusqu'à la fin de la chaîne.
    # On utilise 'a[i:]' pour obtenir cette sous-chaîne.
    a2 = int(a[i:])

    # Maintenant, on vérifie deux conditions pour décider s'il faut compter ce cas :
    # Condition 1 : 'a1' doit être inférieur ou égal à 'a2' (a1 <= a2)
    # Condition 2 : 'a1' et 'a2' doivent avoir la même parité, c'est-à-dire
    #               qu'ils sont tous les deux pairs ou tous les deux impairs.
    #               Cela se teste avec 'a1 % 2 == a2 % 2', car le reste de la division par 2
    #               est identique si les deux nombres sont de même parité.
    if a1 <= a2 and a1 % 2 == a2 % 2:
        # Si les deux conditions sont vérifiées, on incrémente le compteur 'ans' de 1.
        ans += 1

# Après que la boucle for soit terminée, on affiche la valeur finale du compteur 'ans'.
# En Python 2, la fonction 'print' sans parenthèses est une instruction qui affiche ce qui la suit.
print ans