while True:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    seats=['#']*n
    persons=[input() for _ in range(m)]
    for p in persons:
        if p=='A':
            for i in range(n):
                if seats[i]=='#':
                    seats[i]=p
                    break
        elif p=='B':
            candidates=[i for i in range(n-1,-1,-1) if seats[i]=='#']
            placed=False
            for i in candidates:
                if (i>0 and seats[i-1]=='A') or (i<n-1 and seats[i+1]=='A'):
                    continue
                seats[i]=p
                placed=True
                break
            if not placed:
                for i in range(n):
                    if seats[i]=='#':
                        seats[i]=p
                        break
        elif p=='C':
            occupied=[i for i,c in enumerate(seats) if c!='#']
            if not occupied:
                mid=(n+1)//2 if n%2==1 else n//2+1
                seats[mid-1]=p
            else:
                placed=False
                for i_ in occupied:
                    if i_+1<n and seats[i_+1]=='#':
                        seats[i_+1]=p
                        placed=True
                        break
                    elif i_-1>=0 and seats[i_-1]=='#':
                        seats[i_-1]=p
                        placed=True
                        break
                if not placed:
                    for i in range(n):
                        if seats[i]=='#':
                            seats[i]=p
                            break
        else: # D
            occupied=[i for i,c in enumerate(seats) if c!='#']
            if not occupied:
                seats[0]=p
            else:
                max_dist=-1
                candidates=[]
                for i in range(n):
                    if seats[i]!='#': continue
                    dist=min([abs(i-o) for o in occupied])
                    if dist>max_dist:
                        max_dist=dist
                        candidates=[i]
                    elif dist==max_dist:
                        candidates.append(i)
                seats[candidates[0]]=p
    print(''.join(seats))