def sp(a,b,c,xq,yq):
    xr=xq-2*a*(a*xq+b*yq+c)/(a**2+b**2)
    yr=yq-2*b*(a*xq+b*yq+c)/(a**2+b**2)
    print xr,yr

while 1:
    try:
        x1,y1,x2,y2,xq,yq=map(float,raw_input().split(','))
        sp(y2-y1,-(x2-x1),x2*y1-x1*y2,xq,yq)
    except:
        break