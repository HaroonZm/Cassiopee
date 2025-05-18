for j in range(20):
    try:
        d = int(input())
        size = 0
        
        for i in range(600//d - 1):
            #print(i, i*d, (i*d)**2, d, size)
            i += 1
            size += ((i*d)**2) *d
            
        print(int(size))
        
    except:     break