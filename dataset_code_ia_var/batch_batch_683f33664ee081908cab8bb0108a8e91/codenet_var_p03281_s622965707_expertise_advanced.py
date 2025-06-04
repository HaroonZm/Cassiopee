from math import isqrt

def count_odd_with_8_divisors(n):
    def num_divisors(x):
        count = 1
        exp = 0
        i = 2
        y = x
        while i * i <= y:
            exp = 0
            while x % i == 0:
                x //= i
                exp += 1
            if exp:
                count *= (exp + 1)
            i += 1
        if x > 1:
            count *= 2
        return count

    return sum(
        num_divisors(i) == 8
        for i in range(1, n + 1, 2)
    )

print(count_odd_with_8_divisors(int(input())))