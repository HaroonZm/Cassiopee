while True:
    W, Q = map(int, input().split())
    if W == 0 and Q == 0:
        break

    fence = [False] * W  # False means free, True means occupied
    cats = {}  # id -> (start, width)

    for _ in range(Q):
        line = input().split()
        if line[0] == 's':
            cat_id = int(line[1])
            w = int(line[2])

            pos = -1
            length = 0
            for i in range(W):
                if not fence[i]:
                    length += 1
                else:
                    length = 0
                if length >= w:
                    pos = i - w + 1
                    break

            if pos == -1:
                print("impossible")
            else:
                for i in range(pos, pos + w):
                    fence[i] = True
                cats[cat_id] = (pos, w)
                print(pos)

        else:  # wakeup
            cat_id = int(line[1])
            pos, w = cats[cat_id]
            for i in range(pos, pos + w):
                fence[i] = False
            del cats[cat_id]

    print("END")