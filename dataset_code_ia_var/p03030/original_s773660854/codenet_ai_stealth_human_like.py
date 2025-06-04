# C'est le code pour le B d'aujourd'hui (je crois)
n = int(input())  # on lit n
liste = []
for j in range(n):
    s, p = input().split()
    p = int(p)  # conversion forcée (sinon ça plante en int)
    liste.append([s, p, j])

# d'abord tri par place (je préfère), puis par nom
liste.sort(key=lambda elem: elem[1], reverse=True)
liste.sort(key=lambda elem: elem[0])

# affichage des indices 1-based (pas fan de ce "+1" mais bon)
for thing in liste:
    print(thing[2] + 1)  # normalement ça sort dans le bon ordre?