while 1:
    s=list(map(str,input().split()))
    if s[0]=="#":break
    if int(s[1])==31 and int(s[2])>=5 or int(s[1])>=32:
        s[0]="?"
        s[1]=str(int(s[1])-30)
    print(' '.join(map(str, s)))