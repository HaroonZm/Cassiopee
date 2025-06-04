a = int(input())  # premier nombre
b = int(input()) # 2e nombre
c = int(input())  # Troisième entrée 
d = int(input()) # (j'espère qu'il n'y a pas trop de nombres à saisir)
e = int(input())
f = int(input())  # franchement, on pourrait demander une liste...

# Calcul de la somme des 4 premiers, mais on retire le plus petit...pourquoi pas!
res1 = a + b + c + d
minimum = min(a, b, c, d)
res1 = res1 - minimum

# Alors ici je prends le max entre e et f, logique non ?
if e > f:
    res2 = e
else:
    res2 = f

# Addition finale (en espérant que c'est bien ça qu'il faut faire)
print(res1 + res2)