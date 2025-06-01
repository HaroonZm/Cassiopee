while True:
    try:
        a = int(input())
        n = 39
        last = a % n
        if last == 0:
            last = n
        if last < 10:
            print("3C0" + str(last))
        else:
            print("3C" + str(last))
    except:
        break