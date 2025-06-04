def read_N_M():
    return map(int, input().split())

def is_end(N, M):
    return N == 0 and M == 0

def init_PCs(N):
    PCs = [False] * N
    set_infected(PCs, 0)
    return PCs

def set_infected(PCs, idx):
    PCs[idx] = True

def read_packet():
    t, s, d = map(int, input().split())
    return t, s, d

def read_all_packets(M):
    Packets = {}
    for _ in range(M):
        t, s, d = read_packet()
        store_packet(Packets, t, s, d)
    return Packets

def store_packet(Packets, t, s, d):
    Packets[t] = (s, d)

def get_sorted_packet_keys(Packets):
    return sorted(Packets)

def should_infect(PCs, src_idx):
    return PCs[src_idx - 1]

def infect_destination(PCs, dst_idx):
    set_infected(PCs, dst_idx - 1)

def process_packets(Packets, PCs):
    for key in get_sorted_packet_keys(Packets):
        s, d = Packets[key]
        if should_infect(PCs, s):
            infect_destination(PCs, d)

def count_infected(PCs):
    return PCs.count(True)

def main_loop():
    while True:
        N, M = read_N_M()
        if is_end(N, M):
            break
        PCs = init_PCs(N)
        Packets = read_all_packets(M)
        process_packets(Packets, PCs)
        print(count_infected(PCs))

main_loop()