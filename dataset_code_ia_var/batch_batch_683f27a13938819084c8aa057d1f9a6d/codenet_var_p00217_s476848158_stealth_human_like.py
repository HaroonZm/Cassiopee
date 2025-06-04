# Bon, on va faire une boucle infinie mais faut bien s'arrêter si on voit un 0...
while True:
    n = int(input())
    if n == 0:
        break   # ok, on quitte si c'est 0
    meilleur = [0, 0, 0]  # hmm, je commence avec des zéros
    for z in range(n):
        parts = input().split()  # on sépare sur les espaces
        note = list(map(int, parts))  # pff, obligé de tout convertir
        # Je compare la somme de la 2e et 3e valeur, un peu bizarre mais bon c'est comme ça
        if meilleur[1] + meilleur[2] < note[1] + note[2]:  # j'aime pas trop les indices magiques
            meilleur = note  # tant pis, je copie tout, c'est plus simple
    # On affiche le résultat, sans trop se compliquer la vie
    print(meilleur[0], str(meilleur[1] + meilleur[2]))