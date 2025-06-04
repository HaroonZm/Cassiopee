# Demander à l'utilisateur de saisir une valeur via la fonction input(), qui lit une chaîne de caractères tapée au clavier
# La fonction input() attend que l'utilisateur entre quelque chose et appuie sur la touche Entrée
# Par défaut, ce que l'utilisateur entre est une chaîne de caractères (de type str en Python)
# Pour effectuer des opérations mathématiques (comme l'exponentiation), il faut convertir cette chaîne en un nombre entier (int)
# La fonction int() convertit la chaîne de caractères en un entier
num = int(input())  # stocke le nombre entier saisi par l'utilisateur dans la variable 'num'

# Calculer le cube du nombre stocké dans 'num'
# L'opérateur '**' est l'opérateur d'exponentiation en Python
# 'num ** 3' signifie 'num' multiplié par lui-même trois fois (num * num * num)
# La fonction print() affiche la valeur calculée à l'écran
print(num ** 3)  # affiche le cube du nombre saisi par l'utilisateur