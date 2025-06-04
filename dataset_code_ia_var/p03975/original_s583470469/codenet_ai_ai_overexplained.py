# Demande à l'utilisateur une ligne d'entrée, qui contient trois entiers séparés par des espaces.
# input() capture toute la ligne de texte entrée par l'utilisateur sous forme de chaîne de caractères.
# split() découpe cette chaîne en une liste de sous-chaînes, chacune correspondant à un fragment séparé par un espace.
# Le générateur (int(i) for i in input().split()) convertit chaque sous-chaîne en un entier à l'aide de la fonction int().
# Les trois premiers (et seuls) éléments du générateur sont attribués respectivement aux variables N, A et B.
N, A, B = (int(i) for i in input().split())

# On va maintenant créer une liste, nommée 'a', contenant N entiers entrés par l'utilisateur.
# La compréhension de liste [int(input()) for i in range(N)] répète une opération N fois :
#   - range(N) crée un itérable de N nombres successifs à partir de 0 jusque N-1.
#   - À chaque itération, input() invite l'utilisateur à entrer une valeur, puis int() convertit cette valeur de chaîne en entier.
#   - L'entier obtenu à chaque itération est inséré dans la liste 'a'.
a = [int(input()) for i in range(N)]

# Déclare et initialise une variable compteur 'j' à la valeur 0.
# Cette variable servira à compter le nombre d'éléments qui respectent des conditions que l'on va déterminer ensuite.
j = 0

# Boucle for qui va parcourir la plage d'indices de la liste 'a', c'est-à-dire de 0 jusqu'à N-1 inclus.
for i in range(N):
    # Première condition : si l'élément à l'indice i dans la liste 'a' est strictement inférieur à A,
    # alors on incrémente la variable 'j' de 1. Cela permet de compter tous les éléments inférieurs à A.
    if a[i] < A:
        j += 1
    # Deuxième condition : si l'élément à l'indice i dans la liste 'a' est supérieur ou égal à B,
    # alors on incrémente également la variable 'j' de 1. Cela permet de compter tous les éléments
    # supérieurs ou égaux à B.
    # Le mot-clé 'elif' (abréviation de 'else if') indique que cette condition est vérifiée uniquement si la première n'est pas satisfaite.
    elif a[i] >= B:
        j += 1
    # Si aucune des deux conditions ci-dessus n'est vraie (c'est-à-dire A <= a[i] < B), rien ne se passe,
    # et la variable 'j' reste inchangée pour cette itération.

# À la fin de la boucle, la variable 'j' contient le nombre total d'éléments du tableau qui sont soit strictement
# inférieurs à A, soit supérieurs ou égaux à B.
# La fonction print(j) affiche la valeur de 'j' à l'écran.
print(j)