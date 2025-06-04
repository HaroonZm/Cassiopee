# Prend l'entrée utilisateur sous forme d'une chaîne de caractères et sépare la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur
# Utilise la fonction map pour convertir chaque sous-chaîne en entier
# Décompose la liste de trois entiers dans les variables h (un entier), a (entier de début), et b (entier de fin)
h, a, b = map(int, input().split())  # Ex : si l'utilisateur entre "12 2 6", alors h=12, a=2, b=6

# Initialise une variable pour garder une trace du nombre de diviseurs trouvés
# Commence à zéro puisqu'aucun diviseur n'a encore été trouvé
ans = 0

# Lance une boucle for qui itère sur chaque entier i compris entre a et b inclus
# range(a, b+1) produit une séquence d'entiers commençant à a et allant jusqu'à b (inclusivement car il faut ajouter 1 à b pour inclure la borne supérieure)
for i in range(a, b + 1):

    # Opérateur modulo (%) : calcule le reste de la division euclidienne de h par i
    # Si le reste est zéro, cela signifie que h est exactement divisible par i, donc i est un diviseur de h
    if h % i == 0:
        # Si la condition ci-dessus est vraie, on a trouvé un diviseur valide dans la plage [a, b]
        # On incrémente alors le compteur ans de 1
        ans += 1

# Affiche la valeur finale de ans, c'est-à-dire le nombre de diviseurs de h compris entre a et b (inclus)
print(ans)