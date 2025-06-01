b1 = int(input())
b2 = int(input())
b3 = int(input())

if b1 == 1:
    if b2 == 1:
        print('Open')
    else:
        print('Close')
else:
    if b2 == 0:
        if b3 == 1:
            print('Open')
        else:
            print('Close')
    else:
        print('Close')