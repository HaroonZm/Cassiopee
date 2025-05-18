x,a,b = map(int,input().split())
for i in range(int(input())):
    w = input()
    if w == "nobiro":
        x = max(0,x+a)
    elif w == "tidime":
        x = max(0,x+b)
    else:
        x = 0
print(x)