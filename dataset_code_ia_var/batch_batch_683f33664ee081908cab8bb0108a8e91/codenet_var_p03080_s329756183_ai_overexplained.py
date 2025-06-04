# Demande à l'utilisateur d'entrer une valeur entière (le nombre de caractères)
# La fonction input() lit une ligne saisie par l'utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne en un entier.
# La valeur entière ainsi obtenue est stockée dans la variable N.
N = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères.
# La chaîne saisie est stockée dans la variable S.
S = input()

# Initialise une variable R à 0.
# Cette variable va servir à compter le nombre de caractères 'R' dans la chaîne S.
R = 0

# Initialise une variable B à 0.
# Cette variable va servir à compter le nombre de caractères autres que 'R' (dans ce cas, on suppose 'B')
B = 0

# Commence une boucle for qui va parcourir chaque caractère individuel dans la chaîne S.
# La variable 'i' prendra successivement la valeur de chaque caractère.
for i in S:
    # Vérifie si le caractère actuel 'i' est égal à la lettre majuscule 'R'
    if i == "R":
        # Si c'est le cas, cela signifie que le caractère est un 'R'
        # On incrémente donc la variable R de 1 (R = R + 1)
        R += 1
    else:
        # Si ce n'est pas un 'R', alors on considère que c'est un 'B'
        # On incrémente donc la variable B de 1 (B = B + 1)
        B += 1

# Après la boucle, on compare les valeurs des variables R et B.
# Si le nombre de 'R' (stocké dans R) est strictement supérieur au nombre de 'B' (stocké dans B)
if R > B:
    # On affiche "Yes" à l'écran pour indiquer que les 'R' sont majoritaires.
    print("Yes")
else:
    # Si le nombre de 'B' est supérieur ou égal au nombre de 'R', on affiche "No".
    print("No")