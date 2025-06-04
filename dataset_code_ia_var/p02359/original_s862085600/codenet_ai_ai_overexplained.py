# Demander à l'utilisateur d'entrer deux entiers séparés par un espace, puis stocker ceux-ci dans les variables n et t
# - n désigne le nombre d'intervalles à lire
# - t désigne la taille de la liste que nous allons manipuler
n, t = map(int, input().split(" "))

# Créer une liste appelée 'num' contenant t zéros. Ceci servira à compter les occurrences à chaque position.
# La compréhension de liste est utilisée ici : [0 for i in range(t)] veut dire "met 0 t fois en itérant de i=0 jusque t-1"
num = [0 for i in range(t)]

# Boucle principale qui va parcourir chaque intervalle donné parmi les n à lire
for i in range(n):
    # Lire deux entiers l et r pour chaque intervalle
    # Ceux-ci désignent les bornes de l'intervalle (gauche et droite)
    l, r = map(int, input().split(" "))
    # Incrémenter la valeur à l'indice l de la liste num de 1 pour marquer le début de la couverture de l'intervalle
    # Cela signifie que depuis cet indice, quelqu'un "rentre dans la zone couverte"
    num[l] += 1
    # Vérifier si la borne droite r est strictement inférieure à t (pour éviter une erreur d'indice hors limites)
    if r < t:
        # Décrémenter la valeur à l'indice r de la liste num de 1
        # Ceci marque la sortie de la zone couverte
        num[r] -= 1

# Deuxième boucle pour effectuer un calcul de somme partielle (cumulée)
# Elle commence à l'indice 1 (car l'indice 0 n'a pas d'élément précédent)
for i in range(1, t):
    # Ajouter à l'élément courant num[i] la valeur de l'élément précédent num[i-1]
    # Cela cumule les modifications, indiquant combien d'intervalles couvrent chaque position
    num[i] += num[i-1]

# Trouver la valeur maximale de la liste num après calcul des couvertures pour chaque position
# Cela donne le nombre maximal d'intervalles qui se chevauchent à une même position
print(max(num))  # Afficher ce maximum sur la sortie standard