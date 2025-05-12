K = int(raw_input())
nakaji = isono = 0
for I, N in zip([raw_input() for i in xrange(K)], [raw_input() for i in xrange(K)]):
    lose1 = lose2 = False
    if I == "kougekida" and isono == 0: lose1 = True
    if N == "kougekida" and nakaji == 0: lose2 = True
    if lose1 and lose2: continue
    elif lose1:
        print "Nakajima-kun"
        break
    elif lose2:
        print "Isono-kun"
        break

    if I == "tameru": isono = min(5, isono + 1)
    if N == "tameru": nakaji = min(5, nakaji + 1)

    if I == "kougekida":
        if N == "mamoru":
            if isono == 5:
                print "Isono-kun"
                break
            isono = 0
        if N == "tameru":
            print "Isono-kun"
            break
        if N == "kougekida":
            if nakaji < isono:
                print "Isono-kun"
                break
            elif nakaji == isono:
                nakaji = isono = 0
            elif nakaji > isono:
                print "Nakajima-kun"
                break
    if N == "kougekida":
        if I == "mamoru":
            if nakaji == 5:
                print "Nakajima-kun"
                break
            nakaji = 0
        if I == "tameru":
            print "Nakajima-kun"
            break
else:
    print "Hikiwake-kun"