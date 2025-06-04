# Lecture de trois entiers depuis l'entrée standard (généralement la console).
# La fonction input() lit une ligne sous forme de chaîne de caractères (par exemple, "2 3 4").
# La méthode split() sépare la chaîne lue en une liste de sous-chaînes, selon les espaces (' ').
# map(int, ...) applique la fonction int à chaque élément de la liste retournée par split(), convertissant chaque sous-chaîne en un entier.
# Enfin, l'opérateur d'affectation multiple (N, M, C =) extrait les trois entiers de l'itérable retourné par map().
N, M, C = map(int, input().split())

# Lecture de M entiers depuis l'entrée standard.
# On applique la même logique que précédemment : input(), split(), puis map(int, ...), pour convertir chaque sous-chaîne en entier.
# Finalement, list(...) transforme le map en une liste d'entiers.
B = list(map(int, input().split()))

# Initialisation d'un compteur de résultats valides.
# Ce compteur commencera à 0 et s'incrémente à chaque fois qu'une certaine condition (voir plus loin) est vérifiée.
counter = 0

# Boucle for pour répéter une action N fois.
# La fonction range(N) génère une séquence d'entiers de 0 à N-1. 
# Ici, on n'utilise pas la variable i directement dans la boucle, on l'utilise seulement pour compter combien de fois on itère.
for i in range(N):
    # A chaque itération, lecture d'une ligne contenant M entiers.
    # Comme précédemment : on lit une ligne, on décompose la chaîne en M sous-chaînes puis on convertit chaque élément en entier, 
    # et on collecte les entiers dans une liste nommée A.
    A = list(map(int, input().split()))
    
    # Création d'une nouvelle liste 'mul' contenant le produit de chaque paire correspondante des listes A et B.
    # zip(A, B) crée un itérable de paires (a, b), où a provient de A et b de B, pour chaque élément à la même position dans les listes.
    # L'expression [a*b for a, b in zip(A, B)] parcourt chaque paire (a, b) et calcule leur produit.
    # mul est une liste dont chaque élément est a[i]*b[i] pour i de 0 à M-1.
    mul = [a*b for a, b in zip(A, B)]
    
    # Ajout de la constante C à la liste 'mul'.
    # La méthode append() ajoute l'élément C à la fin de la liste mul.
    mul.append(C)
    
    # Somme de tous les éléments de la liste 'mul'.
    # La fonction sum(...) additionne tous les éléments de la liste, y compris ceux issus du produit a*b et la constante C ajoutée à la fin.
    # Si ce total est strictement supérieur à 0, on considère que le critère est rempli.
    if sum(mul) > 0:
        # Incrémentation du compteur : on ajoute 1 à counter.
        counter += 1

# Affichage final du résultat.
# La fonction print() écrit la valeur courante du compteur à la sortie standard (généralement l'écran).
print(counter)