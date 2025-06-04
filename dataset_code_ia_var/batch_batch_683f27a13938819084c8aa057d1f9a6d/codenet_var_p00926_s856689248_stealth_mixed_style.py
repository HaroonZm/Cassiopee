import sys

def next_token():
    for line in sys.stdin:
        for token in line.split():
            yield token

tokens = next_token()
run = True
while run:
    try:
        N = int(next(tokens))
        M = int(next(tokens))
    except:
        break
    arr = list()
    arr.extend([1 for _ in range(N+1)])
    _ = 0
    while _ < M:
        pair = []
        for _ in range(2):
            pair.append(int(next(tokens))-1)
        x = pair[0]
        y = pair[1]
        idx = x
        while idx < y:
            arr[idx] = 3
            idx += 1
        _ += 1
    def calc_sum(lst): return sum(lst)
    print(calc_sum(arr))