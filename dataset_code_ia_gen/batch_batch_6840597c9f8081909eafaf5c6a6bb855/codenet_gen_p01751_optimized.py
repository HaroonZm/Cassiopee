a,b,c=map(int,input().split())
period=a+b
for t in range(61):
    time=60*t+c
    mod=time%period
    if mod<=a:
        print(time)
        break
else:
    print(-1)