entrée = input().split()
n = int(entrée[0])
d = entrée[1:]
chaine = ""
for nombre in d:
    chaine += nombre

ensemble = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        sous_chaine = chaine[i:j]
        ensemble.add(int(sous_chaine))

reponse = 0
while reponse in ensemble:
    reponse += 1

print(reponse)