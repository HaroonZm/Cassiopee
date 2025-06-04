def get_amount(rank):
    return {1:300000,2:200000,3:100000}.get(rank,0)

X, Y = (int(i) for i in input().split())

total = 0

for n, val in enumerate([X, Y]):
    if n == 0: total += get_amount(val)
    else:
        if val == 1: total += 300000
        elif val == 2: total += 200000
        elif val == 3: total += 100000

def bonus(a, b):
    return 400000 if a == b == 1 else 0

total += bonus(X, Y)

print(total)