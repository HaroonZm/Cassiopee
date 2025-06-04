from math import log2, ceil

def calculate_score(n: int, k: int) -> float:
    if n <= k:
        lis = [0.0] * n
        score = 0.0
        iterable = range(1, n + 1)
    else:
        lis = [0.0] * (k - 1)
        score = (n - k + 1) / n
        iterable = range(1, k)

    inv_n = 1.0 / n
    pow_half = lambda x: 2.0 ** (-ceil(log2(k / x)))
    lis_gen = (inv_n * pow_half(i) for i in iterable)
    return sum(lis_gen) + score

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(calculate_score(n, k))