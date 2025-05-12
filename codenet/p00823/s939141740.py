def mole():
    global p
    global s
    num=term()
    while len(s)>p:
        if s[p]=='+':
            p+=1
            num+=term()
        else:
            break
    return num

def term():
    global p
    global s
    num=factor()
    while len(s)>p:
        if s[p]=='*':
            p+=1
            num*=factor()
        else:
            break
    return num

def factor():
    global p
    global s
    num=0
    if len(s)>p and s[p]=='(':
        p+=1
        num=mole()
        p+=1
    else:
        return number()
    return num

def number():
    global p
    global s
    num=0
    if s[p].isdigit():
        while len(s)>p and s[p].isdigit():
            num*=10
            num+=int(s[p])
            p+=1
    elif s[p]!='(' and s[p]!=')':
        tmp=''
        while len(s)>p and s[p]!='(' and s[p]!=')' and s[p]!='+' and s[p]!='*':
            tmp+=s[p]
            p+=1
        if tmp in dic:
            num=int(dic[tmp])
        else:
            global f
            f=False
    return num

def pre():
    global s
    s=list(s)
    i=1
    while True:
        if i>=len(s):
            break
        if s[i].isdigit():
            s.insert(i,'*')
            i+=1
            while i+1<len(s) and s[i+1].isdigit():
                i+=1
        elif (s[i]=='(' or s[i].isupper()) and (s[i-1]!='('):
            s.insert(i,'+')
            i+=1
        i+=1
    s=''.join(s)

dic={}
while True:
    s=input()
    if s=='END_OF_FIRST_PART':
        break
    a,b=s.split()
    dic[a]=b
while True:
    s=input()
    if s=='0':
        break
    p=0
    f=True
    pre()
    ans=mole()
    print(ans if f else 'UNKNOWN')