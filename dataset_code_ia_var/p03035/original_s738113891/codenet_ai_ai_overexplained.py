# Demande à l'utilisateur de saisir deux valeurs séparées par un espace.
# input() lit la saisie de l'utilisateur sous forme de chaîne de caractères (string).
# split() sépare cette chaîne en une liste de deux éléments grâce à l'espace (" ") comme séparateur.
# map(int, ...) applique la fonction int() à chaque élément de cette liste pour les convertir en entiers.
# Enfin, les deux entiers sont stockés dans les variables A et B respectivement grâce à l'affectation multiple.
A, B = map(int, input().split())

# Ici, nous utilisons une instruction conditionnelle pour contrôler le flux du programme selon la valeur de A.
# La première condition vérifie si la valeur de A est supérieure ou égale à 13 à l'aide de l'opérateur de comparaison ">=".
if A >= 13:
    # Si A est supérieur ou égal à 13, on affiche la valeur entière de B.
    # int(B) s'assure que B est bien de type entier, même si ce n'est pas strictement nécessaire ici car B est déjà un entier.
    # print() affiche la valeur sur la sortie standard (écran du terminal).
    print(int(B))
# La clause elif permet de tester une seconde condition si la première n'est pas vérifiée.
# Ici, on vérifie que la valeur de A est comprise entre 6 et 12 inclusivement.
# L'opérateur logique "<=" permet de spécifier une plage de valeurs: 6 <= A <= 12 signifie "A est supérieur ou égal à 6 ET A est inférieur ou égal à 12".
elif 6 <= A <= 12:
    # Si A est compris entre 6 et 12, on affiche la moitié de B (B divisé par 2).
    # L'opération B/2 retourne un nombre à virgule flottante.
    # int(B/2) convertit ce résultat en entier, ce qui tronque la partie décimale.
    print(int(B/2))
# La clause else capture tous les cas non couverts par les if et elif précédents.
# Ici, cela signifie que A est inférieur à 6.
else:
    # Si A est strictement inférieur à 6, on affiche la chaîne de caractères "0".
    # Les guillemets indiquent qu'il s'agit d'une chaîne de caractères, et non d'un nombre.
    print("0")