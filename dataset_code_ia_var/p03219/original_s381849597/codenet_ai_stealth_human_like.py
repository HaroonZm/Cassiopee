# Bon, on lit deux nombres depuis l'entrée...
x, y = input().split()
# euh, faut penser à les convertir en int hein
x = int(x)
y = int(y)
# addition plus moitié de y ? bizarre comme demande mais ok
res = x + y / 2
# ah il faut un int, donc on bourrine ça avec int()
print(int(res))  # j'espère que c'est ce qu'il fallait ?