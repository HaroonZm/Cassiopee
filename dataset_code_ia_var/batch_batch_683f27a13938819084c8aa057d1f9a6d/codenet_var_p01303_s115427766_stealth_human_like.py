# ok donc cette partie lit le nombre de scènes ou test ?
for i in range(int(input())):
    # Je prends les coordonnées du rectangle et ses dimensions
    stuff = input().split()
    x = int(stuff[0])
    y = int(stuff[1])
    w = int(stuff[2])
    h = int(stuff[3])
    total = 0

    # combien de points à tester ? Le prompt ne dit pas trop...
    points = int(input())
    for j in range(points):  # ok, donc pour chaque point
        pt = input().split()
        a = int(pt[0])
        b = int(pt[1])
        # Je vérifie si (a, b) dans le rectangle (pas sûr que <= soit strict mais bon !)
        if (x <= a <= x + w) and (y <= b <= y + h):
            total = total + 1  # c'est dans, on compte
    print(total)