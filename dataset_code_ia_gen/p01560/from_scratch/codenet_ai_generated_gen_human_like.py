import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

# Convert probabilities to [0,1]
prob = [x/100 for x in p]

# Extract unique values of a to avoid duplicates and handle same a_k multiple times
# But problem seems to allow duplicates; so we keep all as is

ans = 0.0

# There are up to 2^n subsets, n <= 20 is OK
# For each subset, compute probability and the lcm of its elements
# Then calculate how many integers from 1 to m are divisible by lcm (if subset non empty)
# If empty subset, count is 0

def lcm(x, y):
    return x // math.gcd(x, y) * y

for mask in range(1 << n):
    p_sel = 1.0
    cur_lcm = 1
    selected = False
    for i in range(n):
        if mask & (1 << i):
            p_sel *= prob[i]
            selected = True
            cur_lcm = lcm(cur_lcm, a[i])
            if cur_lcm > m:
                break
        else:
            p_sel *= (1 - prob[i])
    if not selected:
        ans += 0.0  # no numbers chosen, count = 0
    else:
        if cur_lcm <= m:
            count = m // cur_lcm
        else:
            count = 0
        ans += p_sel * count

print(f"{ans:.7f}")