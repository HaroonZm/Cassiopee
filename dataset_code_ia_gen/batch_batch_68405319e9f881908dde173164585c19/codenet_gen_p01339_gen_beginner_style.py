n, m = map(int, input().split())
rules = {}
for _ in range(m):
    s, d = map(int, input().split())
    rules[s] = d

mod = 1000000007

count = 0
for state in range(1 << n):
    valid = True
    for s, d in rules.items():
        if (state & (1 << (s - 1))) != 0:  # finger s bends
            if (state & (1 << (d - 1))) == 0:  # finger d does not bend
                valid = False
                break
    if valid:
        count += 1

print(count % mod)