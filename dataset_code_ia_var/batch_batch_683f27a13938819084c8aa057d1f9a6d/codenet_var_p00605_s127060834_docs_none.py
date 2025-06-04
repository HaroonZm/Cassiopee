while True:
    n, k = map(int, raw_input().split())
    if n == 0 and k == 0:
        break
    fridge = map(int, raw_input().split())
    judge = False
    for i in xrange(n):
        uses = map(int, raw_input().split())
        for j in xrange(k):
            fridge[j] -= uses[j]
            if fridge[j] < 0:
                judge = True
    if judge:
        print "No"
    else:
        print "Yes"