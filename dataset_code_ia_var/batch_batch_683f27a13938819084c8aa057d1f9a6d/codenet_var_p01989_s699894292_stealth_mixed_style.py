from itertools import combinations as C

def f(s):
    r=0
    i=len(s)
    def z(x): return x[0]!='0' or x=='0'
    def y(x): return 0<=int(x)<=255
    for u in C(range(1,i),3):
        j,k,l = u
        x = [s[:j],s[j:k],s[k:l],s[l:]]
        if all(map(z,x)) and all(y(q) for q in x): r+=1
    return r

print(f(input()))