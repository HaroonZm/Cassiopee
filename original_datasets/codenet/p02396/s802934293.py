x=int(input())
for i in range(10000):
    if x in range(1,10001):
        n=i+1
        print("Case "+str(n)+": "+str(x))
        x=int(input())