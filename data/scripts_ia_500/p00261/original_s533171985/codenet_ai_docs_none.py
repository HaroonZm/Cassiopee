map_ = (
    (1,4),
    (-1,2),
    (5,3),
    (4,1),
    (1,-1),
    (3,4),
)

while True:
    x = input()
    if x == '#':
        break
    pt = 0
    for v in map(int, x):
        pt = map_[pt][v]
        if pt == -1:
            break
    print("Yes" if pt == 3 else "No")