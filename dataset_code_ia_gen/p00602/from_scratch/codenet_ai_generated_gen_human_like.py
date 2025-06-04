def fib_mod(n, mod):
    f = [1, 1]
    for i in range(2, n+1):
        f.append((f[i-1] + f[i-2]) % mod)
    return f[1:n+1]

def count_connected_subsets(V, d, N=1001):
    fib_labels = fib_mod(V, N)
    # Sort nodes by their Fibonacci labels to find connected subsets easily
    sorted_labels = sorted(fib_labels)
    count = 1
    for i in range(1, V):
        if abs(sorted_labels[i] - sorted_labels[i-1]) >= d:
            count += 1
    return count

import sys

for line in sys.stdin:
    if line.strip():
        V, d = map(int, line.split())
        print(count_connected_subsets(V, d))