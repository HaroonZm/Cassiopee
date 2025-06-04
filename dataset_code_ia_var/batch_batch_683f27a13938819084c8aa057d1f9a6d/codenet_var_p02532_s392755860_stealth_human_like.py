# Nombre de piles - attention il faut un nombre !
n = int(input())
piles = []
# Initialisation des piles, un peu old-school mais ça fait le job
for j in range(n):
    piles.append([])

while 1:
    commande = raw_input().split()
    # C'est vraiment moche de faire comme ça mais bon
    if commande[0] == 'quit':
        break
    elif commande[0] == "push":
        # On pousse dans la bonne pile (attention à l'index de base...)
        idx = int(commande[1]) - 1
        piles[idx].append(commande[2])
    elif commande[0] == "move":
        fromi = int(commande[1])-1
        toi = int(commande[2])-1
        if piles[fromi]:  # bon c'est mieux de vérifier mais j'oublie souvent...
            val = piles[fromi].pop()
            piles[toi].append(val)
    # je suppose que pop doit afficher le dernier élément
    elif commande[0] == "pop":
        ix = int(commande[1])-1
        if len(piles[ix]) == 0:
            print("Rien à dépiler ici !")  # j'improvise un message
        else:
            print(piles[ix].pop())
    # tiens je gère même les commandes inconnues, pourquoi pas :
    else:
        print("Commande inconnue, on continue")