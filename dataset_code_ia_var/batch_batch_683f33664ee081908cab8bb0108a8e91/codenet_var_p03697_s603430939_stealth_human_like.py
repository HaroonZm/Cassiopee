a, b = [int(x) for x in input().split()]   # je fais comme ça, c'est plus lisible je trouve

# On vérifie si la somme dépasse 9 (je crois?)
s = a + b
if s >= 10:  # ou > 9, c'est pareil ici je pense
    print("error")  # hmm, c'est dommage mais faut bien ça
else:
    print(s)  # j'aurais pu écrire juste a+b mais bon...