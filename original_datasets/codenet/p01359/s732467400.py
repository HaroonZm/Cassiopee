#! /usr/bin/python

def bm_search(dat, q, l, r):
    #print q, l, r
    if l == r:
        if q <= dat[l][2]:
            return int(l)
        else:
            return l+1
    elif q <= dat[l+(r-l)/2][2]:
        return bm_search(dat, q, l, l+(r-l)/2)
    elif dat[l+(r-l)/2][2] < q:
        return bm_search(dat, q, l+(r-l)/2+1, r)

while True:
    (N, Q) = map(int, raw_input().split())
    if N == 0: break
    
    dat = []
    for i in range(N):
        dat.append(raw_input().split())
    for i in range(N):
        dat[i][1] = int(dat[i][1])
        dat[i][2] = int(dat[i][2])
    dat.sort(key = lambda x:x[2])
        
    for i in range(Q):
        q = int(raw_input())
        p = bm_search(dat, q, 0, N-1)
        if p < N and dat[p][1] > dat[p][2]-q:
            print dat[p][0], dat[p][1]-(dat[p][2]-q)
        else:
            print "Unknown"