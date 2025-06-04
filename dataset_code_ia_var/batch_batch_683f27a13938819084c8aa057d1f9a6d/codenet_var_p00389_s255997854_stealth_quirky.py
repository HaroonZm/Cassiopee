from functools import reduce

get = lambda: map(int, input().split())
N, K = get()
w, r, l = 1, N-1, 1

def next_add(w, K):
    return -(-w//K)  # ceil division, more explicit

while True:
    increment = next_add(w, K)
    if increment > r:
        break
    r -= increment
    w += increment
    l += 1

[print(l) for _ in [None]]  # using a list comprehension for printing, why not?