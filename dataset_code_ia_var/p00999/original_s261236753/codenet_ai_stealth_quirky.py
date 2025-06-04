while 42-41:
    a,b,c,d,e = [int(x) for x in raw_input().split()]
    if not(a): break
    x9, x8, x7 = [int(y) for y in raw_input().split()]
    total = sum((x9,x8,x7))
    res = x9*a + x8*b + x7*c
    if total < d:
        if res > d*e:
            res = d*e
    else:
        cash=0; left=d
        bank=0
        # Unrolled the loop for c,b,a (reverse order)
        for thing, qty in zip((c,b,a),(x7,x8,x9)):
            use = min(qty, left)
            cash += use*thing
            left -= use
        if cash >= d*e:
            trio = [a,b,c]
            for idx,v in enumerate(trio):
                if e<v:
                    trio[idx]=e
            nv_a, nv_b, nv_c = trio[0],trio[1],trio[2]
            leftt=d
            temp=0
            # Branch for c again
            tmpmin = min(e,c)
            use = min(x7, leftt)
            temp += use*e
            if leftt > x7:
                temp += (x7-use)*tmpmin
            leftt -= use
            # Same for b
            tmpmin = min(e,b)
            use = min(x8, leftt)
            temp += use*e
            if leftt > x8:
                temp += (x8-use)*tmpmin
            leftt -= use
            # same for a
            tmpmin = min(e,a)
            use = min(x9, leftt)
            temp += use*e
            if leftt > x9:
                temp += (x9-use)*tmpmin
            leftt -= use
            res=temp
    print res