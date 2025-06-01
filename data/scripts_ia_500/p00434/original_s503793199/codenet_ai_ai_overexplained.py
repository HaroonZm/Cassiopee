# Création d'une liste appelée list1 qui contiendra des entiers saisis par l'utilisateur
# La syntaxe utilisée est une compréhension de liste
# int(input()) signifie : demander une saisie clavier (input()), puis convertir cette saisie en entier (int)
# La boucle for i in range(28) indique que cette opération sera répétée 28 fois, pour i allant de 0 à 27 (mais i n'est pas utilisé dans la conversion)
list1 = [int(input()) for i in range(28)]

# Démarrage d'une boucle for qui parcourra tous les entiers de 1 à 30 inclus
# La fonction range(1,31) génère une suite de nombres allant de 1 jusqu'à 30 (31 non inclus)
for i in range(1, 31):
    # Vérification si le nombre i n'est pas présent dans la liste list1
    # L'opérateur in permet de tester si un élément est dans une liste; ici on utilise not in pour le contraire
    if not (i in list1):
        # Si i n'est pas dans list1, alors on l'affiche avec print()
        # print() affiche la valeur sur la sortie standard, ici la console
        print(i)