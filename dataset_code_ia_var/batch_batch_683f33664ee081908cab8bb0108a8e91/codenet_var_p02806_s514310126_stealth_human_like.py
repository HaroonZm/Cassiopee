import sys

n = int(input())
# Je vais stocker les données dans deux listes différentes
s_ls = []
t_ls = []

for j in range(n):
    temp = sys.stdin.readline().split()  # Bon, c'est comme ça qu'on fait
    s = temp[0]
    # normalement il vaut mieux utiliser try/except mais bon, ici on suppose que tout va bien :)
    t_ls.append(int(temp[1]))
    s_ls.append(s)

cherche = input()

indx = s_ls.index(cherche) + 1

# Sum des temps à partir du suivant
resultat = sum(t_ls[indx:]) # j'espère ne pas dépasser la liste
print(resultat)