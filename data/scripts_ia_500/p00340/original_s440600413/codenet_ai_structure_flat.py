a,b,c,d=map(int,input().split())
if a==b and c==d:
    print('yes')
else:
    if a==c and b==d:
        print('yes')
    else:
        if a==d and b==c:
            print('yes')
        else:
            if a==b==c==d:
                print('yes')
            else:
                print('no')