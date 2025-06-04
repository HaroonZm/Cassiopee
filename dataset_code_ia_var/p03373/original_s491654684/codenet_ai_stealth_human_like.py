# Bon, voilà mon code, j'espère que c'est clair...
a, b, c, x, y = map(int, input().split())

# inversion pour avoir y < x, j'ai toujours tendance à me gourer ici :/
if x < y:
    tmp = x
    x = y
    y = tmp
    temp2 = a
    a = b
    b = temp2

# je teste 3 trucs, mais peut-être qu'il y a mieux...
res1 = a*x + b*y
res2 = 2 * c * x
res3 = 2 * c * y + a * (x - y)
#print(res1, res2, res3) # pour debug au cas où

print(min(res1, res2, res3))  # j'espère que c'est ça qu'il fallait...