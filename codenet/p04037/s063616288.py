N=int(input())
A=list(map(int,input().split()))
A.append(0)
A.sort()
winner=""
for i in range(N+1):
    if A[N-i]>i:
        if (A[N-i]-i)%2==0:
            winner="First"
        else:
            winner="Second"
    elif A[N-i]==i:
        if (A[N-i+1]-A[N-i])%2==1:
            winner="First"
            break
        else:
            count=0
            for j in range(N-i,-1,-1):
                if A[j]==i:
                    count+=1
                else:
                    break
            if count%2==1:
                winner="First"
            else:
                winner="Second"
            break
    else:
        break

print(winner)