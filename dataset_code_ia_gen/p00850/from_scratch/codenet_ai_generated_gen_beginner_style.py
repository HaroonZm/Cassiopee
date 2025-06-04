def main():
    memo = {1: 0}  # operations needed to get x^1 is 0

    def min_ops(n):
        if n in memo:
            return memo[n]
        ops = float('inf')
        # Try to build n by multiplication from two smaller exponents
        for i in range(1, n):
            j = n - i
            # multiplication: op to i + op to j + 1
            ops = min(ops, min_ops(i) + min_ops(j) + 1)
        # Also try division: if n divides m, x^m/x^(m-n) = x^n
        for m in range(n + 1, 1001):
            if m % n == 0:
                ops = min(ops, min_ops(m) + 1)
        memo[n] = ops
        return ops

    while True:
        n = int(input())
        if n == 0:
            break
        print(min_ops(n))

main()