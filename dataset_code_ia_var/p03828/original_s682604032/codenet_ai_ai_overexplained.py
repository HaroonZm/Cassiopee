import sys  # Importe le module système, qui permet d'interagir avec l'environnement du programme

# Redéfinit la fonction input pour qu'elle lise une ligne depuis l'entrée standard (clavier ou fichier)
input = sys.stdin.readline

# Lit une ligne depuis l'entrée standard, enlève le caractère de fin de ligne, convertit en entier et stocke dans la variable n
n = int(input())

# Définit une constante INF qui vaut 10 puissance 9 plus 7 (un grand nombre premier utilisé pour le modulo afin d'éviter les gros entiers)
INF = 10 ** 9 + 7

# Crée une liste appelée Num de taille n+1, initialisée avec des zéros. Cette liste servira à compter les exposants des facteurs premiers.
Num = [0] * (n + 1)

# Cette boucle va de 2 à n inclus. Elle va analyser chaque nombre x dans cette plage.
for x in range(2, n + 1):
    i = 2  # Initialise le diviseur i à 2 (plus petit nombre premier)
    # Tant que i*2 est inférieur ou égal à x, on peut encore essayer de diviser x par des petits nombres
    while i * 2 <= x:
        # Cette boucle while interne divise x par i autant de fois que possible tant que c'est divisible (i est un diviseur)
        while x % i == 0:
            # x est divisible par i, donc on divise x par i (c'est l'opération de factorisation)
            x = x // i  # Met à jour x en lui assignant le résultat de la division entière par i
            # On augmente le nombre d'occurrences du facteur premier i dans Num
            Num[i] += 1
        # Passe au diviseur suivant
        i = i + 1
    # Si, à la fin de l'analyse, il reste une valeur de x différente de 1,
    # cela signifie que x est soit un nombre premier ou supérieur à la moitié de sa valeur initiale
    if not x == 1:  # Vérifie si le x restant est différent de 1
        # On considère que x est premier et on enregistre une occurrence de ce facteur dans Num
        Num[x] += 1

# Initialise la variable ans à 1. Elle servira à stocker le résultat final.
ans = 1

# Parcourt chaque élément i dans la liste Num.
for i in Num:
    # Multiplie ans par (i + 1), puis applique le modulo INF pour éviter de dépasser la capacité d'un entier
    ans = (ans * (i + 1)) % INF

# Affiche le résultat final à l'écran
print(ans)