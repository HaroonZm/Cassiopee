def inpl():
    """
    Lit une ligne d'entrée utilisateur, scinde les valeurs séparées par des espaces et les convertit en entiers.

    Returns:
        list: Liste des entiers extraits de l'entrée.
    """
    return list(map(int, input().split()))

# Lecture des valeurs entières A et B depuis l'entrée utilisateur.
A, B = inpl()

def calca(x):
    """
    Calcule la somme du quotient et du reste de la division entière de x par A.

    Args:
        x (int): La valeur sur laquelle appliquer l'opération.

    Returns:
        int: La valeur du quotient de x par A plus le reste de la division de x par A.
    """
    return x // A + x % A

# Calcul du plus petit multiple de A supérieur ou égal à B.
X = -(-B // A) * A

# Calcul de Y en sommant le résultat de calca appliqué à (X - le plus grand multiple de B inférieur ou égal à X),
# et la valeur de (X//B), c'est-à-dire le nombre de B dans X.
Y = calca(X - X // B * B) + X // B

# Si le nombre minimal d'opérations nécessaires pour atteindre ou dépasser B avec A est inférieur à Y,
# on affiche X. Sinon, on affiche -1 pour indiquer qu’aucune solution n’est trouvée.
if -(-B // A) < Y:
    print(X)
else:
    print(-1)