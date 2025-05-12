n=int(input())
h=list(map(int,input().split()))
judge = True

for i in range(n-1):
    if h[i]>h[i+1]:
        judge=False
        break
    elif h[i]!=h[i+1]:
        h[i+1]=h[i+1]-1

if judge:
    print("Yes")
else:
    print("No")