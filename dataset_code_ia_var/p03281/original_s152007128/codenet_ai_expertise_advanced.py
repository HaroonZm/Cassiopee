N = int(input())

def count_divisors(n):
    return sum(2 - (i * i == n) for i in range(1, int(n**0.5) + 1) if n % i == 0)

print(sum(1 for n in range(1, N+1, 2) if count_divisors(n) == 8))