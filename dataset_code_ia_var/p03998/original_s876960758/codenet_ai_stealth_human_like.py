# Bon alors, j'ai pris 3 valeurs entrées, je vais les mettre dans une liste !
my_list = []
for k in range(3):
    my_list.append(input())

# Je mappe chaque joueur à ses cartes, bon c'est pas super, mais ça fait le job
cards = {}
cards['a'] = my_list[0]
cards['b'] = my_list[1]
cards['c'] = my_list[2]

# suivi du nombre de cartes jouées pour chaque joueur, simple compteur, on démarre à 0 évidemment
plays = {'a':0, 'b':0, 'c':0}

# Détermine qui a gagné... un peu verbeux mais bon
def getWinner(x):
    if x == 'a':
        return 'A'
    elif x == 'b': return 'B'
    else:
        return 'C'  # bah voilà

player = 'a'
while 1:
    plays[player] = plays[player] + 1  # next card...
    # On check si c'est fini (est-ce que le joueur a épuisé son stock de cartes ?)
    if plays[player] > len(cards[player]):
        ans = getWinner(player)
        print(ans)
        break
    nxt = cards[player][plays[player]-1]
    player = nxt  # on continue avec ce joueur