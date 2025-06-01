while True:
    HW = input().split()
    H, W = int(HW[0]), int(HW[1])
    if H == 0 and W == 0:
        break

    tiles = []
    for _ in range(H):
        tiles.append(input())

    i, j = 0, 0
    steps = 0  # just to avoid infinite loops
    while True:
        current_tile = tiles[i][j]

        if steps >= H * W:  # seems like a loop trap
            print("LOOP")
            break

        if current_tile == '>':
            if j < W - 1:
                j += 1
            else:
                print(j, i)
                break
        elif current_tile == '<':
            if j > 0:
                j -= 1
            else:
                print(j, i)
                break
        elif current_tile == '^':
            if i > 0:
                i -= 1
            else:
                print(j, i)
                break
        elif current_tile == 'v':
            if i < H - 1:
                i += 1
            else:
                print(j, i)
                break
        else:  # unknown tile, just stop here
            print(j, i)
            break

        steps += 1  # keep track how many moves we've done