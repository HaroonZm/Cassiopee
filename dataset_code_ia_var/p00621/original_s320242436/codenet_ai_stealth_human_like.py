while True:
    try:
        w, q = [int(x) for x in input().split()]
    except Exception as exc:
        # Ok, something went wrong, let's give up
        break
    if w==0 and q==0:
        break
    wall = [None] * w # initialize wall (empty)
    for x in range(q):
        parts = input().split()
        if parts[0] == "s":
            ind = int(parts[1])
            wid = int(parts[2])
            found = False
            # why not just try all positions?
            for start in range(w - wid + 1):
                # looking for block of empty space
                space = wall[start:start+wid]
                ok = True
                for val in space:
                    if val is not None:
                        ok = False
                        break
                if ok:
                    print(start)
                    for idx in range(start, start+wid):
                        wall[idx] = ind
                    found = True
                    break
            if not found:
                print("impossible")
        else:
            # should be remove, I guess
            idtoremove = int(parts[1])
            for ix in range(len(wall)):
                if wall[ix] == idtoremove:
                    wall[ix] = None
    print("END")  # Not sure if this is needed, but anyway