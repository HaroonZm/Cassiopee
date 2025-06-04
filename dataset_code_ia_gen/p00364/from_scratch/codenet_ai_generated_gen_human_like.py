N, t = map(int, input().split())
buildings = [tuple(map(int, input().split())) for _ in range(N)]

# On cherche la hauteur minimale h du sommet de la tour à t
# tel que la ligne de vue du sommet à la base du donjon (x=0, h=0)
# n'intersecte aucun autre bâtiment.
# On modélise la ligne de vue par y = h - (h * x) / t
# Pour chaque bâtiment à (x_i, h_i), 
# la hauteur sur la ligne de vue est y_i = h * (1 - x_i / t)
# Pour que le bâtiment ne bloque pas la vue, il faut :
# h_i < y_i soit h_i < h * (1 - x_i/t) donc
# h > h_i / (1 - x_i / t) = h_i * t / (t - x_i)

# On calcule la valeur minimale de h qui satisfait toutes ces contraintes
res = 0.0
for x_i, h_i in buildings:
    val = h_i * t / (t - x_i)
    if val > res:
        res = val

print(res)