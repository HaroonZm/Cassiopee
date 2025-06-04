from itertools import accumulate
import sys

def preprocess(limit):
    count = list(range(limit + 1))
    for i in range(2, (limit // 2) + 1):
        k = count[i] - 1
        count[i*2 : limit+1 : i] = (val - k for val in count[i*2 : limit+1 : i])
    count[1] = 2
    count = list(accumulate(count))
    return count

if __name__ == "__main__":
    input_func = sys.stdin.readline
    limit = 1000000
    count = preprocess(limit)
    t = int(input_func())
    for _ in range(t):
        n = int(input_func())
        print(count[n] - n + 1)