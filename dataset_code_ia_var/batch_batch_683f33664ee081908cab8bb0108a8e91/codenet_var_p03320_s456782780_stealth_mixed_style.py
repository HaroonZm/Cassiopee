k = int(input())

AnS = [x for x in range(1,10)]
def sumdig(z): return sum(map(int,str(z)))
for X in range(1,15):
    b = [None]*100000
    n,d=pow(10,X),eval("'9'"*X)
    I=0
    while I<10000:
        nu = I*n+d
        s = ''.join(str(nu))
        s_ = 0
        j=0
        while j<len(s):
            s_ = s_ + int(s[j])
            j=j+1
        res = nu/s_
        b[I]=res
        if I:
            if res<b[I-1]:
                try:
                    AnS.pop()
                except:
                    pass
                break
            else:
                if nu not in AnS:
                    AnS.append(nu)
        else:
            if nu not in AnS:
                AnS.append(nu)
        I+=1

for i in range(k):
    print(AnS[i])