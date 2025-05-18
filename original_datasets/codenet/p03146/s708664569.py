def func(n):
    return n//2 if n%2==0 else 3*n+1

s = int(input())

i=0
sl = [s]
while True:
    n = func(sl[-1])
    if( n  in sl):
        print(i+2)
        exit()
    sl.append(n)
    #sl = list(set(sl))
    i+=1