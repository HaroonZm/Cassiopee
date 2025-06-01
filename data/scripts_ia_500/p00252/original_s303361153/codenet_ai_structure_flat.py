b1,b2,b3=map(int,input().split())
if b1==1:
    if b2==1:
        if b3==0:
            print("Open")
        else:
            print("Close")
    else:
        if b2==0:
            if b3==1:
                print("Open")
            else:
                print("Close")
        else:
            print("Close")
else:
    if b1==0:
        if b2==1:
            print("Close")
        else:
            if b2==0:
                if b3==1:
                    print("Open")
                else:
                    print("Close")
            else:
                print("Close")
    else:
        print("Close")