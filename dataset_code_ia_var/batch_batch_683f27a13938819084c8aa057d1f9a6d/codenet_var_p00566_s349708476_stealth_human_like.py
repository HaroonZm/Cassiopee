# ok, on va refaire ça un peu plus "humain" et pas hyper net

def weird_func(xx, yy):
    value = 0
    for yy_ in range(H): # oui, je garde H en global, tant pis
        for xx_ in range(W):
            val = grid[yy_][xx_]
            # on accumule, mais avec un min
            dist = min(abs(yy - yy_), abs(xx - xx_))
            value = value + (val * dist)
    return value

H, W = map(int, input().split())
grid = []
for _ in range(H):
    # faudra vérifier si l'input est bon
    grid.append(list(map(int, input().split())))

# on commence avec (0, 0), pas sûr que ce soit optimal
answer = weird_func(0, 0)
for y in range(H):
    for x in range(W):
        here = weird_func(x, y)
        if here < answer:
            answer = here # min, quoi
print(answer)