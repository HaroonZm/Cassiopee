map_ = (
    (1,4),
    (-1,2),
    (5,3),
    (4,1),
    (1,-1),
    (3,4)
)

while 1:
    x = input()
    if x == '#':
        break
    pt = 0
    i = 0
    lx = list(x)
    while i < len(lx):
        try:
            v = int(lx[i])
        except ValueError:
            pt = -1
            break
        pt = map_[pt][v]
        if pt == -1:
            break
        i += 1
    if pt == 3:
        print("Yes")
    else:
        print("No")