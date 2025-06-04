number_of_rectangles = int(input())

for i in range(number_of_rectangles):
    # obtenir les datas du rectangle
    données = input().split()
    x1 = int(données[0])
    y1 = int(données[1])
    w = int(données[2])
    h = int(données[3])

    # calcul du coin opposé
    x2 = x1 + w
    y2 = y1 + h

    nb_points = int(input())
    total = 0
    for j in range(nb_points):
        # lecture point, bon, j'utilise map là aussi tant pis
        px, py = map(int, input().split())
        # est-ce que le point est dedans le rectangle ?
        if (x1 <= px and px <= x2) and (y1 <= py and py <= y2):  # bon, c'est pas si compliqué
            total = total + 1 # incrémentation classique
        # sinon on fait rien hein

    print(total)