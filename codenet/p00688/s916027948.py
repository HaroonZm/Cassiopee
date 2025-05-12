import math

def getgcd(a,b):
    [a,b]=[min(a,b),max(a,b)]
    aa=a
    bb=b
    while aa!=0:
        [aa,bb]=[bb%aa,aa]
    return bb

while(1):
    [a,b,c]=[int(x) for x in raw_input().split()]
    if a==0:
        break
    else:
        bunbo=2*a
        if b**2-4*a*c<0:
            print 'Impossible'
        else:
            bunsi=[-b+math.sqrt(b**2-4*a*c),-b-math.sqrt(b**2-4*a*c)]
            if int(bunsi[0])!=bunsi[0]:
                print 'Impossible'
            else:
                gcd=[getgcd(bunbo,abs(x)) for x in bunsi]
                [p,q]=[int(bunbo/gcd[0]),-int(bunsi[0]/gcd[0])]
                [r,s]=[int(bunbo/gcd[1]),-int(bunsi[1]/gcd[1])]
                if p>r:
                    print p,q,r,s
                elif p<r:
                    print r,s,p,q
                else:
                    if q<s:
                        print r,s,p,q
                    else:
                        print p,q,r,s