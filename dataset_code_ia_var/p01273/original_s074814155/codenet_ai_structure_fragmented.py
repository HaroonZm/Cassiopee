def read_input():
    return list(map(int, input().split()))

def is_termination_case(N, M):
    return N == 0 and M == 0

def read_logs(M):
    logs = []
    for _ in range(M):
        log = parse_log(input())
        logs.append(log)
    return logs

def parse_log(line):
    t, s, d = map(int, line.split())
    return create_log_entry(t, s, d)

def create_log_entry(t, s, d):
    return (t, s - 1, d - 1)

def initialize_infected(N):
    infected = [0] * N
    return set_initial_infected(infected)

def set_initial_infected(infected):
    infected[0] = 1
    return infected

def process_logs(infected, logs):
    sorted_logs = sort_logs(logs)
    for log in sorted_logs:
        infected = infect_if_possible(infected, log)
    return infected

def sort_logs(logs):
    return sorted(logs)

def infect_if_possible(infected, log):
    t, s, d = log
    if check_infected(infected, s):
        infected = infect_destination(infected, d)
    return infected

def check_infected(infected, s):
    return infected[s]

def infect_destination(infected, d):
    infected[d] = 1
    return infected

def count_infected(infected):
    return sum(infected)

def output_result(count):
    print(count)

def main_loop():
    while True:
        N, M = read_input()
        if is_termination_case(N, M):
            break
        logs = read_logs(M)
        infected = initialize_infected(N)
        infected = process_logs(infected, logs)
        total_infected = count_infected(infected)
        output_result(total_infected)

main_loop()