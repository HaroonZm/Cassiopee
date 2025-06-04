# Demander à l'utilisateur d'entrer un entier qui sera stocké dans 'n'
# 'n' représente le nombre d'éléments dans la liste 'a'
n = int(input())

# Demander à l'utilisateur d'entrer 'n' entiers séparés par des espaces
# 'input().split()' sépare la chaîne en une liste de chaînes sur les espaces
# 'map(int, ...)' convertit chaque chaîne en entier
# 'list(...)' rassemble les entiers dans une liste
a = list(map(int, input().split()))

# Demander un entier 'q' qui sera le nombre de requêtes posées par l'utilisateur
q = int(input())

# Créer une liste vide 'k' qui va contenir les requêtes
k = []

# Boucle 'for' pour itérer exactement 'q' fois, c’est-à-dire pour chaque requête
for i in range(q):
    # Lire un entier représentant la requête
    k1 = int(input())
    # Ajouter dans 'k' une sous-liste composée du nombre de la requête et de son index dans la liste des requêtes
    # Cela permet de garder l’ordre original des requêtes pour l’affichage final des résultats
    k.append([k1, i])

# Trier la liste 'a' en ordre croissant
a.sort()

# Trier la liste 'k' selon la valeur de la requête (qui est le premier élément de chaque sous-liste)
k.sort()

# Créer une liste 'ans' de longueur 'q' dont tous les éléments sont initialisés à 'n'
# 'ans[i]' enregistrera la réponse pour la i-ème requête, c’est-à-dire combien d’éléments de 'a' sont inférieurs ou égaux à la requête
ans = [n] * q

# Initialiser la variable 'i' à 0
# 'i' servira à parcourir la liste des requêtes 'k'
i = 0

# Initialiser la variable 'j' à 0
# 'j' servira à parcourir la liste triée 'a'
j = 0

# Boucle principale :
# On continue tant qu’il reste des requêtes à traiter ('i < q') et qu'il reste des éléments dans 'a' ('j < n')
while i < q and j < n:
    try:
        # Cette boucle interne fait avancer 'j' tant que la valeur de la requête 'k[i][0]' est strictement supérieure à 'a[j]'
        # Cela signifie que 'a[j]' est encore plus petit que la valeur recherchée
        # À chaque incrémentation, on cherche positionner 'j' pour être le premier indice où 'a[j]' n'est PAS strictement inférieur à 'k[i][0]'
        while k[i][0] > a[j]:
            j += 1
            # Si 'j' atteint ou dépasse la longueur de 'a' (c'est-à-dire 'j == n'), 'a[j]' va lancer une exception (IndexError) qui sera capturée
    except:
        # Ce bloc 'except' capture toutes les exceptions (notamment l'IndexError quand 'j' dépasse les bornes de 'a')
        # C’est utilisé ici car une fois que 'j' est hors index, la boucle doit s'arrêter
        pass

    # On place dans 'ans' pour la requête 'k[i]', à la position originelle 'k[i][1]', la valeur courante de 'j'
    # Ceci correspond au nombre d'éléments de 'a' strictement plus petits que la requête, ce qui est ce que la boucle ci-dessus a calculé
    ans[k[i][1]] = j

    # Passer à la requête suivante
    i += 1

# Boucle 'for' pour afficher la réponse pour chaque requête selon l’ordre d’entrée initial
for i in range(q):
    # Affiche la valeur correspondante à la i-ème requête dans 'ans'
    print(ans[i])