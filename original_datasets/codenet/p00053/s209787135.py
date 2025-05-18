Max=1000000
Sqrt=1000
def prime_number():
    count=[]
    prime=[True for i in range(Max)]
    for i in range(4,Max,2):
        prime[i]=False
    for i in range(3,Sqrt,2):
        if prime[i]==True:
            for j in range(i*2,Max,i):
                prime[j]=False       
    for k in range(2,Max):
        if prime[k]==True:
            count.append(k)
    return count
box=prime_number()
while 1:
    try:
        ans=0
        N=int(input())
        if N==0:break
        for i in range(N):
            ans +=box[i]
        print(ans)
    except:break