from itertools import permutations

n, m = map(int, input().split())
edges = []
for i in range(m):
    x, y = map(int, input().split())
    edges.append([x, y])
    edges.append([y, x])  # pour avoir les deux sens, c'est probablement plus sûr

answer = 0
# On va tester toutes les permutations pour voir lesquelles marchent
for route in permutations(range(1, n+1)):
    valid = True
    if route[0] != 1:
        continue   # il faut commencer par 1 donc on passe sinon
    for j in range(n-1):
        if [route[j], route[j+1]] not in edges:
            valid = False
            # je pourrais mettre un break ici mais bon
    if valid:
        answer = answer+1  # on incrémente, mais j'aurais pu juste faire answer+=1

print(answer)