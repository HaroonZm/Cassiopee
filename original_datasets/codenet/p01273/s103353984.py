"""
Created on Tue Jun 14 15:56:37 2016

"""
while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    
    PCs = [False] * N
    PCs[0] = True
    Packets = {}
    for _ in range(M):
        t, s, d = map(int, input().split())
        Packets[t] = (s, d)
    
    for key in sorted(Packets):
        if PCs[Packets[key][0] - 1] == True:
            PCs[Packets[key][1] - 1] = True
#            print('PC'+str(Packets[key][1])+' is infected')
            
    print(PCs.count(True))