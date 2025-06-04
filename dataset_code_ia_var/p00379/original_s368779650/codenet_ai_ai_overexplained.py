# Initialisation d'une liste vide qui va servir à stocker certains entiers calculés plus tard
list = []

# On lit trois entiers depuis l'entrée standard (l'utilisateur), séparés par des espaces
# map(int, ...) va convertir tous les éléments fournis par input().split() en entiers
# Ces entiers sont affectés respectivement aux variables a, n et s
a, n, s = map(int, input().split())

# Initialisation d'une autre liste vide appelée ans, qui servira à stocker les résultats finaux
ans = []

# On commence une boucle for, avec une variable i qui va de 1 à 10000 inclus (Python s'arrête avant la borne supérieure, donc on met 10001)
for i in range(1, 10001):
    # Pour chaque i, on calcule i à la puissance n (i**n)
    # On vérifie si ce résultat est inférieur ou égal à s
    if i**n <= s:
        # Si c'est vérifié, on ajoute (append) ce résultat (i**n) à la liste appelée 'list'
        list.append(i**n)

# On commence une nouvelle boucle for pour parcourir tous les éléments de la liste 'list'
for i in list:
    # On convertit l'entier courant i en une chaîne de caractères, stockée dans k
    # Cela signifie que chaque chiffre du nombre i est désormais un caractère de k
    k = str(i)

    # On initialise une variable d avec la valeur de 'a' (cette opération crée une copie locale du nombre a)
    d = a

    # On parcourt chaque caractère j dans la chaîne k (chaque j représente un chiffre individuel du nombre i)
    for j in k:
        # On ajoute l'entier correspondant au chiffre j à la variable d
        # int(j) convertit le caractère en entier, d += int(j) ajoute ce chiffre à la somme courante
        d += int(j)

    # À ce stade, d est égal à a + somme des chiffres de i
    # On élève d à la puissance n (d**n), puis on compare ce résultat à i
    if d**n == i:
        # Si l'égalité est vérifiée, on ajoute i à la liste des réponses (ans)
        ans.append(i)

# Enfin, on affiche sur la sortie standard la longueur de la liste ans, c'est-à-dire le nombre d'éléments trouvés répondant à la condition
print(len(ans))