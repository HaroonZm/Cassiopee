def get_vals():
    return list(map(int, input().split()))
N,P = get_vals()
lst = []
b_total = 0

def calc(x, y):
    return (100 - P)*x + P*y

for j in range(N):
    entry = get_vals()
    b_total += entry[1]
    lst += [calc(entry[0], entry[1])]

from functools import reduce
lst.sort(reverse=True)

sum_acc = 0
ctr = 1
while ctr <= N:
    sum_acc = sum(lst[:ctr])
    if P*b_total <= sum_acc:
        print(ctr)
        break
    ctr += 1