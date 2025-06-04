# Demande deux entrées à l'utilisateur, séparées par un espace, et les convertit en entiers :
# La première valeur représente le nombre total d'éléments (N)
# La deuxième valeur représente le nombre d'éléments à exclure (K)
N, K = map(int, input().split())

# Demande une deuxième entrée de l'utilisateur représentant les hauteurs.
# Divise la chaîne entrée en une liste de chaînes, puis convertit chaque élément de cette liste en entier.
# Place le résultat dans une liste nommée 'H'
H = list(map(int, input().split()))

# Vérifie si le nombre total d'éléments (N) est inférieur ou égal au nombre d'éléments à exclure (K)
if N <= K:
    # Si c'est le cas, cela signifie qu'il n'y a aucun élément à considérer ou qu'ils sont tous exclus
    # Affiche "0" à l'écran
    print("0")
    # Quitte le programme immédiatement sans exécuter les instructions suivantes
    exit()

# Initialise une variable pour stocker la réponse finale. Elle est mise à zéro car on va additionner dessus.
ans = 0

# Définition d'une fonction 'quicksort' permettant de trier une liste d'entiers 'a' par ordre croissant.
def quicksort(a):
    # Convertit la liste en un ensemble (set) pour éliminer les doublons, puis vérifie sa taille.
    # Si la taille de l'ensemble est inférieure à 2, cela signifie que tous les éléments sont identiques,
    # ou que la liste est vide ou a un seul élément. La liste triée est donc identique à la liste d'origine.
    if len(set(a)) < 2:
        return a
    # Crée une liste vide qui contiendra les éléments inférieurs ou égaux au pivot. Elle s'appelle 'left'
    left = []
    # Le pivot (élément de référence) est choisi comme étant le premier élément de la liste ; on l'enlève de la liste originale.
    center = a.pop(0)
    # Crée une autre liste vide pour stocker les éléments strictement supérieurs au pivot. Celle-ci s'appelle 'right'
    right = []
    # Parcourt chaque élément restant dans la liste
    for i in a:
        # Si l'élément courant est strictement supérieur au pivot,
        if i > center:
            # Ajoute l'élément à la liste 'right'
            right.append(i)
        else:
            # Sinon (c'est-à-dire inférieur ou égal), ajoute l'élément à la liste 'left'
            left.append(i)
    # Trie récursivement la liste 'left'
    left = quicksort(left)
    # Trie récursivement la liste 'right'
    right = quicksort(right)
    # Ajoute le pivot à la fin de la liste triée 'left'
    left.append(center)
    # Ajoute (concatène) toute la liste triée 'right' à la suite de 'left'
    left.extend(right)
    # Retourne la liste triée (qui combine left, center, et right)
    return left

# Trie la liste H grâce à notre fonction de tri personnalisé 'quicksort'
# Après cette étape, H contient les mêmes éléments que précédemment mais rangés par ordre croissant
H = quicksort(H)

# Parcourt les N-K premiers éléments de la liste H triée (c'est-à-dire les plus petits éléments)
for i in range(N-K):
    # Ajoute la valeur de chaque élément à la variable de réponse 'ans'
    ans += H[i]

# Affiche le résultat final, qui est la somme des N-K plus petits éléments de la liste H
print(ans)