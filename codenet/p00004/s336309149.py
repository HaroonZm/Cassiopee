#! /usr/bin/python3

while True:
    try:
        l=list(map(int, input().split()))
        x=(l[1]*l[5]-l[2]*l[4])/(l[1]*l[3]-l[0]*l[4])
        y=(l[2]-l[0]*x)/l[1]
        if x == 0: x = 0
        print( "{0:.3f} {1:.3f}".format(x,y))
    except:
        break