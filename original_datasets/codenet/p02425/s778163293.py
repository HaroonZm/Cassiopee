q = int(input())

MASK = (1 << 64) -1
n = 0
for i in range(q):
    query = [i for i in map(int,input().split())]
    if query[0] == 0:
        temp = 1 << query[1]
        if (n & temp) == 0:
            print(0)
        else:
            print(1)

    elif query[0] == 1:
        temp = 1 << query[1]
        n = (n | temp)

    elif query[0] == 2:
        temp = 1 << query[1]
        n = n & (~temp & MASK)
        
    elif query[0] == 3:
        temp = 1 << query[1]
        n = n ^ temp
        
    elif query[0] == 4:
        if n == MASK:
            print(1)
        else:
            print(0)
    elif query[0] == 5:
        if n & MASK > 0:
            print(1)
        else:
            print(0)
            
    elif query[0] == 6:
        if n == 0:
            print(1)
        else:
            print(0)
            
    elif query[0] == 7:
        temp = n
        one = 1
        counter = 0
        for i in range(64):
            if one & temp == 1:
                counter += 1
            temp = temp >> 1
        print(counter)
        
    elif query[0] == 8:
        print(n)