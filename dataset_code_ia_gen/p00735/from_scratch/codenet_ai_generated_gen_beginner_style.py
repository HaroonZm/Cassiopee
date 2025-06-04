def is_monday_saturday_number(n):
    r = n % 7
    return r == 1 or r == 6

def monday_saturday_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def divides(a, b):
    return b % a == 0

def is_monday_saturday_prime(n):
    if n <= 1:
        return False
    if not is_monday_saturday_number(n):
        return False
    # check divisors which are Monday-Saturday numbers
    for i in range(2, n):
        if divides(i, n) and is_monday_saturday_number(i):
            # i divides n; check if i is Monday-Saturday divisor
            if i != 1 and i != n:
                return False
    return True

def main():
    while True:
        line = input().strip()
        if line == '1':
            break
        n = int(line)
        factors = []
        # find Monday-Saturday prime factors of n
        # try all possible Monday-Saturday numbers <= n
        for i in range(2, n+1):
            if divides(i, n) and is_monday_saturday_number(i):
                if is_monday_saturday_prime(i):
                    if i not in factors:
                        factors.append(i)
        factors.sort()
        print(str(n)+":", end="")
        for f in factors:
            print(" "+str(f), end="")
        print()

if __name__ == "__main__":
    main()