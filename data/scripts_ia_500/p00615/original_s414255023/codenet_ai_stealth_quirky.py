while 1:
    n,m=(int(x) for x in raw_input().split())
    if not n and not m: break
    up=[int(x) for x in raw_input().split()] if n else []
    down=[int(x) for x in raw_input().split()] if m else []
    combined = up + down
    combined.sort()
    maximum_gap = combined[0]
    for index in xrange(len(combined)-1):
        diff = combined[index+1] - combined[index]
        maximum_gap = (diff, maximum_gap)[diff < maximum_gap]
    print maximum_gap