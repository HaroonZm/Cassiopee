# Demander à l'utilisateur de saisir un nombre entier depuis l'entrée standard
# La fonction input() lit une ligne de texte depuis l'entrée
# La fonction int() convertit la chaîne de caractères lue en un entier
N = int(input())

# Début d'une boucle for qui attribue à la variable h chacune des valeurs de 1 à 3500 inclus (puisque range va de 1 à 3501, car le deuxième argument est exclu)
for h in range(1,3501):
    # À l'intérieur de la première boucle, commencer une seconde boucle for qui attribue à n les valeurs de 1 à 3500 inclus
    for n in range(1,3501):
        # Calculer la valeur de p selon la formule donnée
        # Cette opération effectue des multiplications et des soustractions simples
        # On multiplie 4 par h puis par n, puis on soustrait N fois h et N fois n
        p = 4*h*n - N*h - N*n

        # Vérifier si la valeur calculée de p est inférieure ou égale à 0
        # Si c'est le cas, alors il n'est pas valable de continuer avec ce couple (h, n)
        if p <= 0:
            # continue passe à l'itération suivante de la boucle interne (celle sur n)
            continue
        else:
            # Si p est supérieur à 0, on vérifie si (h*n) est divisible par p sans reste
            # Le symbole % est l'opérateur modulo, qui retourne le reste de la division entière
            # Si le reste est nul, cela signifie que h*n est un multiple exact de p, donc la division tombera juste
            if (h*n) % p == 0:
                # On a trouvé une solution. On va afficher h, n et la valeur correspondante de w
                # str(h) convertit h en une chaîne de caractères pour pouvoir la concaténer avec d'autres chaînes
                # str(n) convertit n en chaîne de caractères également
                # (N*h*n)//p effectue la multiplication de N, h et n puis la division entière (//) par p
                # Cela correspond à calculer la valeur de w sous forme entière
                # Les chaînes associées sont séparées par un espace pour l'affichage
                print(str(h) + " " + str(n) + " " + str((N*h*n)//p))
                # Fin du programme car on a trouvé une solution; la fonction exit() termine le script immédiatement
                exit()