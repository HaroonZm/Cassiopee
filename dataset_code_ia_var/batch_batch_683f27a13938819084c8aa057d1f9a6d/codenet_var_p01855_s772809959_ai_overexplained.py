# Définition de la fonction gcd pour calculer le plus grand commun diviseur (PGCD) de deux entiers a et b
def gcd(a, b):
    # Si a est égal à zéro, cela signifie qu'il n'y a plus rien à diviser, donc on retourne b qui est le PGCD
    if a == 0:
        return b
    else:
        # Sinon, on rappelle la fonction gcd avec en premier argument le reste de la division de b par a
        # et en second argument a lui-même. Ceci est basé sur l'algorithme d'Euclide pour trouver le PGCD.
        return gcd(b % a, a)

# Lecture de l'entrée utilisateur, on s'attend à saisir un entier qui sera converti à l'aide de int()
t = int(input())  # Ceci lit une chaîne de caractères de la console et la convertit en entier

# On utilise une boucle while pour répéter le bloc de code qui suit 't' fois
while t:
    # On décrémente la valeur de t de 1 à chaque itération afin de finir la boucle après t tours
    t -= 1

    # Lecture d'une ligne de l'entrée standard, on suppose que cette ligne contient deux entiers séparés par un espace
    # La fonction input() lit la chaîne, split() découpe la chaîne en liste de sous-chaînes en utilisant l'espace comme séparateur,
    # puis map(int, ...) convertit chaque sous-chaîne en entier
    a, b = map(int, input().split())

    # On calcule le PGCD des deux nombres a et b en appelant la fonction gcd définie précédemment. Le résultat est stocké dans c
    c = gcd(a, b)

    # On divise a par le PGCD c à l'aide de la division entière //. Cela simplifie a et b au niveau de leur plus grand facteur commun
    a = a // c
    b = b // c

    # On commence l'analyse des cas avec une structure conditionnelle if/elif/else

    # Premier cas : si a et b sont égaux après réduction, on assigne 1 à ans1 et 0 à ans2
    if a == b:
        ans1 = 1
        ans2 = 0
    # Deuxième cas : si au moins l'un des deux nombres (a ou b) est pair (c'est-à-dire divisible par 2),
    # on assigne 1 à ans1 et 1 à ans2
    elif a % 2 == 0 or b % 2 == 0:
        ans1 = 1
        ans2 = 1
    # Dernier cas (le 'else') : cela signifie qu'a et b sont différents et tous deux impairs
    # On calcule a*b et on le divise par 2 (division entière //), puis on ajoute 1 à ans1
    # ans2 reçoit la valeur de a*b // 2 sans l'ajout
    else:
        ans1 = a * b // 2 + 1
        ans2 = a * b // 2

    # Affichage des résultats ans1 et ans2 à l'écran, séparés par un espace
    print(ans1, ans2)