while True:
    N = int(raw_input())
    if N == 0:
        break
    a = raw_input().split()
    mn = -10000000000
    mx =  10000000000
    i = 1
    found_none = False
    while i < N:
        if a[i-1] == "x" and a[i] == "x":
            print "none"
            found_none = True
            break
        elif a[i-1] == "x":
            if (i+1) % 2 == 0:
                if int(a[i]) - 1 < mx:
                    mx = int(a[i]) - 1
            else:
                if int(a[i]) + 1 > mn:
                    mn = int(a[i]) + 1
        elif a[i] == "x":
            if (i+1) % 2 == 0:
                if int(a[i-1]) + 1 > mn:
                    mn = int(a[i-1]) + 1
            else:
                if int(a[i-1]) - 1 < mx:
                    mx = int(a[i-1]) - 1
        else:
            n1 = int(a[i-1])
            n2 = int(a[i])
            if (i+1) % 2 == 0 and n2 <= n1:
                print "none"
                found_none = True
                break
            elif (i+1) % 2 == 1 and n2 >= n1:
                print "none"
                found_none = True
                break
        i += 1
    if not found_none:
        if "x" not in a:
            print "ambiguous"
        else:
            if mn == mx:
                print mx
            elif mn < mx:
                print "ambiguous"
            else:
                print "none"