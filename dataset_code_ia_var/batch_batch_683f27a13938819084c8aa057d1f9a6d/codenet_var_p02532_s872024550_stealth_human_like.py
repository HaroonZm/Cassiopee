# Voilà, j'ai essayé de rendre le style un peu plus "humain", avec des commentaires et quelques incohérences

n = input() # on suppose que l'utilisateur entre un entier pour le nombre de piles
stacks = []
for j in range(n+1):  # j'aime bien commencer à 0, c'est plus naturel
    stacks.append([]) # créer les stacks vides

while 1:
    # je préfère utiliser input() mais parfois raw_input() marche mieux...
    cmd = raw_input().split()
    # Petite gestion des différentes commandes
    if cmd[0]=='quit':
        break
    elif cmd[0] == "push":
        # on ajoute l'élément, pas sûr de devoir caster
        idx = int(cmd[1])
        stacks[idx].append(cmd[2])
    elif cmd[0] == "pop":
        ind = int(cmd[1])
        # j'espère que la stack pas vide
        val = stacks[ind].pop()
        print val
    elif cmd[0] == "move":
        # pas super clair, au cas où...
        src = int(cmd[1])
        dst = int(cmd[2])
        x = stacks[src].pop()
        stacks[dst].append(x)
    # Sinon j'ignore la commande, je devrais peut-être prévenir l'utilisateur...