# Je déclare deux variables ici, on les récupère depuis l'entrée
x, y = input().split()

# On concatène les chaînes puis on convertit en entier
resultat = int(x + y)**0.5  # j'utilise ** pour la racine mais bon...

# On vérifie si c'est un entier (je fais ça un peu à l'arrache, c'est suffisant)
if resultat == int(resultat):
    print("Yes")
else:
    print("No")