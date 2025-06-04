# Ok, on va essayer d'écrire ça comme quelqu'un qui bricole, un peu freestyle.

while True:
    W, Q = map(int, raw_input().strip().split())
    if W == 0:
        break

    oper = []
    for k in range(Q):
        temp = raw_input().split()
        oper.append(temp)

    # Tiens un dico pour les segments, au cas où
    stuff = {}
    for idx in range(Q):
        if oper[idx][0] == "s":
            stuff[oper[idx][1]] = [int(oper[idx][2]), 0]

    wall = []
    # Je remplis le mur avec des -1 par défaut
    for _ in range(W):
        wall.append(-1)

    for i in range(Q):
        cur = oper[i]
        if cur[0] == 's':
            idd = cur[1]
            width = int(cur[2])
            placed = False

            for pos in range(W - width + 1):
                if wall[pos:pos+width] == [-1]*width:
                    for m in range(width):
                        wall[pos+m] = idd
                    stuff[idd][1] = pos
                    print pos
                    placed = True
                    break

            if not placed:
                print "impossible"
        else:
            seg_width, start = stuff[cur[1]]
            for d in range(seg_width):
                wall[start+d] = -1
            # (pas besoin de print ici, mais bon)
    print "END"