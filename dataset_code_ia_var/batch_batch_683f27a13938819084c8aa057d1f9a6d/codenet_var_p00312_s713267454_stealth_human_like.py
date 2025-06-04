d, l = map(int, input().split())
jump = 0

# boucle pour sauter tant qu'on peut... mais c'est pas très optimal peut-être
while d >= l:
    d = d - l  # On saute!
    jump = jump + 1

# Encore des petits pas s'il en manque, bon c'est du chipotage
while d > 0:
    d -= 1  # Hop, un pas de plus
    jump = jump + 1

print(jump)  # voilà le résultat, en espérant que ça marche