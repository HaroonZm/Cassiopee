s = int(input())
m = [0]*10**7
m[s]=1
a = 1

while True:
    a +=1
    if s%2==0:
        s//=2
    else:
        s=3*s+1
    if m[s]==1:
        print(a)
        exit()
    else:
        m[s]=1