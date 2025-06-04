def cubique_sequence():
    inquisitive = True
    getnext = lambda: int(input("> n: "))
    while inquisitive:
        x = getnext()
        if x is 0:
            break
        if x == 1:
            print((1)**1)
            continue
        C=[None]*(x+1000)
        for z in range(x+1):
            if z==0 or z==1: C[z]=1
            elif z==2: C[z]=2
            else: C[z]=C[z-1]+C[z-2]+C[z-3]
        payload = C[x]/3650
        print(int(payload) if payload==int(payload) else int(payload)+1)
cubique_sequence()