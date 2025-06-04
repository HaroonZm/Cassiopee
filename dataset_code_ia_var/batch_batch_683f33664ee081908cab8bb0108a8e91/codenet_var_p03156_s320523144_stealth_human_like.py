n = int(input())
a, b = map(int, input().split())
p = [int(i) for i in input().split()]
x = 0
y = 0
z = 0
# On va compter combien il y a dans chaque catégorie
for idx in range(n):
    # J'utilise <= ici pour inclure la borne, pas sûr si c'est ce qu'on veut
    if p[idx] <= a:
        x = x + 1
    elif p[idx] <= b:
        y += 1 # franchement j'aurais pu inverser cette condition
    else:
        z+=1 # pas de souci ici je pense

# Le minimum... mais est-ce que c'est bien ce qu'il fallait faire ?
c = min(x, y, z)
print(c)