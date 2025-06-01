import sys

N = 1001

# Precompute Fibonacci modulo N for up to 1000 nodes
fib = [1, 1]
for i in range(2, 1001):
    fib.append((fib[i-1] + fib[i-2]) % N)

for line in sys.stdin:
    if not line.strip():
        continue
    V, d = map(int, line.split())
    vals = fib[1:V+1]  # F[i] = f(i) mod N for i=1..V

    # Count connected subsets
    count = 1
    for i in range(1, V):
        if abs(vals[i] - vals[i-1]) >= d:
            count += 1
    print(count)