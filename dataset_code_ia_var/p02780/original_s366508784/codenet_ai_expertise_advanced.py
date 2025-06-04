from itertools import accumulate
from operator import add

def main():
    N, K = map(int, input().split())
    dice = list(map(int, input().split()))
    expected = [(p + 1) / 2 for p in dice]
    prefix = [0, *accumulate(expected)]
    max_E = max(prefix[i + K] - prefix[i] for i in range(N - K + 1))
    print(max_E)

if __name__ == "__main__":
    main()