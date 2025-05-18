while 1:
    n=input()
    if n==0: break
    ar=raw_input()+' '
    for i in range(n):
        cnt=1
        tmp=''
        for i in range(len(ar)-1):
            if ar[i]==ar[i+1]:
                cnt+=1
            else:
                tmp+="%d%s"%(cnt,ar[i])
                cnt=1
        ar=tmp+' '
    print ar.rstrip()