# Demander à l'utilisateur de saisir un nombre entier qui sera stocké dans la variable n
n = int(input())

# Demander à l'utilisateur de saisir une ligne d'entiers séparés par des espaces
# L'appel à input() lit cette ligne sous forme de chaîne de caractères
# split() découpe cette chaîne en une liste de sous-chaînes à chaque espace
# map(int, ...) applique la fonction int à chaque sous-chaîne, transformant chaque élément de la liste en entier
# list(...) convertit l'objet map en une liste réelle d'entiers, que l'on stocke dans la variable a
a = list(map(int, input().split()))

# Initialiser la variable ans à la valeur 'APPROVED'
# Cette variable servira à stocker le résultat final après traitement des valeurs de la liste a
ans = 'APPROVED'

# Parcourir (itérer) chaque entier x de la liste a
for x in a:
    # Vérifier si le nombre x est impair
    # L'opérateur % (modulo) donne le reste de la division de x par 2
    # Si ce reste est 1, le nombre est impair
    if x % 2 == 1:
        # L'instruction continue force la boucle à passer directement à l'itération suivante
        # Ainsi, on ne traite pas plus loin les nombres impairs
        continue
    # Si on arrive ici, c'est que x est pair (car sinon on aurait sauté cette partie avec continue)
    # On vérifie alors une condition supplémentaire :
    #   - x doit être à la fois pair, et divisible soit par 3, soit par 5
    #   - x % 2 == 0 vérifie que x est pair (ceci est déjà vrai ici)
    #   - (x % 3 == 0 or x % 5 == 0) vérifie que x est divisible par 3 ou par 5
    # Le mot-clé not inverse la condition logique : on entre dans le bloc si x n'est pas divisible par 3 ou 5
    if not (x % 2 == 0 and (x % 3 == 0 or x % 5 == 0)):
        # Si x ne remplit pas la condition, on considère que la règle n'est pas respectée
        # On change la valeur de ans en 'DENIED'
        ans = 'DENIED'
# Après la fin de la boucle (après avoir examiné tous les éléments de la liste a),
# on affiche (imprime à l'écran) la valeur finale de ans
print(ans)