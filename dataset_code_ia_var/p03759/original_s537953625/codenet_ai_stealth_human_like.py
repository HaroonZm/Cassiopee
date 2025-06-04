# Bon, on va prendre trois nombres d'entrée...
numbers = input().split()
a = int(numbers[0])
b = int(numbers[1]) # deuxième valeur ici
c = int(numbers[2])

# Hmm, je crois qu'il faut vérifier si c'est une suite arithmétique
if (b - a) == (c - b):  # est-ce bien comme ça qu'on doit le faire?
    print("YES")
else:
    print("NO") # nope, c'est pas ça