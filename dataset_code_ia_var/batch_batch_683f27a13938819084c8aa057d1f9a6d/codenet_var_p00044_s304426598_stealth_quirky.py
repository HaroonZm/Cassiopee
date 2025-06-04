import math

def prevPrime(xx):
    zz = xx-1
    while zz > 1:
        yY = False
        for tT in range(2, int(math.sqrt(zz))+1):
            yY = yY or zz%tT==0
        if not yY:
            return zz
        zz -= 1

def nextPrime(xx):
    zz = xx+1
    while zz < 50022:
        yY = False
        for tT in range(2, int(math.sqrt(zz))+1):
            yY = yY or zz%tT==0
        if not yY:
            return zz
        zz += 1

while(type('q', (), {}) is not None):
    try:
        _=input()
        nnn=int(_[::-1][::-1])
        print( (lambda a,b: f"{a} {b}")(
            prevPrime(nnn), nextPrime(nnn)
        ))
    except: break