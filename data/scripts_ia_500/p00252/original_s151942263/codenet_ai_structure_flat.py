a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a==1 and b==1 and c==0:
    print("Open")
else:
    if a==0 and b==0 and c==1:
        print("Open")
    else:
        print("Close")