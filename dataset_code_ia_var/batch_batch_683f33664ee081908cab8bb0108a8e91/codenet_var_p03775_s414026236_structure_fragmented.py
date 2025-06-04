def get_input():
    return input()

def to_int(s):
    return int(s)

def calc_sqrt(n):
    return n ** 0.5

def get_range_end(n):
    return int(calc_sqrt(n)) + 1

def is_divisor(n, i):
    return n % i == 0

def get_other_divisor(n, i):
    return int(n / i)

def append_divisors(ans, i, n):
    ans.append(i)
    ans.append(get_other_divisor(n, i))

def build_divisors_list(n):
    ans = []
    rng = range(1, get_range_end(n))
    for i in rng:
        if is_divisor(n, i):
            append_divisors(ans, i, n)
    return ans

def is_one(n):
    return n == 1

def get_last_element(lst):
    return lst[-1]

def to_str(x):
    return str(x)

def get_len(s):
    return len(s)

def main():
    inp = get_input()
    N = to_int(inp)
    ans = build_divisors_list(N)
    if is_one(N):
        print("1")
    else:
        last = get_last_element(ans)
        s = to_str(last)
        l = get_len(s)
        print(l)

main()