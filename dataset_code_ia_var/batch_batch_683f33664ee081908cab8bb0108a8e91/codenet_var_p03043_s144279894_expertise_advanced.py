from decimal import Decimal, getcontext

def expected_value(n: int, k: int) -> float:
    getcontext().prec = 15
    total = Decimal(0)
    power_of_two = [1 << i for i in range(31)]
    for i in range(1, n + 1):
        # Binary search for minimal t such that i * t >= k with t = 2**m
        left, right = 0, 30
        while left < right:
            mid = (left + right) // 2
            if i * power_of_two[mid] >= k:
                right = mid
            else:
                left = mid + 1
        total += Decimal(1) / Decimal(power_of_two[left])
    return float(total / Decimal(n))

n, k = map(int, input().split())
print(expected_value(n, k))