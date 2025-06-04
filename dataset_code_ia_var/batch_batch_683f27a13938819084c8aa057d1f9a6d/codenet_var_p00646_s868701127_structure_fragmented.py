MAX = 1000004

def get_initial_ptbl():
    return [ 3,   5,   7,  11,  13,  17,  19,  23,  29,
       31,  37,  41,  43,  47,  53,  59,  61,  67,  71,
       73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
      127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
      179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
      233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
      283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
      353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
      419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
      467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
      547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
      607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
      661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
      739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
      811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
      877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
      947, 953, 967, 971, 977, 983, 991, 997 ]

def get_tbl():
    return [0]*MAX

def mark_multiples(p, tbl_arr):
    for i in range(p*p, MAX, p):
        tbl_arr[i] = 1

def extend_ptbl_and_tbl(ptbl_arr, tbl_arr):
    for p in ptbl_arr:
        mark_multiples(p, tbl_arr)
    for i in range(997, MAX, 2):
        if tbl_arr[i] == 0:
            ptbl_arr.append(i)

def sieve(tbl_arr, ptbl_arr):
    extend_ptbl_and_tbl(ptbl_arr, tbl_arr)

def handle_even_power(n):
    c = 0
    while True:
        n >>= 1
        c += 1
        if n & 1:
            break
    return c, n

def append_power_if_prime(n, power, tbl_arr):
    if n <= 1:
        return True
    if n <= MAX and tbl_arr[n] == 0:
        power.append(1)
        return True
    return False

def k_for_sqrt(n):
    return int(n**0.5)

def loop_prime_factors(n, ptbl_arr, tbl_arr, k, power):
    for p in ptbl_arr:
        if n <= 1:
            break
        if p > k or (n <= MAX and tbl_arr[n] == 0):
            power.append(1)
            break
        if n % p:
            continue
        c = 0
        while True:
            n //= p
            c += 1
            if n % p:
                break
        power.append(c)
    return power

def prime_factor(n, ptbl_arr, tbl_arr):
    power = []
    if (n & 1) == 0:
        c, n = handle_even_power(n)
        power.append(c)
    if append_power_if_prime(n, power, tbl_arr):
        return power
    k = k_for_sqrt(n)
    return loop_prime_factors(n, ptbl_arr, tbl_arr, k, power)

def read_input():
    return int(input())

def process_one_case(n, tbl_arr, ptbl_arr):
    if n == 1:
        print(1)
        return
    if n <= MAX and (n & 1) and tbl_arr[n] == 0:
        print(2)
        return
    power = prime_factor(n, ptbl_arr, tbl_arr)
    ans = calculate_ans(power)
    print(ans)

def calculate_ans(power):
    ans = 1
    for p in power:
        ans = ans * (1 + (p << 1))
    return (ans + 1) >> 1

def main_loop(tbl_arr, ptbl_arr):
    while True:
        n = read_input()
        if n == 0:
            break
        process_one_case(n, tbl_arr, ptbl_arr)

def main():
    tbl_arr = get_tbl()
    ptbl_arr = get_initial_ptbl()
    sieve(tbl_arr, ptbl_arr)
    main_loop(tbl_arr, ptbl_arr)

main()