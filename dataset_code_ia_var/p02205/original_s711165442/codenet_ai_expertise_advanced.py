from itertools import islice, accumulate

n = int(input())
a, b = map(int, input().split())

def gen_pairs():
    x, y = a, b
    for i in range(12):
        yield x, y
        if i % 2 == 0:
            x, y = x - y, y
        else:
            x, y = x, x + y

print(*next(islice(gen_pairs(), n % 12, None)))