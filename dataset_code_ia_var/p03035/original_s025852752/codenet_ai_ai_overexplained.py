# Demande à l'utilisateur une entrée via le terminal
# La fonction input() lit une ligne de texte entrée par l'utilisateur
# .split(" ") sépare cette chaîne en une liste de chaînes, là où il y a des espaces
# Par exemple, si l'utilisateur tape "15 600", alors .split(" ") donne ["15", "600"]
user_input = input()

# Utilise une compréhension de liste pour convertir chaque chaîne de cette liste en entier
# int(i) pour chaque i dans la liste créée précédemment
# Le résultat est une liste de deux entiers, par exemple [15, 600]
int_list = [int(i) for i in user_input.split(" ")]

# Attribue le premier élément de la liste d'entiers à la variable a
# Attribue le second élément à la variable b
a = int_list[0]
b = int_list[1]

# Maintenant, on va décider de ce qu'on affiche en fonction de la valeur de a
# Si a est supérieur ou égal à 13 :
#    On affiche b (donc la valeur de la seconde entrée)
# Sinon, si a est supérieur ou égal à 6 (c'est-à-dire a vaut 6, 7, 8, 9, 10, 11 ou 12) :
#    On affiche la moitié de b, arrondie vers le bas (c'est ce que fait // en division entière)
# Sinon (donc a est strictement inférieur à 6) :
#    On affiche 0
#
# Ceci est réalisé en une seule ligne avec une structure conditionnelle compacte (opérateur ternaire)
if a >= 13:
    # Cas où a est au moins 13
    output = b
else:
    if a >= 6:
        # Cas où a est au moins 6 mais strictement inférieur à 13
        output = b // 2  # // signifie division entière
    else:
        # Cas où a est strictement inférieur à 6
        output = 0

# Affiche la valeur sélectionnée précédemment dans la console
print(output)