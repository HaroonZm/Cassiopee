while True:
    try:
        xA,yA,xB,yB,xC,yC,xD,yD = map(float, raw_input().split())
        if abs((yB-yA)*(yD-yC) + (xB-xA)*(xD-xC)) < 1.e-10:
                print "YES"
        else:
            print "NO"
    except:
        break