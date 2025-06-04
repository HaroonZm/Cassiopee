# Demande une entrée à l'utilisateur, qui doit être trois entiers séparés par des espaces.
# Par exemple : "12 2 4"
# La fonction input() lit l'entrée au clavier sous forme de chaîne de caractères.
# La méthode split() découpe la chaîne en une liste en séparant les éléments selon les espaces.
# La fonction map(int, ...) convertit chaque élément de la liste (qui sont des chaînes) en un entier.
# Les trois entiers obtenus sont ensuite affectés respectivement aux variables H, A, et B à l'aide de l'affectation multiple.
H, A, B = map(int, input().split())

# Initialisation d'une variable nommée 'ans' à la valeur 0.
# Cette variable servira à compter le nombre d'entiers i pour lesquels H est divisible par i, où i est compris entre A et B inclus.
ans = 0

# Utilisation d'une boucle for pour itérer sur une séquence d'entiers.
# La fonction range(A, B+1) génère une séquence d'entiers débutant à A et se terminant à B inclusivement.
# En Python, range ne prend pas en compte la borne supérieure, c'est pour cela qu'on ajoute 1 à B pour que B soit inclus.
for i in range(A, B+1) :
    # À chaque itération, 'i' prend la valeur du nombre courant dans la plage [A, B].
    # On vérifie si H est divisible exactement par i, c'est-à-dire si le reste de la division de H par i vaut zéro.
    # L'opérateur % réalise l'opération modulo (calcul du reste de la division entière).
    if H % i == 0 :
        # Si la division de H par i ne laisse aucun reste, alors 'i' est un diviseur de H dans la plage considérée.
        # Dans ce cas, on incrémente la variable 'ans' de 1, en utilisant l'opérateur += qui ajoute 1 à sa valeur actuelle.
        ans += 1

# Après la boucle, la variable 'ans' contient le nombre total de diviseurs de H qui sont compris entre A et B inclusivement.
# On affiche la valeur de 'ans' à l'écran grâce à la fonction print().
print(ans)