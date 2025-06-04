dvals = {'m':1000,'c':100,'x':10,'i':1}
order = ['m','c','x','i']
def to_val(s):
    res=0
    i=0
    while i<len(s):
        if s[i] in '23456789' and i+1<len(s):
            res += int(s[i])*dvals[s[i+1]]
            i+=2
        else:
            res += dvals[s[i]]
            i+=1
    return res
def to_mcxi(val):
    res=[]
    for c in order:
        q,val = divmod(val,dvals[c])
        if q>1: res.append(str(q)+c)
        elif q==1: res.append(c)
    return ''.join(res)
n=int(input())
for _ in range(n):
    a,b=input().split()
    print(to_mcxi(to_val(a)+to_val(b)))