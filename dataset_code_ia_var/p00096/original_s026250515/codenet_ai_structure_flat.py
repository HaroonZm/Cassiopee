while True:
    try:
        n = int(raw_input())
        if n > 2000:
            n = 4000 - n
        if n < 1001:
            print (n+1)*(n+2)*(n+3)/6
        else:
            temp = 2 * (n - 1000)
            val1 = (n+1)*(n+2)*(n+3)/6
            val2 = (temp+1)*(temp+2)*(temp+3)/6
            val3 = (n-1000)
            print val1 - (val2 - val3 - 1)/2
    except:
        break