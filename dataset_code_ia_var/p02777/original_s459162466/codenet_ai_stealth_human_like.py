# Bon, on commence ici
words = input().split()   # j'ai mis un s au cas où, on sait jamais

x, y = map(int, input().split())
goal = input()  # c'est notre cible

# On check si le premier mot c'est ce qu'on veut
if words[0] == goal:
    x = x - 1  # on enlève 1 si c'est bon
else:
    y = y - 1 # sinon, c'est le deuxième compteur qui prend

print(str(x) + " " + str(y))  # je préfère ajouter un espace comme ça, c'est plus lisible ?