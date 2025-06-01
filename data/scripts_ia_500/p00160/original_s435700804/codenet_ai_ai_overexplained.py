# Boucle infinie : elle continuera à s'exécuter indéfiniment jusqu'à ce qu'une condition explicite mette fin à cette boucle
while 1:
    # Lecture d'une valeur entière depuis l'entrée standard avec input() convertie en int
    # Cette valeur sera stockée dans la variable 'n'
    # Initialisation de la variable 'v' à 0, qui servira à accumuler une valeur totale
    n, v = int(input()), 0

    # Condition qui vérifie si la valeur saisie est 0
    # Si n vaut 0, on quitte la boucle avec break
    if n == 0:
        break

    # Boucle for exécutée 'n' fois avec une variable temporaire '_' qui signifie que cette variable n'est pas utilisée
    for _ in range(n):
        # Lecture d'une ligne depuis l'entrée standard, contenant 4 nombres séparés par des espaces
        # Ces nombres sont convertis en entiers et assignés aux variables x, y, h, w simultanément
        x, y, h, w = map(int, input().split())

        # Modification de la variable x en lui affectant la somme de x, y, et h
        x = x + y + h

        # Série de conditions if ... elif qui contrôlent la valeur de x et w pour augmenter v
        # Ces conditions sont exclusives grâce à elif : une seule pourra être exécutée par itération
        if x < 61 and w < 3:
            v += 600  # Si x est strictement inférieur à 61 et w strictement inférieur à 3, v est incrémenté de 600
        elif x < 81 and w < 6:
            v += 800  # Si la première condition est fausse, mais que x < 81 et w < 6, on ajoute 800 à v
        elif x < 101 and w < 11:
            v += 1000  # Si les conditions précédentes sont fausses et que celle-ci est vraie, on ajoute 1000 à v
        elif x < 121 and w < 16:
            v += 1200  # Ajoute 1200 si x < 121 et w < 16
        elif x < 141 and w < 21:
            v += 1400  # Ajoute 1400 si x < 141 et w < 21
        elif x < 161 and w < 26:
            v += 1600  # Ajoute 1600 si x < 161 et w < 26

    # Affichage de la valeur finale de v après avoir traitée les 'n' entrées
    print(v)