# Demande à l'utilisateur d'entrer une valeur qui sera évaluée comme une expression Python.
# Cela permet d'accepter aussi bien des nombres entiers, des flottants, des opérations arithmétiques, etc.
# Par exemple, si l'utilisateur tape "3 + 2", le résultat de eval(input()) sera 5.
n = eval(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères.
# input() lit toute la ligne entrée par l'utilisateur au format texte (string).
# La méthode count('R') compte combien de fois la lettre 'R' apparaît dans la chaîne saisie.
r_count = input().count('R')

# On veut savoir si le nombre de 'R' rencontrés dans la chaîne donnée par l'utilisateur
# dépasse la moitié de la valeur de n (c'est-à-dire si r_count > n/2).
# Si c'est vrai, on affiche "Yes". Sinon, on affiche "No".
# L'instruction print() affiche le texte à l'écran.
# L'opérateur conditionnel ternaire (ou expression conditionnelle) permet d'effectuer ce test en une ligne :
# "Yes" if condition else "No". Si la condition (r_count > n/2) est vraie, "Yes" est affiché, sinon "No" l'est.
print("Yes" if r_count > n/2 else "No")