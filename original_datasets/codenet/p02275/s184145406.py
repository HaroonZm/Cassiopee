def CountingSort(A,k):
    C=[0]*(k+1)
    for a in A:
        C[a]+=1
    for i in range(k):
        C[i+1]+=C[i]
    ret=[0]*len(A)
    for a in A[::-1]:
        ret[C[a]-1]=a
        C[a]-=1
    return ret
n=int(input())
A=list(map(int,input().split()))
print(*CountingSort(A,max(A)))