h,w,K = map(int,input().split())
c = [list(map(str, input().strip())) for i in range(h)]

count = 0
he = [0 for i in range(h)]
for i in range(2**h):
    we = [0 for i in range(w)]

    h_set = set(range(h))
    for j in range(h):
        if(he[j] == 0):
            h_set.discard(j)
    h_a = list(h_set)
    for j in range(h):
        if(he[h-j-1] == 0):
            he[h-j-1] = 1
            for k in range(h-j,h):
                he[k] = 0
            break

    for j in range(2**w):
        w_set = set(range(w))
        for k in range(w):
            if(we[k] == 0):
                w_set.discard(k)
        w_a = list(w_set)
        for k in range(w):
            if(we[w-k-1] == 0):
                we[w-k-1] = 1
                for m in range(w-k,w):
                    we[m] = 0
                break

        black = 0
        for x in h_a:
            for y in w_a:
                if(c[x][y] == '#'):
                    black += 1
        if(black == K):
            count += 1
 
        

print(count)