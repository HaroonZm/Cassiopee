N=int(input())
X=list(map(int,input().split()))

X_sort=sorted(X)

med_n=X_sort[N//2-1]
med_p=X_sort[N//2]

for i in range(N):
    if X[i]<=med_n:
        print(med_p)
    else:
        print(med_n)