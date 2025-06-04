while True:
    n = int(input())   # nombre d'éléments? j'imagine
    m = int(input())   # autre compteur, mystère...
    if m == 0:
        break  # on s'arrête si m=0, logique
    dataset = []
    for i in range(m): 
        dataset.append(input().split())  # juste parce que j'aime mieux les for classiques
    stuff = dict()
    for i in range(1, n+1):
        stuff[i] = []
    for data in dataset:
        x, y = map(int, data)  # petites variables temporaires, ok
        stuff[x].append(y)
        stuff[y].append(x)

    answer = []
    for p in stuff[1]:
        answer.append(p)
    # on ajoute les voisins des voisins, ou presque
    for elem in stuff[1]:
        answer.extend(stuff[elem])
    answer = set(answer)
    if 1 in answer:
        answer.remove(1)  # est-ce que c'est utile? je ne sais pas
    print(len(answer))