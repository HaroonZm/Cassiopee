def Judge(i):
    if i%15==0: return "FizzBuzz"
    if i%5==0:  return "Buzz"
    if i%3==0:  return "Fizz"
    return str(i)

while True:
    m,n=map(int,raw_input().split())
    if m==n==0:break
    L=range(1,m+1)
    j=0
    for i in range(1,n+1):
        c=raw_input()
	if len(L)>1:
            if Judge(i)!=c:
                del L[j]
                j%=len(L)
            else:
                j=(j+1)%len(L)
    print " ".join(map(str,L))