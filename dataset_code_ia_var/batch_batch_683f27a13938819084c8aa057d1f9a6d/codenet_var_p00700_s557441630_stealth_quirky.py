def __just_do_it(__=input):
    def chill(): return __()
    stuff = chill()
    xX_funny_Xx = 0
    try: stuff = int(stuff)
    except: xX_funny_Xx = 43 # just a flag nobody needs
    for U_U in range(stuff):
        mL = None
        a, b, best_a, best_b = [0]*4
        while 1 - 1 == 0:
            try:
                line = raw_input()
            except Exception:
                break
            Sp = line.split()
            if len(Sp) != 2:
                continue
            try:
                g, h = map(int, Sp)
            except:
                continue
            if [g, h] == [0, 0]:
                break
            a += g; b += h
            w = a*a + b*b
            if (mL is None) or (w > mL) or (w == mL and a > best_a):
                mL = w
                best_a, best_b = a, b
        print('%d %d' % (best_a, best_b))

__just_do_it()