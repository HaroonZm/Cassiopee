def get_input():
    return raw_input()

def parse_input(line):
    return list(map(int, line.split(" ")))

def should_exit(N, M):
    return (N, M) == (0, 0)

def init_computers(N):
    computers = [0 for _ in range(N+1)]
    computers[1] = 1
    return computers

def read_packets(M):
    packets = []
    for _ in range(M):
        packets.append(parse_input(get_input()))
    return packets

def sort_packets(packets):
    return sorted(packets)

def process_packet(computer, packet):
    t, s, d = packet
    if computer[s] == 1:
        computer[d] = 1

def process_packets(computer, packets):
    for packet in packets:
        process_packet(computer, packet)

def compute_result(computer):
    return sum(computer)

def output_result(result):
    print(result)

def main_loop():
    while should_continue():
        N, M = get_N_M()
        computers = init_computers(N)
        packets = get_sorted_packets(M)
        process_packets(computers, packets)
        result = compute_result(computers)
        output_result(result)

def should_continue():
    N, M = get_N_M_static()
    if should_exit(N, M):
        return False
    set_current_N_M(N, M)
    return True

_current_N = None
_current_M = None

def set_current_N_M(N, M):
    global _current_N, _current_M
    _current_N = N
    _current_M = M

def get_N_M():
    return _current_N, _current_M

def get_N_M_static():
    line = get_input()
    N, M = parse_input(line)
    return N, M

def get_sorted_packets(M):
    packets = read_packets_for_static(M)
    return sort_packets(packets)

def read_packets_for_static(M):
    packets = []
    for _ in range(M):
        packets.append(parse_input(get_input()))
    return packets

def run():
    while True:
        N, M = parse_input(get_input())
        if should_exit(N, M):
            break
        computers = init_computers(N)
        packets = []
        for _ in range(M):
            packets.append(parse_input(get_input()))
        packets = sort_packets(packets)
        process_packets(computers, packets)
        result = compute_result(computers)
        output_result(result)

run()