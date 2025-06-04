# Demande à l'utilisateur de saisir une valeur entière et stocke cette valeur dans la variable N.
# La fonction input() attend l'entrée utilisateur sous forme de texte (chaîne de caractères).
# La fonction int() convertit la chaîne de caractères en un nombre entier (integer).
N = int(input())

# Initialise la variable w à 0. w va servir à stocker la valeur trouvée plus tard dans le programme.
w = 0

# Boucle for pour parcourir toutes les valeurs possibles de h.
# La fonction range(1, 3501) crée une séquence de nombres de 1 à 3500 inclus.
# Cela signifie que h va prendre toutes les valeurs entières de 1 à 3500, une par une.
for h in range(1, 3501):
    # Boucle for imbriquée pour parcourir toutes les valeurs possibles de n.
    # La fonction range(h, 3501) crée une séquence de nombres allant de la valeur actuelle de h à 3500 inclus.
    # Cela garantit que n est toujours supérieur ou égal à h pour éviter les doublons et respecter les contraintes du problème.
    for n in range(h, 3501):
        # La ligne suivante contient une condition if complexe :
        # Première partie : 4*h*n > N*(h+n) 
        #   - Cette condition vérifie que le produit de 4, de h et de n est strictement plus grand que le produit de N et de (h+n).
        # Deuxième partie : N*h*n % (4*h*n - N*(h+n)) == 0
        #   - Cette partie vérifie que (4*h*n - N*(h+n)) divise exactement N*h*n, c'est-à-dire que le reste de la division est nul.
        #   - L'opérateur % représente le calcul du reste (modulo) en Python.
        if 4 * h * n > N * (h + n) and N * h * n % (4 * h * n - N * (h + n)) == 0:
            # Si les deux conditions précédentes sont remplies, on calcule la valeur de w.
            # w est égal au quotient entier (division entière) de N*h*n par (4*h*n - N*(h+n)).
            # L'opérateur // effectue une division entière : il retourne seulement la partie entière du quotient.
            w = N * h * n // (4 * h * n - N * (h + n))
            # On quitte la boucle for la plus interne (celle de n) prématurément grâce au mot-clé break.
            # Cela signifie que puisque nous avons trouvé une solution, il n'est pas nécessaire de tester les autres valeurs de n pour ce h.
            break
    # Cette condition vérifie si w est strictement supérieur à 0, ce qui veut dire qu'une solution a été trouvée à l'intérieur de la boucle précédente.
    if w > 0:
        # On quitte la boucle for externe (celle de h) dès qu'une solution satisfaisante a été trouvée.
        break

# Affiche les valeurs de h, n et w trouvées, séparées par des espaces.
# La fonction print() affiche ses arguments à l'écran.
print(h, n, w)