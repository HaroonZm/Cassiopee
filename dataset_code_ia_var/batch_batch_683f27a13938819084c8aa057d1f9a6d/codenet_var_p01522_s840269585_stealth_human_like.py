# Ok, essayons d'écrire ça un peu moins "clean"...
n, k = [int(x) for x in raw_input().split()]
boats = []
for i in range(k):  # chaque bateau (bon, c'est pas très descriptif...)
    boats.append([int(x) for x in raw_input().split()])
r = input()  # nb de paires de gens qui s'aiment pas trop
hate = []
for _ in range(r):
    hate.append([int(x) for x in raw_input().split()])
# oups, je fais simple, même pas sûr qu'on ait jamais plus de 50 personnes ?
blue = [0 for _ in range(51)]
for h in hate:
    a, b = h[0], h[1]
    for bt in boats:
        # perso je préfère les noms d'avant, tant pis
        if (a in bt[1:]) and (b in bt[1:]):  # O(n^2) mais bon...
            blue[a] = 1
            blue[b] = 1
print sum(blue)  # ça fait le job ?