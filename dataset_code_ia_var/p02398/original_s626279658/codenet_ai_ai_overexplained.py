# Demande à l'utilisateur de saisir une ligne de texte, typiquement trois nombres séparés par des espaces
# Par exemple : "2 4 12"
# La fonction input() lit la saisie de l'utilisateur sous forme de chaîne de caractères (string)
# La méthode split() sépare cette chaîne en une liste de sous-chaînes selon les espaces (" "), permettant de récupérer chaque nombre individuellement
# La fonction map(int, ...) applique la fonction int (conversion en entier) à chaque élément de la liste obtenue, transformant ainsi les sous-chaînes en entiers
# Enfin, les trois valeurs sont affectées respectivement aux variables a, b et c grâce à l'opérateur de décomposition (unpacking)
a, b, c = map(int, input().split())

# Initialise une variable compteur nommée 'cnt' à 0
# Cette variable servira à compter le nombre d'entiers k pour lesquels c est divisible par k dans l'intervalle demandé
cnt = 0

# Utilise une boucle for pour itérer sur tous les entiers k compris entre a et b inclus
# La fonction range(a, b+1) génère une séquence d'entiers commençant à 'a' et s'arrêtant à 'b' inclus (car la borne supérieure de range est exclusive, on ajoute donc 1)
for k in range(a, b + 1):
    # Pour chaque valeur de k, vérifie si c est divisible par k sans reste
    # L'opérateur modulo (%) donne le reste de la division entière de c par k
    # Si le reste est égal à 0, cela signifie que k divise exactement c
    if c % k == 0:
        # Si la condition précédente est vraie (k est un diviseur de c), incrémente la variable cnt de 1 (c'est-à-dire augmente son ancienne valeur de 1)
        cnt += 1

# Affiche la valeur finale du compteur cnt, qui représente donc le nombre d'entiers k dans l'intervalle [a, b] qui divisent c sans reste
print(cnt)