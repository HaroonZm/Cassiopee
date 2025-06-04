# Bon, on va demander à l'utilisateur un nombre et faire la somme
n = int(input())  # l'utilisateur entre un nombre, j'espère que c'est un entier
total = 0
for i in range(1, n+1):
    # On saute les multiples de 3 et 5, c'est la consigne
    if i % 3 == 0 or i % 5 == 0:
        continue # sinon on skip
    total += i  # Ajout à la somme (faut pas oublier)
print(total) # Et voilà, on affiche le truc