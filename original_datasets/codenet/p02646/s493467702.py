a,v = map(int,input().split())
b,w = map(int,input().split())

T = int(input())

if a==b:
    print("YES")

elif a<b:
    if v<=w:
        print("NO")
    else:
        if a+v*T>=b+w*T:
            print("YES")
        else:
            print("NO")

else:
    if v<=w:
        print("NO")
    else:
        if a-v*T<=b-w*T:
            print("YES")
        else:
            print("NO")