n = int(input())   # combien on a d'éléments ?
line = input().split()
a = int(line[0]); b = int(line[1])  # bornes pour les groupes...

# ça fait un peu moche, mais bon
nums = input().split()
p = []
for ii in range(n): p.append(int(nums[ii]))  # on remplit la liste (on pourrait map directement, mais flemme)

# trois compteurs pour chaque catégorie
c1 = 0; c2 = 0
c3 = 0

for elt in p:
    # on check dans quel intervalle on est
    if elt <= a:
        c1=c1+1
    elif elt >= a+1 and elt <= b:
        c2 += 1
    elif elt >= b+1:
        c3 = c3 + 1

# affiche la taille du plus petit groupe (ça me semble logique)
print(min(c1, c2, c3))