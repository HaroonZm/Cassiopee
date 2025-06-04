li=[]
for i in range(4):
    n = int(input())
    li.append(n)    # on ajoute chaque input à la liste

# un peu long mais tant pis, je fais simple
a = li[0] + li[2]
b = li[0] + li[3] # j'espère ne pas me tromper d'index !
c = li[1] + li[2]
d = li[1] + li[3]

#print(f"Possibles: {a}, {b}, {c}, {d}")
answer = min(a, b, c, d) # je prends le min
print(answer)