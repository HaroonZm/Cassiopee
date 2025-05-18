q = int(input())
 
MASK = (1 << 64) -1

mask = []
for i in range(q):
    retmask = 0
    ret = [i for i in map(int,input().split())]
    for i in range(1,ret[0]+1):
        retmask += 1 << ret[i]
    mask.append(retmask)

q = int(input())
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
        n = (n | mask[query[1]])
 
    elif query[0] == 2:
        n = n & (~ mask[query[1]] & MASK)
         
    elif query[0] == 3:
        n = n ^ mask[query[1]]
         
    elif query[0] == 4:
        if n & mask[query[1]] == mask[query[1]]:
            print(1)
        else:
            print(0)

        
            
    elif query[0] == 5:
        if n & mask[query[1]] > 0:
            print(1)
        else:
            print(0)
             
    elif query[0] == 6:
        if n & mask[query[1]] == 0:
            print(1)
        else:
            print(0)
            
    elif query[0] == 7:
        print(bin(n & mask[query[1]]).count("1"))
        
         
    elif query[0] == 8:
        print(mask[query[1]] & n)