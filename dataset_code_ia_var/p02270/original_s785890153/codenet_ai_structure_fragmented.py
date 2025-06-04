def read_input():
    N, K = map(int, input().split())
    W = [int(input()) for _ in range(N)]
    return N, K, W

def get_min_capacity(W):
    return max(W)

def get_max_capacity():
    return 10 ** 9

def can_load_all(N, W, K, P):
    M = calculate_trucks_needed(N, W, P)
    return M <= K

def calculate_trucks_needed(N, W, P):
    M = 0
    i = 0
    while not all_loaded(i, N):
        i, M = load_one_truck(i, N, W, P, M)
    return M

def all_loaded(i, N):
    return i >= N

def load_one_truck(i, N, W, P, M):
    mass = 0
    i = load_packages(i, N, W, P, mass)
    M += 1
    return i, M

def load_packages(i, N, W, P, mass):
    while more_to_load(i, N) and can_add_package(mass, W[i], P):
        mass += W[i]
        i += 1
    return i

def more_to_load(i, N):
    return i < N

def can_add_package(mass, package_weight, P):
    return mass + package_weight <= P

def binary_search_min_capacity(N, K, W):
    P_MIN = get_min_capacity(W)
    P_MAX = get_max_capacity()
    while less_than(P_MIN, P_MAX):
        P = get_mid_capacity(P_MIN, P_MAX)
        if enough_trucks(N, W, K, P):
            P_MAX = update_max(P)
        else:
            P_MIN = update_min(P)
    return P_MIN

def less_than(a, b):
    return a < b

def get_mid_capacity(P_MIN, P_MAX):
    return (P_MAX + P_MIN) // 2

def enough_trucks(N, W, K, P):
    return can_load_all(N, W, K, P)

def update_max(P):
    return P

def update_min(P):
    return P + 1

def output_result(result):
    print(result)

def main():
    N, K, W = read_input()
    result = binary_search_min_capacity(N, K, W)
    output_result(result)

main()