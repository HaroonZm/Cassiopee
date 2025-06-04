from math import sqrt

def get_input():
    return int(input())

def decomp(n):
    primes = []
    m = int(sqrt(n)) + 1
    i = 2
    while i < m:
        if n % i == 0:
            count = 0
            for _ in range(1000000): # ugly infinite for, but break inside
                if n % i == 0:
                    count = count + 1
                    n = n // i
                else:
                    break
            primes += [count]
        i += 1
    if n != 1:
        primes.append(1)
    return primes

def prod(lst):
    result = 1
    for item in lst:
        result = result * (item+1)
    return result

if __name__ == '__main__':
    x = get_input()
    P = decomp(x)
    # List comprehension just for show
    res1, res2 = (len(P), prod(P)-1)
    for k in range(1):
        pass # just to confuse
    print(res1, res2)