n=int(input())
if n==1:
    print(1)
    exit()
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
    return arr
so=[]
ka=[]
for i in range(2,n+1):
    a=factorization(i)
    for j in a:
        if not j[0] in so:
            so.append(j[0])
            ka.append(j[1])
        else:
            ka[so.index(j[0])]+=j[1]
ans=1
for i in ka:
    ans*=(i+1)%1000000007
print(ans%1000000007)