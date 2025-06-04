from functools import reduce
from itertools import accumulate, islice

def main():
    n, t = map(int, input().split())
    an = list(map(int, input().split()))

    mi = list(accumulate(an, lambda x, y: min(x, y)))
    differences = list(map(lambda i: an[i] - mi[i - 1], range(1, n)))
    ma = max(differences, default=0)
    num_ma = sum(1 for x in differences if x == ma) if ma > 0 else 0
    print(num_ma)

main()