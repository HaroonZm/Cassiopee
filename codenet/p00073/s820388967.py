while 1:
    x=float(input())
    h=float(input())
    if x==0: break
    print(x*x+2*x*(((x/2)**2)+h*h)**0.5)