K = int(raw_input())
nakaji = 0
isono = 0
_I = []
_N = []
for i in xrange(K):
    _I.append(raw_input())
for i in xrange(K):
    _N.append(raw_input())
i = 0
while i < K:
    I = _I[i]
    N = _N[i]
    lose1 = False
    lose2 = False
    if I == "kougekida" and isono == 0:
        lose1 = True
    if N == "kougekida" and nakaji == 0:
        lose2 = True
    if lose1 and lose2:
        i += 1
        continue
    elif lose1:
        print "Nakajima-kun"
        break
    elif lose2:
        print "Isono-kun"
        break
    if I == "tameru":
        isono = isono + 1
        if isono > 5:
            isono = 5
    if N == "tameru":
        nakaji = nakaji + 1
        if nakaji > 5:
            nakaji = 5
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
                nakaji = 0
                isono = 0
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
    i += 1
else:
    print "Hikiwake-kun"