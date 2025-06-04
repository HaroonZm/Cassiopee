# Lire trois entiers depuis l'entrée standard, séparés par des espaces, et les stocker respectivement dans N, A et B.
# L'expression (int(i) for i in input().split()) crée un générateur qui convertit chaque élément obtenu en divisant la chaîne par split() en entier.
N, A, B = (int(i) for i in input().split())

# Créer une liste h de taille N contenant uniquement des zéros.
# Cette liste servira à stocker des hauteurs (ou d'autres entrees) que nous lirons ensuite une par une.
h = [0] * N

# Pour chaque index de 0 à N-1 (ce qui signifie "pour chaque élément de la liste h"),
# lire une entrée de l'utilisateur, la convertir en entier, puis l'affecter à la position i de la liste h.
for i in range(N):
    h[i] = int(input())

# Déterminer la valeur maximale présente dans la liste h à l'aide de la fonction max(),
# et l'affecter à la variable hmax.
hmax = max(h)

# Mettre à jour la valeur de A en la remplaçant par la différence entre A et B.
# Cela signifie qu'à partir de ce moment, A contiendra le résultat de A moins B.
A = A - B

# Définir une fonction appelée func qui prend un argument k.
# Cette fonction vérifie si un certain critère est satisfait pour une valeur k donnée.
def func(k):
    # Créer une nouvelle liste hn où chaque élément est la hauteur originale (a)
    # diminuée de k multiplié par B. Cela modélise l'effet de k opérations de "B" sur chaque hauteur.
    hn = [a - k * B for a in h]
    # Initialiser un compteur appelé res à zéro.
    # Ce compteur servira à compter combien de fois nous devons effectuer une opération "A" supplémentaire.
    res = 0
    # Boucler sur chaque indice de 0 à N-1, c'est-à-dire sur toutes les hauteurs modifiées.
    for i in range(N):
        # Si, après avoir enlevé les k * B, la valeur hn[i] est toujours strictement positive,
        # cela signifie qu'on n'a pas encore complètement réduit cet élément à zéro ou moins.
        if hn[i] > 0:
            # Calculer le nombre d'opérations "A" supplémentaires nécessaires pour réduire hn[i] à zéro ou moins.
            # L'opération "-1" et "//A" permettent d'obtenir le plafond de la division hn[i]/A,
            # c'est-à-dire combien de fois A doit être soustrait à hn[i] pour atteindre zéro ou moins.
            res += (hn[i] - 1 + A) // A
    # La fonction retourne True si le nombre total d'opérations "A" additionnelles nécessaires (res)
    # ne dépasse pas k, sinon False.
    return res <= k

# Initialiser la borne inférieure (left) de la recherche binaire à zéro.
left = 0
# Initialiser la borne supérieure (right) de la recherche binaire à hmax//B + 1.
# Cela garantit que right sera strictement plus grand que n'importe quel k raisonnable.
right = hmax // B + 1

# Entrer dans une boucle qui va continuer indéfiniment jusqu'à ce qu'on la quitte avec break.
while True:
    # Vérifier si les deux bornes sont égales.
    # Lorsque left == right, cela signifie qu'on a trouvé la plus petite valeur de k satisfaisant la condition.
    if left == right:
        break
    # Calculer la valeur médiane (half) comme la moyenne entière de left et right.
    # Cela permet de diviser l'intervalle de recherche en deux (c'est la base de la recherche binaire).
    half = (left + right) // 2
    # Appeler la fonction func avec la valeur half.
    # Si func(half) est True, cela veut dire qu'il existe une solution avec k = half.
    if func(half):
        # Si une telle solution existe, on réduit l'intervalle supérieur (right = half)
        # car on cherche la plus petite valeur pour laquelle cela marche.
        right = half
    else:
        # Sinon, on avance le début de l'intervalle à half + 1,
        # car toutes les valeurs inférieures ou égales à half ne conviennent pas.
        left = half + 1

# À la sortie de la boucle, left contient la plus petite valeur de k pour laquelle func(k) est vrai.
# Afficher cette valeur sur une nouvelle ligne par l'instruction print.
print(left)