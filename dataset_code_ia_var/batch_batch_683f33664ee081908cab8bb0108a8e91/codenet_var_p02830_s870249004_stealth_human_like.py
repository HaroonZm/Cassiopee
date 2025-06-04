n = int(input())
s, t = input().split()
res = []
# On va parcourir chaque caractère des deux chaînes
for i in range(n):
    res += s[i]
    res.append(t[i])  # j'utilise append ici, c'est pareil normalement
# Bon, on affiche le résultat final
print(''.join(res))