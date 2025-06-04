case_num = 1

while True:
    N = input()
    if N == '':
        continue
    N = int(N)
    if N == 0:
        break

    box = []
    # lire 5 couches z=0..4
    for z in range(5):
        grid = []
        for y in range(5):
            while True:
                line = input()
                if line.strip() != '':
                    break
            row = list(line.strip())
            grid.append(row)
        box.append(grid)
        # lire ligne vide
        while True:
            try:
                blank = input()
                if blank.strip() == '':
                    break
            except:
                break

    # lire M1 et a_i
    while True:
        line = input()
        if line.strip() != '':
            break
    M1 = int(line)
    a_list = []
    if M1 > 0:
        while True:
            line = input()
            if line.strip() != '':
                a_list = list(map(int, line.strip().split()))
                if len(a_list) < M1:
                    while len(a_list) < M1:
                        a_list += list(map(int, input().strip().split()))
                break
    else:
        a_list = []

    # lire M2 et b_j
    while True:
        line = input()
        if line.strip() != '':
            break
    M2 = int(line)
    b_list = []
    if M2 > 0:
        while True:
            line = input()
            if line.strip() != '':
                b_list = list(map(int, line.strip().split()))
                if len(b_list) < M2:
                    while len(b_list) < M2:
                        b_list += list(map(int, input().strip().split()))
                break
    else:
        b_list = []

    # voisins relatifs en 3D (face, edge, corner)
    neighbors = []
    for dz in [-1,0,1]:
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dz==0 and dy==0 and dx==0:
                    continue
                neighbors.append( (dz, dy, dx) )

    # simuler N jours
    for day in range(N):
        new_box = []
        for z in range(5):
            new_grid = []
            for y in range(5):
                new_row = []
                for x in range(5):
                    # compter voisins vivants
                    count = 0
                    for dz,dy,dx in neighbors:
                        nz = z + dz
                        ny = y + dy
                        nx = x + dx
                        if 0 <= nz < 5 and 0 <= ny <5 and 0 <= nx <5:
                            if box[nz][ny][nx] == '1':
                                count += 1
                    if box[z][y][x] == '0':
                        # naissance si count dans a_list
                        if count in a_list:
                            new_row.append('1')
                        else:
                            new_row.append('0')
                    else:
                        # mort si count pas dans b_list
                        if count in b_list:
                            new_row.append('1')
                        else:
                            new_row.append('0')
                new_grid.append(new_row)
            new_box.append(new_grid)
        box = new_box

    print("Case {}:".format(case_num))
    for z in range(5):
        for y in range(5):
            print(''.join(box[z][y]))
        if z != 4:
            print()
    print()
    case_num += 1