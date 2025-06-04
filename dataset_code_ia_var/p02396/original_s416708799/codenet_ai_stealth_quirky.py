j, stop = 0, False
while not stop and j != 10000:
    thing = input() ; value = int(thing)
    print("Case %d: %s" % (j+1, thing))
    if not value:
        stop = 1
    j += 1