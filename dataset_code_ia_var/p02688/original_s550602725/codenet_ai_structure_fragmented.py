def get_n_k():
    return map(int, input().split())

def read_d():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def add_unique(have, value):
    if value not in have:
        have.append(value)

def process_k_times(k, have):
    for _ in range(k):
        process_one_d(have)

def process_one_d(have):
    d = read_d()
    a = read_a()
    process_a_values(d, a, have)

def process_a_values(d, a, have):
    for j in range(d):
        add_unique(have, a[j])

def compute_output(n, have):
    return n - len(have)

def display_result(result):
    print(result)

def main():
    n, k = get_n_k()
    have = []
    process_k_times(k, have)
    output = compute_output(n, have)
    display_result(output)

if __name__ == "__main__":
    main()