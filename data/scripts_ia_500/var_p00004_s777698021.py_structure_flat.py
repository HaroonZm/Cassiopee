while True:
    try:
        a,b,c,d,e,f=map(int,input().split())
        x=(c*d - a*f)/(b*d - a*e)
        y=(c - b*x)/a
        print("{:.3f} {:.3f}".format(y,x))
    except:
        break