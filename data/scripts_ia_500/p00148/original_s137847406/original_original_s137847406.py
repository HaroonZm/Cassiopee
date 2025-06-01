L = [39]+range(1,39)
while True:
    try:
        print "3C{0:02d}".format(L[input()%39])
    except:
        break