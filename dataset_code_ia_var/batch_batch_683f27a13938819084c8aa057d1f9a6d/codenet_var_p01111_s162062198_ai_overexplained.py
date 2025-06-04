# Début d'une boucle infinie
while True:
    # Lecture d'une entrée utilisateur depuis la console, attend que l'utilisateur tape un nombre et appuie sur "Entrée"
    # La fonction input() renvoie une chaîne de caractères, donc on utilise int() pour convertir cette chaîne en entier
    b = int(input())
    # Si l'utilisateur entre la valeur 0, alors on sort de la boucle avec break
    if b == 0:
        break
    # Calcul de x qui vaut le double de b
    x = b * 2
    # La boucle for va itérer sur la valeur de k, en décrémentant de 1 à chaque tour
    # On commence à int(x ** (1 / 2)), c'est-à-dire la partie entière de la racine carrée de x
    # On s'arrête à 0 (non compris), donc on prend les valeurs k = racine_carrée_int_vers_le_bas(x), ..., 3, 2, 1
    for k in range(int(x ** (1 / 2)), 0, -1):
        # On vérifie si k est un diviseur de x, c'est-à-dire si x modulo k vaut 0 (si la division euclidienne de x par k donne reste 0)
        if x % k == 0:
            # Calcul de (-k + 1 + (x // k)), où x // k est la division entière de x par k
            # Puis, on vérifie si ce résultat est un nombre pair (le test modulo 2 doit être nul)
            if (-k + 1 + (x // k)) % 2 == 0:
                # Calcul de a, qui est la valeur entière de (-k + 1 + x // k) divisée par 2
                a = (-k + 1 + x // k) // 2
                # On vérifie que a est strictement positif (supérieur à 0)
                if a > 0:
                    # Affichage des valeurs a et k sur la même ligne, séparées par un espace
                    print(a, k)
                    # On arrête la boucle for prématurément avec break, ce qui fait qu'on n'essaiera pas de plus petites valeurs de k
                    break