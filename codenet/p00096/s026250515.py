def N(n):
    return (n+1)*(n+2)*(n+3)/6

while True:
    try:
        n = int(raw_input())
        if n > 2000:
            n = 4000 - n
        if n < 1001:
            print N(n)
        else:
            print N(n) - (N(2*(n-1000)) - (n-1000) - 1)/2
    except:
        break