# Définition de la fonction era qui génère la liste des nombres premiers inférieurs ou égaux à n
def era(n):
    # Création d'une liste "table" de taille n+1, initialisée à 0
    # table[i] sera utilisé pour indiquer si i est un nombre composé (non premier)
    # 0 signifie "a priori premier", 1 signifie "composé"
    table = [0] * (n + 1)
    # Création d'une liste vide "prime_list" pour stocker les nombres premiers trouvés
    prime_list = []
    
    # Parcours de tous les entiers i de 2 à n inclus (car 0 et 1 ne sont pas premiers)
    for i in range(2, n + 1):
        # Si table[i] vaut 0, cela signifie que i n'a pas été marqué comme composé
        # donc c'est un nombre premier
        if table[i] == 0:
            # On ajoute i à la liste des nombres premiers
            prime_list.append(i)
            # On marque tous les multiples de i (à partir de 2*i) comme composés
            # La boucle commence à 2*i, s'arrête à n inclus, en avançant de i à chaque itération
            for j in range(2*i, n + 1, i):
                # table[j] passe à 1 (non premier)
                table[j] = 1
    # On retourne la liste des nombres premiers trouvés
    return prime_list

# Définition de la fonction f, qui compte le nombre d'éléments dans la liste data
# tels que leur deuxième élément (stocké à l'indice 1 de la sous-liste) est supérieur ou égal à n-1
def f(n):
    # Initialisation d'un compteur à zéro
    cnt = 0
    # Parcours de chaque élément i de la liste data
    for i in data:
        # Si le deuxième élément de la liste i (c'est-à-dire i[1])
        # est supérieur ou égal à n-1, alors on incrémente le compteur cnt de 1
        if i[1] >= n-1:
            cnt += 1
    # On retourne la valeur finale du compteur
    return cnt

# Lecture d'un entier N depuis l'entrée standard (utilisateur)
N = int(input())
# Appel de la fonction era pour obtenir la liste des nombres premiers inférieurs ou égaux à N
s = era(N)
# Initialisation de la liste "data" à vide
data = []

# Parcours de tous les nombres premiers i dans la liste s
for i in s:
    # On commence avec k égal à i (le premier nombre premier en cours)
    k = i
    # Initialisation du compteur c à zéro
    c = 0
    # Tant que la division entière de N par k est supérieure ou égale à 1
    # (c'est-à-dire que k ne dépasse pas N)
    while N // k >= 1:
        # On ajoute à c la partie entière de N divisé par k
        # Cela compte combien de fois k (puissances successives de i) apparaît dans la décomposition en facteurs premiers des entiers 1..N
        c += N // k
        # On fait passer k à la puissance suivante de i (k = k*i)
        k = k * i
    # Après avoir compté les occurrences de i dans la décomposition en facteurs premiers de N!
    # On ajoute la paire [i, c] à la liste data
    data.append([i, c])

# Calcul final demandé dans la consigne, puis affichage du résultat : 
# Il s'agit de combiner les différents résultats de la fonction f
# selon les combinaisons suivantes :
# f(75) : compte les nombres premiers dont la multiplicité est au moins 74 (équivalent à avoir un exposant >= 74)
# f(15) * (f(5) - 1) : nombre de façons de choisir un nombre premier avec exposant >= 14, et un autre distinct avec exposant >= 4
# f(25) * (f(3) - 1) : nombre de façons de choisir un nombre premier avec exposant >= 24, et un autre distinct avec exposant >= 2
# f(5) * (f(5) - 1) * (f(3) - 2) // 2 : nombre de façons de choisir trois nombres premiers distincts,
# deux avec exposant >= 4, un autre avec exposant >= 2. La division par 2 évite de compter deux fois la même combinaison.
print(
    f(75)
    + f(15) * (f(5) - 1)
    + f(25) * (f(3) - 1)
    + f(5) * (f(5) - 1) * (f(3) - 2) // 2
)