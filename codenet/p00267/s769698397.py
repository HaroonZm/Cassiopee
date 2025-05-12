while 1:
    if input()=='0':break
    a=sorted(list(map(int,input().split())))[::-1]
    b=sorted(list(map(int,input().split())))[::-1]
    p=0;c=0;
    for i,x in enumerate(a):
        if i/2<c:print(i);break
        if x<=b[p]:p+=1
        else:c+=1
    else:print('NA')