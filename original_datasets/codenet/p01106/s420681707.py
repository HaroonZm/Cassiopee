while 1:
    n,a,b=map(int,input().split())
    if n==0:
        break
    h_pos=[a]
    all=2**n
    for i in range(n):
        if 1<=h_pos[-1]<=all//4:
            h_pos.append(all//4+all//4-h_pos[-1]+1)
        elif all//4+1<=h_pos[-1]<=all//2:
            h_pos.append(all//2-h_pos[-1]+1)
        elif all//2+1<=h_pos[-1]<=3*all//4:
            h_pos.append(h_pos[-1]-all//2)
        else:
            h_pos.append(h_pos[-1]-3*all//4+all//4)
        all//=2
    h_pos=h_pos[::-1]
    all=2**n
    s=''
    for i in range(n):
        if 1<=b<=all//2:
            if h_pos[i+1]<=2**(i+1)//2:
                b=all//2-b+1
                s+='L'
            else:
                s+='R'
        else:
            if h_pos[i+1]<=2**(i+1)//2:
                b=all-b+1
                s+='R'
            else:
                b=b-all//2
                s+='L'
        all//=2
    print(s)