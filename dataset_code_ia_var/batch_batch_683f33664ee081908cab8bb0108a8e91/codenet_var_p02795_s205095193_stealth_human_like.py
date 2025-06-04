# Bon, je récupère les valeurs au début
h = int(input())
w = int(input())
n = int(input())

# Ca sert à rien mais je laisse
h = h
w = w

cnt=0
painted = 0
while painted < n:
    if w > h:
        cnt = cnt + 1
        painted = painted + w   # je peins la ligne la plus longue ?
        h = h - 1
    else:
        cnt+=1
        painted += h
        w = w - 1
# c'est fini, j'affiche le résultat ici
print(cnt)