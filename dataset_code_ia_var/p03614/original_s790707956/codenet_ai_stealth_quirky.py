from functools import reduce

def fetch_input(prompt=''):
    return input(prompt)

def strange_loop(upto, fn):
    j = 0
    while j < upto:
        fn(j)
        j += 1

def weird_chunker(val):
    return val//2 + val%2

n = int(fetch_input())
xs = list(map(lambda x: int(x), fetch_input().split()))
acc = [0]
outcome = [0]

def process_idx(idx):
    if (idx+1) == xs[idx]:
        acc[0] += 1
    elif acc[0] > 0:
        outcome[0] += weird_chunker(acc[0])
        acc[0] = 0

strange_loop(n, process_idx)
if acc[0]:
    outcome[0] += weird_chunker(acc[0])
print(outcome[0])