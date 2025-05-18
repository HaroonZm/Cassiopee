import math

def make_func1(a, b, c, d):
    return lambda X : a*X**3 + b*X**2 + c*X + d
def make_func2(a, b, c):
    return lambda x : 3*a*x**2 + 2*b*x + c

i = int(input())
for j in range(i):
    a, b, c, d = map(int, input().split())
    fX = make_func1(a, b, c, d)
    fx = make_func2(a, b, c)
    D_4 = b**2 - 3*a*c
    
    if D_4<=0:
        if 0<a:
            if d<0:
                pos=1
                neg=0
            if d==0:
                pos=0
                neg=0
            if 0<d:
                pos=0
                neg=1
        if a<0:
            if d<0:
                pos=0
                neg=1
            if d==0:
                pos=0
                neg=0
            if 0<d:
                pos=1
                neg=0
    
    if D_4>0 :
        if 0<a:
            p = (-b-math.sqrt(b**2-3*a*c))/(3*a)
            q = (-b+math.sqrt(b**2-3*a*c))/(3*a)
            if 0<fX(q) or fX(p)<0 :
                if d<0:
                    pos=1
                    neg=0
                if d==0:
                    pos=0
                    neg=0
                if 0<d:
                    pos=0
                    neg=1
            if fX(q)==0:
                if d<0:
                    pos=3
                    neg=0
                if d==0 and 0<p:
                    pos=2
                    neg=0
                if 0<d and 0<q:
                    pos=2
                    neg=1
                if d==0 and q==0:
                    pos=0
                    neg=1
                if 0<d and q<0:
                    pos=0
                    neg=3
            if fX(p)==0:
                if d<0 and 0<p:
                    pos=3
                    neg=0
                if d==0 and p==0:
                    pos=1
                    neg=0
                if d<0 and p<0:
                    pos=1
                    neg=2
                if d==0 and q<0:
                    pos=0
                    neg=2
                if 0<d and q<0:
                    pos=0
                    neg=3
            if fX(q)<0<fX(p):
                if d<0 and 0<p:
                    pos=3
                    neg=0
                if d==0 and 0<p:
                    pos=2
                    neg=0
                if 0<d and 0<q:
                    pos=2
                    neg=1
                if d==0 and p<0<q:
                    pos=1
                    neg=1
                if d<0 and p<0:
                    pos=1
                    neg=2
                if d==0 and q<0:
                    pos=0
                    neg=2
                if 0<d and q<0:
                    pos=0
                    neg=3
        
        if a<0:
            p = (-b+math.sqrt(b**2-3*a*c))/(3*a)
            q = (-b-math.sqrt(b**2-3*a*c))/(3*a)
            if 0<fX(p) or fX(q)<0 :
                if d<0:
                    pos=0
                    neg=1
                if d==0:
                    pos=0
                    neg=0
                if 0<d:
                    pos=1
                    neg=0
            if fX(p)==0:
                if 0<d and 0<p:
                    pos=3
                    neg=0
                if d==0 and p==0:
                    pos=1
                    neg=0
                if 0<d and p<0:
                    pos=1
                    neg=2
                if d==0 and q<0:
                    pos=0
                    neg=2
                if d<0 and q<0:
                    pos=0
                    neg=3
            if fX(q)==0:
                if 0<d and 0<p:
                    pos=3
                    neg=0
                if d==0 and 0<p:
                    pos=2
                    neg=0
                if d<0 and 0<q:
                    pos=2
                    neg=1
                if d==0 and q==0:
                    pos=0
                    neg=1
                if d<0 and q<0:
                    pos=0
                    neg=3
            if fX(p)<0<fX(q):
                if 0<d and 0<p:
                    pos=3
                    neg=0
                if d==0 and 0<p:
                    pos=2
                    neg=0
                if d<0 and 0<q:
                    pos=2
                    neg=1
                if d==0 and p<0<q:
                    pos=1
                    neg=1
                if 0<d and p<0:
                    pos=1
                    neg=2
                if d==0 and q<0:
                    pos=0
                    neg=2
                if d<0 and q<0:
                    pos=0
                    neg=3
    
    print(pos,neg)