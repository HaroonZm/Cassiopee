# Demande à l'utilisateur de saisir une valeur entière et la stocke dans la variable n.
n = int(input())

# Crée une liste s contenant les entiers de 1 à 2n inclus (donc de 1 à 2*n).
# range(1, 2 * n + 1) génère les entiers de 1 jusqu'à (2*n), car le second argument n'est pas inclus.
s = [i for i in range(1, 2 * n + 1)]

# Demande à l'utilisateur combien d'opérations seront effectuées. 
# Convertit l'entrée utilisateur en entier et exécute la boucle for ce nombre de fois.
for _ in range(int(input())):
    # À chaque itération, demande un entier a à l'utilisateur et le stocke dans la variable a.
    a = int(input())
    # Si a est une valeur différente de 0 (autrement dit, si a est "vrai" en Python) :
    if a:
        # Effectue une rotation circulaire de la liste s vers la gauche de a positions.
        # s[a:] prend tous les éléments de l'index a jusqu'à la fin de la liste,
        # s[:a] prend les éléments du début de la liste jusqu'à l'index a (exclus).
        # Additionner ces deux listes réalise ainsi la rotation demandée.
        s = s[a:] + s[:a]
    else:
        # Si a vaut 0, effectue une opération de mélange spécial de la liste s.
        # Crée une nouvelle liste en prenant un élément de la première moitié,
        # puis un élément de la deuxième moitié, alternativement.
        # Plus précisément, pour chaque indice i allant de 0 à n-1,
        # puis pour j prenant la valeur 0 puis 1 :
        #   - Si j == 0 : prend s[i + 0*n] ==> s[i]
        #   - Si j == 1 : prend s[i + 1*n] ==> s[i + n]
        # Cela donne un "interleave" ou brassage parfait de deux moitiés de la liste.
        s = [s[i + n * j] for i in range(n) for j in [0, 1]]

# À la fin, affiche tous les éléments de la liste s, un par ligne.
# print(*s, sep='\n') utilise l'opérateur * pour "dépaqueter" la liste,
# envoyant chaque élément comme argument séparé à print, avec '\n' comme séparateur, 
# donc chaque élément est affiché sur sa propre ligne.
print(*s, sep='\n')