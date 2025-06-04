# Bon, d'abord on lit le nombre de cas à traiter
num_cases = int(input())
for i in range(num_cases):
    # On récupère les coordonnées du rectangle (j'espère qu'on n'a pas de mauvaises surprises)
    X, Y, W, H = [int(z) for z in input().split()]
    total_inside = 0
    stuff = int(input())  # le nombre de points
    for _ in range(stuff):
        point = input().split()
        A, B = int(point[0]), int(point[1])
        # Hmm, je crois que c'est bien inclusif ces bornes ?
        if (X <= A and A <= X+W) and (Y <= B and B <= Y+H):
            total_inside += 1
        # sinon, on fait rien, next!
    print(total_inside)  # résultat pour ce cas-là