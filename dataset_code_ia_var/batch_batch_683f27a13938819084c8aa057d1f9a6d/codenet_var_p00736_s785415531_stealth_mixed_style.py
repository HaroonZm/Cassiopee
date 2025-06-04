def parens_split(expr):
    i=0;j=0
    while 1:
        if expr[i]=='(':
            j+=1
        if expr[i]==')':
            j-=1
        if (j==1) and (expr[i] in '+*'):
            return expr[1:i],expr[i],expr[i+1:-1]
        i+=1

def OR(*args):
    a,b=args
    match a:
        case '0': return b
        case '1': return '1' if b=='0' else b
        case '2': return '2'

def And_(a,b):
    if a=='0':return '0'
    if a=='1':
        if b=='0':return '0'
        else: return '1'
    if a=='2':
        return b

def NEG(x):
    if x=='1':return '1'
    elif x=='0':return '2'
    else:return '0'

def calc(formula,pp,qq,rr):
    if formula in {'0','1','2'}:return formula
    if formula=='P':return pp
    if formula=='Q':return qq
    if formula=='R':return rr

    if formula.startswith("("):
        [fa,sig,fb]=parens_split(formula)
        a=calc(fa,pp,qq,rr)
        b=calc(fb,pp,qq,rr)
        if sig=='+':return OR(a,b)
        if sig=='*':return And_(a,b)
    elif formula[0]=='-':
        return NEG(calc(formula[1:],pp,qq,rr))

if __name__=="__main__":
    get = lambda: input().strip()
    while 1:
        f=get()
        if f=='.': break
        s=0
        for a in range(3):
          for b in range(3):
            r=[calc(f,str(a),str(b),str(c)) for c in range(3)]
            s += r.count('2')
        print(s)