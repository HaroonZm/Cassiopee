n = int(input())  # Nombre de lignes à lire
s = []
for x in range(n):
    val = input()  # On prend chaque ligne
    s.append(val)
# Combien de fois "E869120" apparaît ?
counter = 0
for elem in s:
    if elem == "E869120":
        counter += 1
print(counter)
# (Je crois que ça marche ?)