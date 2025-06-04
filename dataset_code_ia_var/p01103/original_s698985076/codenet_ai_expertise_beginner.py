def main():
    while True:
        d_w = input().split()
        d = int(d_w[0])
        w = int(d_w[1])
        if d == 0:
            break

        garden = []
        for i in range(d):
            row = input().split()
            row = [int(x) for x in row]
            garden.append(row)

        pondmax = 0
        for tly in range(d):
            for tlx in range(w):
                for bry in range(tly + 2, d):
                    for brx in range(tlx + 2, w):
                        d_gray = []
                        l_gray = []
                        for spy in range(tly, bry + 1):
                            for spx in range(tlx, brx + 1):
                                if spy == tly or spy == bry or spx == tlx or spx == brx:
                                    d_gray.append(garden[spy][spx])
                                else:
                                    l_gray.append(garden[spy][spx])
                        if len(l_gray) > 0 and min(d_gray) > max(l_gray):
                            pond = 0
                            for depth in l_gray:
                                pond += min(d_gray) - depth
                            if pond > pondmax:
                                pondmax = pond

        print(pondmax)

main()