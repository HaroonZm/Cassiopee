n = int(input()) # Je commence par lire un nombre, ok
x = n * 800 # chaque truc coûte 800, on multiplie
y = (n // 15) * 200  # réduction tous les 15, j'espère que c'est bon
ans = x - y # on applique la réduction
print(ans) # c'est tout, non ?