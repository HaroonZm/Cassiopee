def read_input_n():
    return int(input())

def read_input_a():
    return list(map(int, input().split()))

def generate_powers_of_two(limit):
    p = []
    for j in range(limit):
        p.append(pow(2, j))
    return p

def compute_total_xor(a, n):
    t = 0
    for i in range(n):
        t = t ^ a[i]
    return t

def compute_xor_with_total(a_elem, t):
    return a_elem ^ t

def compute_ans_for_index(a_elem, t, p):
    ans = 0
    for j in range(len(p)):
        ans += p[j] * (((a_elem ^ t) // p[j]) % 2)
    return ans

def print_ans_space(ans, is_last):
    if is_last:
        print(ans)
    else:
        print(ans, end=" ")

def main():
    n = read_input_n()
    a = read_input_a()
    p = generate_powers_of_two(30)
    t = compute_total_xor(a, n)
    for i in range(n):
        a_elem = a[i]
        xor_res = compute_xor_with_total(a_elem, t)
        ans = compute_ans_for_index(a_elem, t, p)
        is_last = (i == n - 1)
        print_ans_space(ans, is_last)

main()