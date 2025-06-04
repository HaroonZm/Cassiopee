from collections import Counter

def compute():
    N = int(input())
    arr = list(map(lambda x: int(x), input().split()))
    freq = Counter()
    for x in arr:
        freq.setdefault(x, 0)
        freq[x] += 1

    sum_result = 0
    keys = [k for k in freq]
    for i in range(len(keys)):
        k = keys[i]
        v = freq[k]
        if v < k:
            sum_result += v
        else:
            for _ in range(v - k):
                sum_result += 1
    print(sum_result)

compute()