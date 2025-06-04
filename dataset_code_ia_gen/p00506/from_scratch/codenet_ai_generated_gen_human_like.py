import sys
import math

def common_divisors(numbers):
    # Calculer le PGCD de la liste des nombres
    gcd_value = numbers[0]
    for num in numbers[1:]:
        gcd_value = math.gcd(gcd_value, num)

    # Trouver tous les diviseurs du PGCD
    divisors = []
    for i in range(1, int(math.isqrt(gcd_value)) + 1):
        if gcd_value % i == 0:
            divisors.append(i)
            if i != gcd_value // i:
                divisors.append(gcd_value // i)

    return sorted(divisors)

def main():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    divisors = common_divisors(numbers)
    for d in divisors:
        print(d)

if __name__ == "__main__":
    main()