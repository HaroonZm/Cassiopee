# Lecture d'un nombre entier N à partir de l'entrée standard de l'utilisateur
# int() convertit la chaîne lue par input() en un entier
N = int(input())

# Création d'une liste x contenant 55565 éléments initialisés à zéro
# L'opérateur * multiplie la liste [0] par 55565
# Cette liste servira à marquer les nombres composés (non premiers)
x = [0] * (55555 + 10)

# Initialisation d'une liste vide appelée ans qui contiendra la réponse finale
ans = []

# Boucle for allant de 2 à 55556 (non inclus)
# La fonction range(2, 55556) génère les entiers de 2 à 55555
for i in range(2, 55556):
    # Vérifie si x[i] est égal à 0 (donc i est encore non marqué, potentiellement premier)
    if x[i] == 0:
        # Stocke la valeur de i dans la variable t
        t = i
        # Tant que t est inférieur à 55556
        while t < 55556:
            # Marque x[t] comme 1 pour indiquer que t n'est pas premier (car multiple d'un nombre plus petit)
            x[t] = 1
            # Incrémente t de i pour passer au multiple suivant
            t += i
        # Vérifie si le reste de la division de i par 5 est égal à 1
        # Cela sélectionne uniquement les nombres premiers congrus à 1 modulo 5
        if i % 5 == 1:
            # Ajoute i à la liste ans (car i est un nombre premier de la forme 5k+1)
            ans.append(i)
            # Si la longueur de la liste ans atteint N (autant que demandé par l'utilisateur)
            if len(ans) == N:
                # Quitte la boucle for, car on a trouvé suffisamment de nombres
                break

# Affiche tous les éléments de la liste ans
# L'opérateur * permet de décompresser la liste pour imprimer chaque élément séparément sur une même ligne
print(*ans)