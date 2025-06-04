while True:
    line = input()
    N_M = line.split()
    N = int(N_M[0])
    M = int(N_M[1])
    if N == 0 and M == 0:
        break

    PCs = []
    for i in range(N):
        if i == 0:
            PCs.append(True)
        else:
            PCs.append(False)
    
    packets = []
    for i in range(M):
        t_s_d = input().split()
        t = int(t_s_d[0])
        s = int(t_s_d[1])
        d = int(t_s_d[2])
        packets.append([t, s, d])

    packets.sort()
    
    for packet in packets:
        t = packet[0]
        s = packet[1]
        d = packet[2]
        if PCs[s - 1]:
            PCs[d - 1] = True

    print(PCs.count(True))