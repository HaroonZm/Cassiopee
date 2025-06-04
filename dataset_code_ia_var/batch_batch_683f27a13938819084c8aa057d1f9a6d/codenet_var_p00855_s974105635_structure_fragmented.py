import array
import bisect

MAX_PRIME = 1299709

def create_true_array(length):
    return array.array("B", (True for _ in range(length)))

def mark_non_primes(is_prime, end):
    is_prime[0] = False
    is_prime[1] = False

def sieve_loop(is_prime, end, typecode):
    primes = array.array(typecode)
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            mark_composites(is_prime, i, end)
    return primes

def mark_composites(is_prime, prime, end):
    for j in range(2 * prime, end, prime):
        is_prime[j] = False

def sieve_of_eratosthenes(end, typecode="L"):
    assert end > 1
    is_prime = create_true_array(end)
    mark_non_primes(is_prime, end)
    primes = sieve_loop(is_prime, end, typecode)
    return primes

def get_next_prime(primes, index):
    return primes[index]

def is_prime_number(n, primes, index):
    return primes[index] == n

def get_prev_prime(primes, index):
    return primes[index - 1]

def calculate_gap(prev_prime, next_prime):
    return next_prime - prev_prime

def length_of_gap_containing(n, primes):
    idx = find_insertion_index(primes, n)
    if is_prime_number(n, primes, idx):
        return 0
    else:
        prev_prime = get_prev_prime(primes, idx)
        next_prime = get_next_prime(primes, idx)
        return calculate_gap(prev_prime, next_prime)

def find_insertion_index(primes, n):
    return bisect.bisect_left(primes, n)

def read_input():
    return input()

def parse_int(s):
    return int(s)

def handle_input(n, primes):
    if n == 0:
        return False
    else:
        print(length_of_gap_containing(n, primes))
        return True

def main_loop(primes):
    while True:
        s = read_input()
        n = parse_int(s)
        proceed = handle_input(n, primes)
        if not proceed:
            break

def main():
    primes = sieve_of_eratosthenes(MAX_PRIME + 1)
    main_loop(primes)

if __name__ == '__main__':
    main()