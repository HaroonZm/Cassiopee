# Demande à l'utilisateur d'entrer deux entiers séparés par un espace.
# Par exemple, si l'utilisateur saisit "5 3", alors N vaudra 5 et K vaudra 3.
# input() lit la ligne de texte saisie par l'utilisateur.
# split() divise cette chaîne en une liste d'éléments, en utilisant l'espace comme séparateur par défaut.
# map(int, ...) applique la fonction int à chaque élément de la liste obtenue, convertissant chaque sous-chaîne en entier.
# Les deux entiers convertis sont ensuite respectivement affectés à N et K.
N, K = map(int, input().split())

# Initialise la variable ans avec la valeur 1.
# Cette variable 'ans' va recevoir une nouvelle valeur à chaque itération.
ans = 1

# for _ in range(N-1): exécute une boucle for qui va répéter le bloc indenté juste en dessous.
# range(N-1) génère une séquence de nombres de 0 à N-2 (inclus), c'est-à-dire (N-1) valeurs au total.
# L'underscore (_) est utilisé comme nom de variable lorsqu'on n'a pas besoin de la valeur courante de la boucle.
for _ in range(N-1):
    # Calcule l'expression (ans + K - 2) // (K - 1).
    # Opérateur + effectue une addition. // effectue une division entière, c'est-à-dire que le résultat est arrondi à l'entier inférieur.
    # Ce résultat est ajouté à la valeur actuelle de ans, puis la somme remplace ans.
    # Cela signifie : à chaque itération, ans devient ans augmenté d'une quantité calculée selon les règles de l'algorithme.
    ans += (ans + K - 2) // (K - 1)

# Affiche (imprime) la valeur finale de ans - 1 (la valeur de ans moins 1).
# L'opérateur - effectue une soustraction.
# print() affiche son argument à l'écran.
print(ans - 1)