# Demande à l'utilisateur de saisir un entier, puis convertit cette saisie (qui est une chaîne de caractères) en entier avec int()
s = int(input())

# Crée une liste (tableau) appelée "m" de taille 10 000 000 (10 puissance 7) avec uniquement des zéros. 
# Cette liste va servir de table pour mémoriser quels nombres ont déjà été observés dans la suite.
# Chaque index de la liste représente un nombre possible, la valeur à cet index indique s'il a été vu (1) ou non (0).
m = [0] * 10**7

# Marque le nombre initial s comme déjà vu en plaçant 1 à l'index s dans la liste m. Cela veut dire que s a été rencontré dans la suite.
m[s] = 1

# Initialise une variable "a" à 1, elle compte le nombre d'itérations effectuées dans la boucle. 
a = 1

# Commence une boucle infinie; elle continuera jusqu'à ce que le programme rencontre un "exit()" ou une interruption.
while True:
    # Incrémente la variable "a" de 1. Cela représente le passage à l'étape suivante de la suite.
    a += 1

    # Vérifie si le nombre courant s est pair.
    if s % 2 == 0:
        # Si s est pair, divise s par 2 en utilisant la division entière (//) afin d'obtenir un résultat entier.
        s //= 2
    else:
        # Si s est impair, applique la formule 3*s + 1 assignée à s selon la définition de la suite de Collatz.
        s = 3 * s + 1

    # Vérifie si le nombre s nouvellement calculé a déjà été rencontré auparavant.
    # Si c'est le cas (m[s] égal à 1), c'est qu'une boucle a été détectée dans la suite.
    if m[s] == 1:
        # Affiche la variable "a" qui représente le nombre d'étapes effectuées jusqu'à la répétition.
        print(a)
        # Quitte immédiatement le programme grâce à exit(), la boucle infinie se termine donc ici.
        exit()
    else:
        # Si le nombre s n'avait encore jamais été rencontré, on le marque comme vu
        # pour éviter de repasser dessus plus tard, en mettant 1 à l'index s de la liste m.
        m[s] = 1