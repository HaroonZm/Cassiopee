# Définition d'une constante m qui sera utilisée comme module pour éviter les débordements lors des calculs.
m = 10**9 + 7  # 10 puissance 9 plus 7, un nombre premier très utilisé pour le modulo dans les problèmes algorithmiques

# Attribution de la fonction built-in max (qui retourne la plus grande valeur parmi ses arguments) à la variable f.
f = max  # f est maintenant un alias pour la fonction max

# Attribution de la fonction built-in range (qui génère une séquence de nombres de 0 à n-1) à la variable r.
r = range  # r est maintenant un alias pour la fonction range

# Boucle principale qui s'exécute pour chaque jeu de données en fonction du nombre de cas de test fourni en entrée.
for _ in r(int(input())):  # int(input()) lit une ligne de l'entrée standard, la convertit en entier, qui devient le nombre de cas à traiter
    # Lecture de deux entiers sur une ligne, conversion en liste, tri pour garantir x <= y
    x, y = sorted(map(int, input().split()))  # .split() sépare la ligne, map(int, ...) convertit en int, sorted range du plus petit au plus grand, dépaquetage dans x et y

    # Initialisation de la variable s à -1. Elle servira à compter les étapes dans la boucle suivante.
    s = -1

    # Initialisation des variables i et j à 1.
    i = j = 1  # Types d'entiers, valeurs de départ pour générer une séquence similaire à Fibonacci

    # Boucle qui s'exécute tant que j ne dépasse pas x ET que i+j ne dépasse pas y.
    while j <= x and i + j <= y:
        # Mise à jour des variables i et j pour générer la séquence suivante (semblable à Fibonacci)
        temp = i  # Stockage temporaire de i
        i = j     # i prend la valeur de j
        j = temp + j  # j devient la somme de l'ancien i et de j

        # Incrémentation de s à chaque itération de la boucle
        s += 1

    # Condition spéciale : si x est égal à 1 ou y est strictement inférieur à 3
    if x == 1 or y < 3:
        # Affiche les résultats : 1 et (x*y modulo m)
        print(1, x * y % m)
    else:
        # Calcul d'une borne inférieure sur une quantité a, en utilisant la relation entre x, y, i et j
        # f(0, ...) assure que la valeur ne soit pas négative
        a = max(0, (y - j) // i + 1) + f(0, (x - j) // i + 1)

        # Réinitialisation de i et j pour une nouvelle séquence
        i = j = 1

        # Boucle s'exécutant s fois (s a été calculé auparavant)
        for c in r(s):  # c va de 0 à s-1

            # Calcul de nouvelles valeurs pour k et l à partir des valeurs courantes de i et j
            k = j                   # k reçoit la valeur de j
            l = i + j * 2           # l = i + 2*j

            # Boucle imbriquée s'exécutant s-c fois
            for _ in r(s - c):
                temp = k      # Stockage temporaire de k
                k = l         # k prend la valeur de l
                l = temp + l  # l devient la somme de l'ancien k et l

            # Si x au moins k, on incrémente a de la borne max relative à y-l via k
            if x >= k:
                a += f(0, (y - l) // k + 1)
            # Même principe, mais pour le cas symétrique y et x
            if y >= k:
                a += f(0, (x - l) // k + 1)

            # Mise à jour des valeurs i et j pour l'itération suivante, toujours dans la logique des suites similaires à Fibonacci
            temp = i
            i = j
            j = temp + j

        # Après la boucle, affichage du résultat final pour ce jeu de données
        print(s + 1, a % m)  # On ajoute 1 à s pour avoir le bon compte, puis a modulo m pour obtenir le résultat borné comme attendu