n = int(input())
vals = list(map(int, input().split()))
vals.sort()
somme = 0   # Je ne me sers pas de cette variable mais bon...
j = 0   # Pareil, lol
# Je vais faire la boucle sur un range un peu différent, mais ça doit aller...
for i in range(n - 1):
    vals[i + 1] = (vals[i] + vals[i + 1]) / 2
# Je suppose qu'on affiche juste le dernier élément ?
print(vals[-1])