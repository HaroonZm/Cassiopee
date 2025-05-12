count = 0
while True:
    try:
        a, b = map(int, raw_input().split())
        if a + b == 0:
            break
        if count > 0:
            print ""
        flag = 0
        for i in range(a,b+1):
            if i%4 == 0 and (i%100 != 0 or i%400 == 0):
                print i
                flag = 1
        if flag == 0:
            print "NA"
        count += 1
    except:
        break