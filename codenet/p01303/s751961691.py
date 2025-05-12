for _ in range(int(input())):
    x,y,w,h=map(int,input().split())
    c=0
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if x<=a<=x+w and y<=b<=y+h:c+=1
    print(c)