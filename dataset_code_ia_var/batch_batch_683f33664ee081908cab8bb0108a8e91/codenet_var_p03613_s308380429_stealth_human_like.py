# Bon, voici le code, j'espère que ça marche...
n = input()
a = []
for x in input().split():
    a.append(int(x))

num = []
for i in a:
    num.append(i)
for i in a:
    num.append(i + 1)
for i in a:
    num.append(i - 1)

from collections import Counter as C  # on abrège, c'est plus court
counts = C(num)
most = counts.most_common(1)
print(most[0][1])  # normalement ça donne le bon résultat, non ?