while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    seats=['#']*n
    for _ in range(m):
        p=input()
        if p=='A':
            for i in range(n):
                if seats[i]=='#':
                    seats[i]='A'
                    break
        elif p=='B':
            candidates=[]
            for i in range(n-1,-1,-1):
                if seats[i]=='#':
                    left=A_pos=right=False
                    if i>0:
                        left=seats[i-1]=='A'
                    if i<n-1:
                        right=seats[i+1]=='A'
                    if not (left or right):
                        candidates.append(i)
            if candidates:
                seats[candidates[0]]='B'
            else:
                for i in range(n):
                    if seats[i]=='#':
                        seats[i]='B'
                        break
        elif p=='C':
            occupied = [i for i,v in enumerate(seats) if v!='#']
            if not occupied:
                if n%2==1:
                    mid=(n+1)//2 -1
                else:
                    mid=n//2
                seats[mid]='C'
            else:
                placed=False
                for pos in occupied:
                    right=pos+1
                    left=pos-1
                    if right<n and seats[right]=='#':
                        seats[right]='C'
                        placed=True
                        break
                    if left>=0 and seats[left]=='#':
                        seats[left]='C'
                        placed=True
                        break
                if not placed:
                    for i in range(n):
                        if seats[i]=='#':
                            seats[i]='C'
                            break
        else: # p=='D'
            occupied = [i for i,v in enumerate(seats) if v!='#']
            if not occupied:
                seats[0]='D'
            else:
                max_dist=-1
                candidate_positions=[]
                for i in range(n):
                    if seats[i]!='#':
                        continue
                    dist=min([abs(i-o) for o in occupied])
                    if dist>max_dist:
                        max_dist=dist
                        candidate_positions=[i]
                    elif dist==max_dist:
                        candidate_positions.append(i)
                seats[candidate_positions[0]]='D'
    print(''.join(seats))