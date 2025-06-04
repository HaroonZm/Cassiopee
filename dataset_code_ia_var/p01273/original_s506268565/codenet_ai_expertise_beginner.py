while True:
    line = raw_input()
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break

    computer = [0] * (N + 1)
    computer[1] = 1

    packets = []
    for i in range(M):
        t, s, d = map(int, raw_input().split())
        packets.append((t, s, d))

    packets.sort()

    for packet in packets:
        t, s, d = packet
        if computer[s] == 1:
            computer[d] = 1

    print sum(computer)