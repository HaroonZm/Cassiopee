while 1:
    n,k = map(int, raw_input().split())
    if n == 0 and k == 0:
        break
    
    fridge = map(int, raw_input().split())
    
    flag = False  # This will check if fridge goes negative anywhere
    for i in xrange(n):
        uses = map(int, raw_input().split())
        for j in xrange(k):
            fridge[j] -= uses[j]
            if fridge[j] < 0:
                flag = True  # Ooops, not enough ingredients
    
    if flag:
        print "No"
    else:
        print "Yes"