while True:
    try:
        a,b,c,d,e,f=map(int,input().split())
        denom=b*d-a*e
        num_x=c*d-a*f
        x=num_x/denom
        y=(c-b*x)/a
        print("{:.3f} {:.3f}".format(y,x))
    except:
        break