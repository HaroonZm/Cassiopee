def main():
    while True:
        d, w = map(int, input().split())
        if d == 0: break

        garden = []
        for i in range(d):
            garden.append(list(map(int, input().split())))

        pondmax = 0
        for tly in range(len(garden)):
            for tlx in range(len(garden[0])):
                for bry in range(tly + 2, len(garden)):
                    for brx in range(tlx + 2, len(garden[0])):
                        # sampling
                        l_gray = []
                        d_gray = []
                        for spy in range(tly, bry + 1):
                            for spx in range(tlx, brx + 1):
                                if spy == tly or spy == bry or spx == tlx or spx == brx:
                                    d_gray.append(garden[spy][spx])
                                else: l_gray.append(garden[spy][spx])
                        if min(d_gray) > max(l_gray):
                            pond = 0
                            for depth in l_gray:
                                pond += min(d_gray) - depth
                            if pond > pondmax: pondmax = pond

        print(pondmax)
                        
main()