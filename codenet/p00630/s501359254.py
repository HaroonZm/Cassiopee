while True:
    a,b=input().split()
    if b=='X':
        break
    a=list(a)
    if ('_' in a) and (b=='U' or b=='L'):
        c=0
        for i in range(len(a)):
            if i==0 and b=='U':
                a[i]=a[i].upper()
            elif a[i]=='_':
                c+=1
            elif c==1:
                a[i]=a[i].upper()
                c=0
        a=[i for i in a if i!='_']
    elif b=='U':
        a[0]=a[0].upper()
    elif b=='L':
        a[0]=a[0].lower()
    else:
        s=0
        for i in range(len(a)):
            if i==0:
                a[0]=a[0].lower()
                s+=1
            elif a[s].isupper():
                a[s]=a[s].lower()
                a.insert(s,'_')
                s+=2
            else:
                s+=1
    for i in range(len(a)):
        if i==len(a)-1:
            print(a[i])
        else:
            print(a[i],end='')