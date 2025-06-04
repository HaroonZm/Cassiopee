# Bon alors, on va récupérer les valeurs, normal...
x, y, z = map(int, input().split())
# Tiens, je stocke dans une liste bizarrement
mes_vals = [(x, 'A'), (y, 'B'), (z, 'C')]
# Je suppose qu'on doit afficher la lettre la plus grande ?
big = mes_vals[0]
for truc in mes_vals:
    if truc[0] > big[0]:
        big = truc
# pourquoi pas print direct
print(big[1])