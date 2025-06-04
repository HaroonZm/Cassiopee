def read_input_line():
    return input()

def parse_n_k(line):
    n, k = map(int, line.split())
    return n, k

def read_next_value():
    return int(input())

def build_array(n):
    array = []
    for _ in range(n):
        array.append(read_next_value())
    return array

def should_process_inputs(n, k):
    return not (n == 0 and k == 0)

def process_initial_k_elements(array, k):
    k_sum = 0
    for i in range(k):
        k_sum += array[i]
    return k_sum

def update_max_sum(k_sum, a, previous_a, maximam):
    new_sum = k_sum + a - previous_a
    maximam = max(maximam, new_sum)
    return new_sum, maximam

def process_remaining_elements(array, k, k_sum):
    maximam = 0
    for num in range(k, len(array)):
        a = array[num]
        previous_a = array[num - k]
        k_sum, maximam = update_max_sum(k_sum, a, previous_a, maximam)
    return maximam

def fun(n, k):
    arr = build_array(n)
    if k > n:
        print(0)
        return
    k_sum = process_initial_k_elements(arr, k)
    maximam = k_sum if n == k else 0
    if n > k:
        maximam = process_remaining_elements(arr, k, k_sum)
    print(maximam)

def main_loop():
    for _ in range(5):
        line = read_input_line()
        n, k = parse_n_k(line)
        if should_process_inputs(n, k):
            fun(n, k)
        else:
            break

main_loop()