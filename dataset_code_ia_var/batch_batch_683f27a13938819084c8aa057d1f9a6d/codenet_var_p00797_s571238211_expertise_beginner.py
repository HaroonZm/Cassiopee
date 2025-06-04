while True:
    n_m = raw_input()
    n_m = n_m.split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0:
        break
    familymatrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(-100000)
        familymatrix.append(row)
    namedic = {}
    returned = []
    for i in range(n):
        returned.append(0)
    spacenum = 0
    spacenumold = 0
    for i in range(n):
        indata = raw_input()
        name = indata.strip()
        spacenum = len(indata) - len(name)
        namedic[name] = i
        for j in range(i):
            familymatrix[j][i] = familymatrix[j][i-1] + (spacenum - spacenumold)
        spacenumold = spacenum
    for i in range(n):
        for j in range(i):
            if familymatrix[j][i] == 0 and returned[j] == 0:
                returned[j] = 1
            elif familymatrix[j][i] < 0:
                returned[j] = 2
            if familymatrix[j][i] > 0 and returned[j] == 1:
                familymatrix[j][i] = -1
            elif returned[j] == 2:
                familymatrix[j][i] = -1
    for i in range(m):
        query = raw_input()
        query_parts = query.split()
        person1 = query_parts[0]
        relation = ' '.join(query_parts[1:-1])
        person2 = query_parts[-1]
        if person2.endswith('.'):
            person2 = person2[:-1]
        X = namedic[person1]
        Y = namedic[person2]
        if relation == "is a child of":
            print familymatrix[Y][X] == 1
        elif relation == "is the parent of":
            print familymatrix[X][Y] == 1
        elif relation == "is a sibling of":
            print familymatrix[X][Y] == 0 or familymatrix[Y][X] == 0
        elif relation == "is a descendant of":
            print familymatrix[Y][X] > 0
        elif relation == "is an ancestor of":
            print familymatrix[X][Y] > 0
    print ""