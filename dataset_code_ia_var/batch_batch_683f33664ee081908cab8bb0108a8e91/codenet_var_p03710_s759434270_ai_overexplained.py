# Déclaration et initialisation d'une variable nommée 'm'
# Cette variable va servir de modulateur pour les opérations modulo afin d'éviter des dépassements de capacité d'entiers
# 10**9 signifie "10 puissance 9", soit 1000000000, auquel on ajoute 7, donc m = 1000000007, un nombre premier fréquemment utilisé
m = 10 ** 9 + 7

# Définition d'une fonction anonyme (lambda) assignée à la variable 'f'
# Cette fonction prend un argument 'a', ainsi que deux variables globales 'l' et 'k'
# Elle calcule (a-l)//k+1, qui est la division entière de (a-l) par k à laquelle on ajoute 1, puis prend le maximum entre ce résultat et 0
# Cela garantit de ne jamais retourner de valeur négative
f = lambda a: max(0, (a - l) // k + 1)

# Attribution de la fonction range à la variable 'r' pour une utilisation ultérieure simplifiée
# 'r' permettra de créer des séquences d'entiers à la volée
r = range

# La boucle suivante permet de gérer plusieurs cas de test
# Pour chaque cas de test, une itération est effectuée
for _ in r(int(input())):  # Lecture du nombre de cas de test et itération de la boucle pour chaque entrée
    # Lecture et traitement des deux entiers donnés pour ce cas de test, avec un tri croissant
    # Cela garantit que x sera toujours inférieur ou égal à y
    x, y = sorted(map(int, input().split()))
    
    # Initialisation des variables avant l'entrée dans la première boucle while
    # s : Compteur, initialement à -1 (il sera incrémenté au début de chaque boucle while)
    # i, j, k, l : Toutes initialisées à 1, elles seront utilisées dans la génération de termes de suites
    s = -1
    i = j = k = l = 1
    
    # Première boucle while
    # Tant que l ne dépasse pas x ET que k + l ne dépasse pas y, on itère
    # Cette boucle cherche la plus grande valeur de 's' pour laquelle k et l respectent ces contraintes
    while l <= x and k + l <= y:
        # Mise à jour des valeurs comme dans une suite de Fibonacci
        k, l = l, k + l
        s += 1  # Incrémentation de s à chaque tour
    
    # Calcul initial de la valeur 'a' à partir des résultats de la boucle précédente
    # a est la somme de deux appels à la fonction f sur les valeurs x et y
    a = f(y) + f(x)
    
    # Boucle for pour parcourir une plage de longueur 's'
    # Pour chaque valeur de c de 0 à s-1:
    for c in r(s):
        # Mise à jour de k, l pour générer une valeur spécifique selon l'indice c
        k, l = j, i + j * 2  # Calcul personnalisé basé sur i et j
        
        # Boucle imbriquée pour continuer à avancer dans la suite selon la formule
        # Pour chaque valeur _ dans range(s - c):
        for _ in r(s - c):
            # Mise à jour des valeurs en mode suite de Fibonacci généralisée
            k, l = l, k + l
        
        # Si y est supérieur ou égal à k, on ajoute f(x) à a ; si x est supérieur ou égal à k, f(y) à a
        # Cela sert à accumuler le résultat en tenant compte des conditions
        a = a + (y >= k) * f(x) + (x >= k) * f(y)
        
        # Mise à jour de i et j pour la prochaine itération
        i, j = j, i + j
    
    # Enfin, en fonction des valeurs de x et y, on détermine la sortie à afficher
    if x < 2 or y < 3:
        # Cas particuliers : on affiche d'abord 1, puis le produit de x et y modulo m
        print(1, x * y % m)
    else:
        # Dans le cas général, on affiche s+1 suivi de a modulo m
        print(s + 1, a % m)