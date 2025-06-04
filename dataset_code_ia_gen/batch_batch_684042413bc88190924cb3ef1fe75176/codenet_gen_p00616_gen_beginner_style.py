while True:
    line = input()
    if not line:
        break
    n, h = map(int, line.split())
    if n == 0 and h == 0:
        break

    hole = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]

    marks = []
    for _ in range(h):
        c, a, b = input().split()
        a = int(a)
        b = int(b)
        marks.append((c, a, b))

    for (c, a, b) in marks:
        if c == "xy":
            z = a - 1
            x = b - 1
            y = z
            # Actually for xy: a,b = x,y and z is fixed at a; but defined as xy plane at z=a?
            # Problem states ci is xy plane, ai, bi are x,y coords and the plane is at z=ai.
            z = a - 1
            x = b - 1
            for z_i in range(n):
                hole[x][b-1][z_i] = False
            for z_i in range(n):
                hole[z_i][b-1][z] = False
            for i in range(n):
                hole[a-1][b-1][i] = False
            for i in range(n):
                hole[a-1][b-1][i] = False
                
            # We misunderstood the data: the marks specify the plane (xy,xz,yz) and the x,y coords on that plane.
            # The hole will be made at the marked coordinate, through to the opposite face, so all cubes along one dimension are removed.
            # Let's fix this approach.

    # So rewrite from scratch:

    # Initialize a 3D array to mark cubes that are blocked or have a hole
    blocked = [[[False]*n for _ in range(n)] for __ in range(n)]

    # For each mark, we have to make holes from marked cube to opposite surface.

    # For "xy" plane, the hole runs along the z axis (depth)
    # For "xz" plane, hole runs along y axis (vertical)
    # For "yz" plane, hole runs along x axis (horizontal)

    for (c, a, b) in marks:
        if c == "xy":
            x = a - 1
            y = b - 1
            for z in range(n):
                blocked[x][y][z] = True
        elif c == "xz":
            x = a - 1
            z = b - 1
            for y in range(n):
                blocked[x][y][z] = True
        elif c == "yz":
            y = a - 1
            z = b - 1
            for x in range(n):
                blocked[x][y][z] = True

    # Count cubes not blocked
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if not blocked[x][y][z]:
                    count += 1
    print(count)