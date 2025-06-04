# Bon alors, on va commencer ici
liste = []  # Je crois qu'il faut une liste pour stocker les entrées
liste = list(map(int, input().split()))  # On prend l'input, ok

# Je récupère les valeurs
x = liste[0]
y = liste[1]
z = liste[2]

# Je me demande si c'est vraiment utile, mais allons-y
if x == y and y == z:
    print("Yes")
else:
    print('No')  # On mettra No si jamais c'est différent