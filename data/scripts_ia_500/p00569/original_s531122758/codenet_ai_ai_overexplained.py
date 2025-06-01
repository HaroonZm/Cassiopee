N, K, L, *A = map(int, open(0).read().split())  # Lire les entrées de la standard input, transformer chaque élément en entier, et les affecter respectivement aux variables N, K, L, et à la liste A contenant le reste des éléments.

# Définition de la fonction solve qui prend un paramètre X. Elle renvoie un booléen indiquant si une certaine condition est satisfaite.
def solve(X):
    R = []  # Initialisation d'une liste vide R, qui va stocker les indices des éléments de A inférieurs ou égaux à X.
    res = 0  # Initialisation d'un compteur res à 0. Ce compteur va accumuler la somme des indices correspondants à une certaine condition.
    
    # Parcours de la liste A avec ses indices grâce à enumerate.
    for t, a in enumerate(A):
        # Condition pour vérifier si l'élément a est inférieur ou égal à la valeur X passée en paramètre.
        if a <= X:
            R.append(t)  # Si la condition est vraie, on ajoute l'indice t à la liste R.
        # Vérification si la taille actuelle de la liste R est au moins égale à K.
        if len(R) >= K:
            # Ajout à res de la valeur R[-K] + 1. R[-K] est l'indice k-ème dernier ajouté dans R, et on ajoute 1 pour convertir l'indice 0-based en 1-based.
            res += R[-K] + 1
    # La fonction renvoie True si res est supérieur ou égal à L, sinon False.
    return res >= L

# Initialisation des bornes pour la recherche binaire. 'left' commence à 0, 'right' à N.
left = 0
right = N

# Boucle de recherche binaire qui continue tant que la différence entre left et right est supérieure à 1.
while left + 1 < right:
    mid = (left + right) >> 1  # Calcul de la moyenne entre left et right en divisant par 2 avec un décalage binaire à droite (équivalent à (left + right) // 2).
    # Appel à la fonction solve avec mid comme argument.
    if solve(mid):
        # Si solve(mid) est True, on réduit la borne supérieure à mid.
        right = mid
    else:
        # Sinon, on augmente la borne inférieure à mid.
        left = mid

# Affichage de la valeur finale de right, qui correspond à la réponse finale déterminée par la recherche binaire.
print(right)