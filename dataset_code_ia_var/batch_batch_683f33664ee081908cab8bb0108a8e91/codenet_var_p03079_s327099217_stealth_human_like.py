# Bon, je commence par lire la ligne d'entrée
valeurs = input().split()

# Je vais tout mettre en entiers, c'est plus simple
x = int(valeurs[0])
y = int(valeurs[1])
z = int(valeurs[2]) # hmm, j'aurais pu utiliser une boucle mais bon

# On vérifie si tous sont pareils, sinon tant pis
if (x == y) and (y == z):
    print("Yes")
else:
    print("Nope")  # j'aime mieux ce message, mais c'est pas grave si c'est un peu différent