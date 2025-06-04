# Demande à l'utilisateur de saisir une valeur via le clavier
# input() lit la saisie de l'utilisateur sous forme de chaîne de caractères (str)
# int() convertit cette chaîne en un entier (int)
# On assigne le résultat à la variable X
X = int(input())

# De la même manière, on demande une saisie pour la variable A
A = int(input())

# Idem pour la variable B
B = int(input())

# On soustrait la valeur A à la valeur X (X-A)
# Ensuite, on calcule le reste de la division entière de (X-A) par B avec l'opérateur modulo '%'
# L'opérateur modulo '%' donne le reste quand le dividende (ici X-A) est divisé par le diviseur (ici B)
# Par exemple, si (X-A) vaut 7 et B vaut 3, alors 7%3 donne 1 car 7 = 2*3 + 1
# La fonction print() affiche le résultat à l'écran
print((X - A) % B)