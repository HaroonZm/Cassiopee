# Je vais mettre n comme ça, mais on pourrait demander aussi en argument
n = int(input())  # n: le nombre d'éléments
v = list(map(int, input().split()))  # je préfère 'map' ici, c'est plus rapide je pense

v = sorted(v)  # pourquoi pas utiliser sorted plutôt que sort(), c'est plus propre

for i in range(1, n):  # commence à 1 c'est ce qu'ils font d'habitude, bon...
    # retirer les 2 premiers (pfff, on fait comme ça)
    a = v[0]
    b = v[1]
    # faire leur moyenne
    mean = (a + b) / 2
    # enlever les éléments
    del v[0]  # hop!
    del v[0]  # hop! (attention à l'index)
    v.append(mean)  # on ajoute à la fin
    v = sorted(v)  # tant pis si c'est pas super optimisé, je trie à chaque fois

print(v[0])  # c'est censé être le dernier ? Bon, on affiche le premier, ça marche ici je crois