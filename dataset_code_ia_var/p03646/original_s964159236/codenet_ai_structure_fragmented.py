def read_input():
    return int(input())

def initialize_moto():
    return list(range(0, 49)) + [50]

def calculate_ka(k):
    return k % 50

def find_min_index(arr):
    min_value = min(arr)
    return arr.index(min_value)

def increment_min(moto):
    idx = find_min_index(moto)
    moto[idx] += 51
    return idx

def decrement_all(moto):
    for j in range(50):
        moto[j] -= 1

def process_ka_iterations(moto, ka):
    for _ in range(ka):
        increment_min(moto)
        decrement_all(moto)

def calculate_k_div_50(k):
    return k // 50

def increment_all(moto, value):
    for j in range(50):
        moto[j] += value

def format_output(moto):
    return " ".join(map(str, moto))

def main():
    k = read_input() - 1
    moto = initialize_moto()
    ka = calculate_ka(k)
    process_ka_iterations(moto, ka)
    k_div_50 = calculate_k_div_50(k)
    increment_all(moto, k_div_50)
    print(50)
    print(format_output(moto))

main()