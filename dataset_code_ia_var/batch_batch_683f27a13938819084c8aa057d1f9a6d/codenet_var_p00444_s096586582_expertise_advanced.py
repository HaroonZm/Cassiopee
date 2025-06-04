from sys import stdin

def count_steps(n):
    steps = 0
    for inc, limit in [(500, 500), (100, 900), (50, 950), (10, 990), (5, 995), (1, 999)]:
        if n <= limit:
            k, n = divmod(limit - n, inc)
            steps += k + 1
            n = limit + inc
    return steps

for line in stdin:
    n = int(line)
    if n == 0:
        break
    print(count_steps(n))