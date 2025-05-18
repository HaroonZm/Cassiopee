while 1:
    x,h = input(),input()
    if x==0 and h==0: break
    a=float(x)/2
    s=x*x+2*x*(a*a+h*h)**0.5
    print s