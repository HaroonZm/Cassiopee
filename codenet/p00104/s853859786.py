while True:
    HW = list(map(int, input().split()))
    H, W = HW[0], HW[1]
    if H == 0 and W == 0:
        break

    tiles = [input() for i in range(H)]
    i, j, count = 0, 0, 0
    while True:
        tile = tiles[i][j]
        if count >= H*W:
            print("LOOP")
            break

        if tile == ">":
            if W > j:
                j += 1
            else:
                print(j, i)
                break

        elif tile == "<":
            if j > 0:
                j -= 1
            else:
                print(j, i)
                break

        elif tile == "^":
            if i > 0:
                i -= 1
            else:
                print(j, i)
                break

        elif tile == "v":
            if H > i:
                i += 1
            else:
                print(j, i)
                break
        else:
            print(j, i)
            break
        count += 1