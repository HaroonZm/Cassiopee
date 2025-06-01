import math
from bisect import bisect_left

def primes(limit):
    sieve = [True]*(limit+1)
    sieve[0], sieve[1] = False, False
    for number in range(2, int(math.sqrt(limit))+1):
        if sieve[number]:
            for multiple in range(number*number, limit+1, number):
                sieve[multiple] = False
    return list(filter(lambda x: sieve[x], range(limit+1)))

def search_pair(x, primes_list, length):
    count = 0
    idx = 0
    while idx < length:
        p = primes_list[idx]
        if p > x // 2:
            return count
        pos = bisect_left(primes_list, x - p)
        if pos < length and primes_list[pos] == x - p:
            count += 1
        idx += 1
    return count

prime_lst = primes(10**6)
len_prime = len(prime_lst)

def main():
    try:
        while True:
            n = int(input())
            if not n:
                break
            print(search_pair(n, prime_lst, len_prime))
    except EOFError:
        pass

if __name__ == "__main__":
    main()