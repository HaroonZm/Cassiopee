while True:
    m,n_min,n_max = list(map(int,input().split()))
    if m == 0:
        break
    v  = [int(input()) for _ in range(m)]
    
    max_gap = 0
    max_index = n_min

    for i in range(n_min,n_max+1):
        gap = v[i-1]-v[i]

        
        if gap > max_gap:
            max_gap = gap
            max_index = i
        elif gap == max_gap:
            max_index = i
            
    
    print(max_index)