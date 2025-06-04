N = input()
P = input().split()
P = [int(x) for x in P]

min_now = P[0]
count = 0

for p in P:
    if p <= min_now:
        count = count + 1
        min_now = p

print(count)