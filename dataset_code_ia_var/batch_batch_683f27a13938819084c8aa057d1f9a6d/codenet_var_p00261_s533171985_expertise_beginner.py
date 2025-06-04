map_ = [
    (1, 4),  # start
    (-1, 2),
    (5, 3),
    (4, 1),  # goal
    (1, -1),
    (3, 4)
]

while True:
    x = input()
    if x == '#':
        break

    pt = 0
    for ch in x:
        v = int(ch)
        pt = map_[pt][v]
        if pt == -1:
            break

    if pt == 3:
        print("Yes")
    else:
        print("No")