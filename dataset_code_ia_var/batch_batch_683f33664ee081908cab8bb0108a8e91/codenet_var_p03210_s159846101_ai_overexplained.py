# Demande à l'utilisateur de saisir une entrée au clavier à l'aide de la fonction input().
# La fonction input() renvoie toujours une chaîne de caractères.
# On utilise la fonction int() pour convertir cette chaîne de caractères en un nombre entier.
x = int(input())

# Début d'une structure conditionnelle "if"
# On vérifie si la variable x est égale à 5, à 7, ou à 3.
# L'opérateur '==' compare la valeur de x à un nombre donné.
# L'opérateur 'or' permet de combiner plusieurs conditions.
# Si l'une des conditions reliées par 'or' est vraie, alors le bloc associé s'exécute.

if x == 5 or x == 7 or x == 3:
    # Si x vaut 5 OU x vaut 7 OU x vaut 3, alors
    # La fonction print() affiche le texte "YES" à l'écran.
    print("YES")
else:
    # Si aucune des conditions précédentes n'est vraie (donc si x n'est ni 5, ni 7, ni 3),
    # alors le bloc else s'exécute.
    # La fonction print() affiche le texte "NO" à l'écran.
    print("NO")