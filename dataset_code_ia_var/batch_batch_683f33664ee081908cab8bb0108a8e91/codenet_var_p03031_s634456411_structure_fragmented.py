import itertools

def read_input():
    N, M = parse_initial_input(input())
    switches = parse_switches([input() for _ in range(M)])
    p = parse_p(input())
    return N, M, switches, p

def parse_initial_input(line):
    return map(int, line.split())

def parse_switches(lines):
    return [list(map(int, line.split())) for line in lines]

def parse_p(line):
    return [int(x) for x in line.split()]

def generate_combinations(N):
    return itertools.product([0, 1], repeat=N)

def check_condition_for_all_switches(combo, switches, p):
    for j in range(len(switches)):
        if not check_switch(combo, switches[j], p[j]):
            return False
    return True

def check_switch(combo, switch, required_parity):
    count_on = count_switch_on(combo, switch)
    return (count_on % 2) == required_parity

def count_switch_on(combo, switch):
    count = 0
    for k in switch[1:]:
        count += combo[k-1]
    return count

def solve():
    N, M, switches, p = read_input()
    ans = count_valid_combinations(N, switches, p)
    print(ans)

def count_valid_combinations(N, switches, p):
    ans = 0
    for combo in generate_combinations(N):
        if check_condition_for_all_switches(combo, switches, p):
            ans += 1
    return ans

solve()