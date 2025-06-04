import math  # Importe le module math pour utiliser ses fonctions, même si ici il n'est pas utilisé

# Prend l'entrée de l'utilisateur sous forme de chaîne, puis coupe cette chaîne en trois morceaux avec split(),
# ensuite applique int() à chaque morceau avec map() pour avoir trois entiers.
# Ces entiers sont affectés respectivement aux variables A, B et X
A, B, X = map(int, input().split())

# Vérifie si la valeur de A est strictement inférieure à la valeur de B
if A < B:
    # Si c'est le cas, effectue un calcul particulier :
    # -(-X//1000) effectue une division entière de X par 1000 en arrondissant toujours vers le haut
    # Exemple : X=1500 => 1500/1000=1.5, mais -(-1500//1000)=2
    # Ensuite on multiplie ce résultat entier par A
    resultat = A * (-(-X // 1000))
    # Affiche le résultat calculé à l'écran
    print(resultat)

# Si la première condition n'est pas vraie, on vérifie si A est strictement inférieur à 2*B
elif A < 2 * B:
    # Effectue une division entière de X par 1000, résultat arrondi vers le bas
    # Exemple : X=1500 => 1500//1000 = 1
    quotient = X // 1000
    # Multiplie ce quotient par A pour obtenir la valeur de base de C
    C = A * quotient

    # Vérifie si le reste de la division de X par 1000 (c’est-à-dire le X modulo 1000) est égal à zéro,
    # ce qui signifie que X est un multiple de 1000 et qu'il n'y a pas de "reste"
    if X % 1000 == 0:
        pass  # Ne fait rien, car il n'y a pas de reste à traiter

    # Si le reste est différent de zéro et est inférieur ou égal à 500
    elif X % 1000 <= 500:
        # Ajoute le coût B à C pour traiter ce reste de 1000 unités ou moins
        C += B

    # Si le reste de la division vaut plus que 500
    else:
        # Ajoute le coût A à C, car c'est plus avantageux dans ce cas
        C += A

    # Affiche la valeur finale de C
    print(C)

# Si aucune des conditions précédentes n'est vraie, alors A >= 2*B
else:
    # -(-X//500) effectue une division entière de X par 500 tout en arrondissant vers le haut
    # Cela permet de savoir combien de "blocs" de 500 il y a dans X (même s'il y a un reste, on en compte un de plus)
    # On multiplie ce résultat par B 
    resultat = B * (-(-X // 500))
    # Affiche le résultat calculé
    print(resultat)