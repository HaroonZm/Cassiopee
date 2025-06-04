def read_n():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def calculate_total(a):
    return sum(a)

def generate_b(a, k, N):
    return [x + k - (N - 1) for x in a]

def calc_cnt(b, N):
    cnt = 0
    for x in b:
        cnt += (x + N) // (N + 1)
    return cnt

def is_ok(a, k, N):
    b = generate_b(a, k, N)
    cnt = calc_cnt(b, N)
    return cnt <= k

def find_min_k(a, N, tot):
    start_k = max(0, tot - N * (N - 1))
    for k in range(start_k, tot + 1):
        if is_ok(a, k, N):
            return k
    return 0

def output_result(k):
    print(k)

def main():
    N = read_n()
    a = read_a()
    tot = calculate_total(a)
    ret = find_min_k(a, N, tot)
    output_result(ret)

if __name__ == '__main__':
    main()