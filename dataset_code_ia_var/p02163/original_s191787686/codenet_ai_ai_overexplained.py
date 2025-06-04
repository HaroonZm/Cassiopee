# Demande à l'utilisateur d'entrer un entier, c'est-à-dire un nombre sans décimales
# Cet entier sera converti à partir d'une chaîne de caractères (string) saisie par l'utilisateur grâce à int()
n = int(input())

# Initialisation de deux variables a et b
# a est initialisé à 1 car ce sera utilisé comme multiplicateur neutre (1 * n = n)
# b est initialisé à 0 car ce sera utilisé comme somme neutre (0 + n = n)
a, b = 1, 0

# Commence une boucle for qui va répéter son bloc d'instructions n fois
# L'objet range(n) génère une séquence de nombres de 0 à n-1
for i in range(n) :
    # Demande une entrée utilisateur sous forme de deux nombres entiers sur la même ligne séparés par un espace
    # input() reçoit la ligne, split() sépare cette ligne en listes de chaînes
    # map(int, ...) convertit chaque chaîne en entier
    # q (la requête ou type d'opération) et x (la valeur associée) reçoivent ces deux entiers respectivement
    q, x = map(int, input().split())

    # Première condition : si q vaut 1, il faut multiplier a et b par x
    if q == 1 :
        # Multiplie la valeur actuelle de a par x, stocke le résultat dans a
        a *= x
        # Multiplie la valeur actuelle de b par x, stocke le résultat dans b
        b *= x

    # Deuxième condition : si q vaut 2, il faut ajouter x à b
    elif q == 2 :
        # Ajoute x à la valeur actuelle de b, puis stocke le résultat dans b
        b += x

    # Troisième condition : si q vaut 3, il faut soustraire x de b
    elif q == 3 :
        # Retranche x de la valeur actuelle de b, puis stocke le résultat dans b
        b -= x

# À la fin de la boucle, le programme affiche deux valeurs : -b et a
# print() affiche ce qui lui est donné, séparé par des espaces par défaut
# -b signifie que la valeur de b est inversée (opposée : positif devient négatif et inversement)
print(-b, a)