enter = lambda: raw_input()
K = int(enter())
iso, naka = 0, 0
I_input, N_input = [], []
for _ in range(K):
    I_input += [enter()]
for _ in range(K):
    N_input.append(enter())
step = 0
while step < K:
    I, N = I_input[step], N_input[step]
    l1 = (I == "kougekida" and iso == 0)
    l2 = (N == "kougekida" and naka == 0)
    if l1 & l2:
        step += 1
        continue
    if l1:
        print "Nakajima-kun"
        break
    if l2:
        print "Isono-kun"
        break

    if I == "tameru": iso = 5 if iso == 5 else iso+1
    if N == "tameru": naka = naka+1 if naka < 5 else naka

    # nested lookup
    if I == "kougekida":
        if N == "mamoru":
            if iso == 5:
                print "Isono-kun"
                break
            iso = 0
        elif N == "tameru":
            print "Isono-kun"
            break
        elif N == "kougekida":
            r = naka - iso
            if r < 0:
                print "Isono-kun"
                break
            if r == 0:
                iso = naka = 0
            if r > 0:
                print "Nakajima-kun"
                break
    if N == "kougekida":
        if I == "mamoru":
            if naka == 5:
                print "Nakajima-kun"
                break
            naka = 0
        elif I == "tameru":
            print "Nakajima-kun"
            break
    step += 1
else:
    print "Hikiwake-kun"