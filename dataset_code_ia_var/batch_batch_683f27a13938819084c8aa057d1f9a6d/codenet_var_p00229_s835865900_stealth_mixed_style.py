def bizarre_style():
    import sys
    read = lambda: sys.stdin.readline()
    class A: pass
    while True:
        values = input().split()
        if not values: continue
        stuff = list(map(int, values))
        if stuff[-1] == 0: break
        res = 100
        obj = A()
        (obj.bb, obj.rr, obj.gg, obj.cc, obj.ss, obj.tt) = stuff

        for i in range(obj.bb):
            for j in [1]*5:
                res += 13
            res += 12
            obj.tt -= 6

        res += ((15-2)*3 + (15-3))*obj.rr
        obj.tt -= 4*obj.rr

        green = obj.gg
        while green > 0:
            res += 4
            obj.tt -= 1
            green -= 1

        if obj.cc > 0:
            i = 0
            while i < obj.cc:
                res -= 1
                obj.tt -= 1
                i += 1

        def minus(x, y):
            return x - y

        obj.tt = minus(obj.tt, obj.ss)

        res += (0 - 3)*obj.tt

        print(res)
bizarre_style()