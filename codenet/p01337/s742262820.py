n=int(input())
def f(a,b,c,d):
    return lambda x:a*x**3+b*x**2+c*x+d
for i in range(n):
    a,b,c,d=map(int,input().split())
    fx=f(a,b,c,d)
    D=b**2-3*a*c
    if D<=0 :
        if d==0:
            pl=mi=0
        elif (a>0 and d<0) or (a<0 and d>0):
            pl,mi=1,0
        elif (a<0 and d<0) or (a>0 and d>0):
            pl,mi=0,1
    else:
        if a>0:
            al=(-b-D**0.5)/(3*a)
            be=(-b+D**0.5)/(3*a)
            if (fx(al)<0 or fx(be)>0) and d==0:
                pl=mi=0
            elif ((fx(al)<0 or fx(be)>0) and d>0) or (fx(be)==0 and d==0 and be==0):
                pl,mi=0,1
            elif (fx(al)==0 or (fx(al)>0 and fx(be)<0)) and d==0 and be<0:
                pl,mi=0,2
            elif (fx(al)==0 or fx(be)==0 or (fx(al)>0 and fx(be)<0)) and d>0 and be<0:
                pl,mi=0,3
            elif ((fx(al)<0 or fx(be)>0) and d<0) or (fx(al)==0 and d==0 and al==0):
                pl,mi=1,0
            elif fx(al)>0 and fx(be)<0 and d==0 and al<0 and be>0:
                pl=mi=1
            elif (fx(al)==0 or (fx(al)>0 and fx(be)<0)) and d<0 and al<0:
                pl,mi=1,2
            elif (fx(be)==0 or (fx(al)>0 and fx(be)<0)) and d==0 and al>0:
                pl,mi=2,0
            elif (fx(be)==0 or (fx(al)>0 and fx(be)<0)) and d>0 and be>0:
                pl,mi=2,1
            elif ((fx(al)==0 and al>0) or fx(be)==0 or (fx(al)>0 and fx(be)<0 and al>0)) and d<0:
                pl,mi=3,0
        else:
            al=(-b+D**0.5)/(3*a)
            be=(-b-D**0.5)/(3*a)
            if (fx(al)>0 or fx(be)<0) and d==0:
                pl=mi=0
            elif ((fx(al)>0 or fx(be)<0) and d<0) or (fx(be)==0 and d==0 and be==0):
                pl,mi=0,1
            elif (fx(al)==0 or (fx(al)<0 and fx(be)>0)) and d==0 and be<0:
                pl,mi=0,2
            elif (fx(al)==0 or fx(be)==0 or (fx(al)<0 and fx(be)>0)) and d<0 and be<0:
                pl,mi=0,3
            elif ((fx(al)>0 or fx(be)<0) and d>0) or (fx(al)==0 and d==0 and al==0):
                pl,mi=1,0
            elif fx(al)<0 and fx(be)>0 and d==0 and al<0 and be>0:
                pl=mi=1
            elif (fx(al)==0 or (fx(al)<0 and fx(be)>0)) and d>0 and al<0:
                pl,mi=1,2
            elif (fx(be)==0 or (fx(al)<0 and fx(be)>0)) and d==0 and al>0:
                pl,mi=2,0
            elif (fx(be)==0 or (fx(al)<0 and fx(be)>0)) and d<0 and be>0:
                pl,mi=2,1
            elif (fx(al)==0 or fx(be)==0 or (fx(al)<0 and fx(be)>0)) and d>0 and al>0:
                pl,mi=3,0
    print(pl,mi)