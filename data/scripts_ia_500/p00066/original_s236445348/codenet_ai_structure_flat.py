while True:
    try:
        a = raw_input()
        if a[::4] == "ooo" or a[2:8:2] == "ooo":
            print "o"
        elif a[::4] == "xxx" or a[2:8:2] == "xxx":
            print "x"
        elif a[0:3] == "ooo":
            print "o"
        elif a[3:6] == "ooo":
            print "o"
        elif a[6:9] == "ooo":
            print "o"
        elif a[0::3] == "ooo":
            print "o"
        elif a[1::3] == "ooo":
            print "o"
        elif a[2::3] == "ooo":
            print "o"
        elif a[0:3] == "xxx":
            print "x"
        elif a[3:6] == "xxx":
            print "x"
        elif a[6:9] == "xxx":
            print "x"
        elif a[0::3] == "xxx":
            print "x"
        elif a[1::3] == "xxx":
            print "x"
        elif a[2::3] == "xxx":
            print "x"
        else:
            print "d"
    except:
        break